from typing import Dict

import requests
from pathlib import Path
import shutil
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from urllib.parse import urlparse, urlunparse, urlencode
from datetime import date, datetime, timedelta
import time
import codecs
import win32com.client as win32
import ssl

class ParseAP:
    dir_name = 'parser_files'
    headers = \
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
        }
    __parse_time = 0
    export_path = Path(__file__).parent.joinpath(dir_name).joinpath('export')

    def path_check(self, ap):
        if not self.export_path.exists():
            self.export_path.mkdir()
            self.export_path.joinpath(ap).mkdir()
            self.logger(f'{ap} Parser: Export directory was created')
            return str(self.export_path.joinpath(ap))
        else:
            if not self.export_path.joinpath(ap).exists():
                self.export_path.joinpath(ap).mkdir()
                self.logger(f'{ap} Parser: Export directory was created')
                return str(self.export_path.joinpath(ap))
            else:
                self.logger(f'{ap} Parser: Export directory exists')
                return str(self.export_path.joinpath(ap))

    def logger(self, log_text):
        log_dir = Path(__file__).parent.joinpath(self.dir_name)

        if not log_dir.exists():
            log_dir.mkdir()
        log_file_dir = log_dir.joinpath('log_file.log')
        log_file = open(log_file_dir, 'a')

        log_file.write(f'{datetime.now().time()} : {log_text}\n')

    def _decoder(self, file_in, file_out=None, in_encode='utf-8', out_encode='cp1251', ap=None):
        deleter = True
        if file_out is None:
            deleter = False
            file_out = file_in

        coded_file = codecs.open(file_in, 'r', in_encode).read()
        codecs.open(file_out, 'w', out_encode).write(coded_file)
        Path(__file__).parent.joinpath(file_in).unlink(missing_ok=True) if deleter is True else None

        ap = 'UNKNOWN' if ap is None else ap
        self.logger(f'{ap} Parser: CSV file encoded - {file_out}')

    def _get_response(self, response_url):
        next_time = self.__parse_time + self.delay
        url = response_url.replace(urlparse(response_url).netloc, urlparse(self.start_url).netloc)
        while True:
            if next_time > time.time():
                time.sleep(next_time - time.time())
            response = requests.get(url, headers=self.headers)
            self.__parse_time = time.time()
            if response.status_code == 200:
                return response
            time.sleep(self.delay)

class ParseSVO(ParseAP):
    parse_url = ''
    task_list = []
    parse_dict = {}
    export_joinpath = ''
    files_created = {'arr': None, 'dep': None}

    def __init__(self, start_url, delay=3):
        self.start_url = start_url
        self.delay = delay

    def svo_decoder(self, file_in, file_out=None, in_encode='utf-8', out_encode='utf-16'):
        deleter = True
        if file_out is None:
            deleter = False
            file_out = file_in

        coded_file = codecs.open(file_in, 'r', in_encode).read()
        codecs.open(file_out, 'w', out_encode).write(coded_file)
        Path(__file__).parent.joinpath(file_in).unlink(missing_ok=True) if deleter is True else None

    def run(self):
        self.logger('SVO Parser: Started')
        self.export_joinpath = self.path_check('SVO')
        self.url_configurator_svo(self.start_url, 'departure')
        self._parse()
        self.save('D')
        self.url_configurator_svo(self.start_url, 'arrival')
        self._parse()
        self.save('A')
        with open(self.export_path.joinpath('SVO').joinpath('last_parsed.notify'), 'w') as n:
            print(f'{self.files_created["arr"][-33:]}\n{self.files_created["dep"][-35:]}', file=n)
        self.logger('SVO Parser: .notify file is created')
        self.logger('SVO Parser: Stopped')

    def url_configurator_svo(self, start_url, direction):
        date_format = '%Y-%m-%d'
        today_t = datetime.now()
        today = today_t.strftime(date_format)
        yesterday_t = today_t - timedelta(days=1)
        yesterday = yesterday_t.strftime(date_format)
        query_dict = {'direction': direction, 'dateStart': yesterday + 'T00:00:00+03:00',
                      'dateEnd': today + 'T00:00:00+03:00', 'perPage': '9999', 'page': '0', 'locale': 'ru'}
        parts = list(urlparse(start_url))
        parts[4] = urlencode(query_dict)
        parse_url = urlunparse(parts)
        self.parse_url = parse_url
        self.logger(f'SVO Parser: Parse url configured - "{parse_url}"')

    def _parse(self):
        self.task_list.clear()
        response = self._get_response(self.parse_url)
        init_dict = response.json()
        self.task_list = init_dict.get("items")
        self.logger(f'SVO Parser: {self.parse_url} was parsed')

    def save(self, _dir):
        self.parse_dict.clear()
        counter_id = 0
        for di in self.task_list:
            counter = 0
            counter_id = 0
            for it in di:
                if isinstance(di[it], dict) is False:
                    self.parse_dict[it] = []
                else:
                    counter_id += 1
                    for it_d in di[it]:
                        self.parse_dict[it + '_' + it_d + str(counter)] = []
        for di in self.task_list:
            counter = 0
            counter_id = 0
            for it in di:
                if isinstance(di[it], dict) is False:
                    self.parse_dict[it].append(di[it])
                else:
                    counter_id += 1
                    for it_d in di[it]:
                        self.parse_dict[it + '_' + it_d + str(counter)].append(di[it][it_d])
            for it in self.parse_dict:
                if len(self.parse_dict[it]) < len(self.parse_dict['i_id']):
                    self.parse_dict[it].append('')
        data_frame = pd.DataFrame(self.parse_dict)
        for i in self.parse_dict:
            for y in range(0, len(self.parse_dict[i])):
                if isinstance(data_frame[i][y], dict) is False:
                    if (data_frame[i][y] is None) is False:
                        if data_frame[i][y].replace(".", "").isdigit():
                            if data_frame[i][y].find(".") != -1:
                                data_frame[i][y] = float(data_frame[i][y])
                            else:
                                data_frame[i][y] = int(data_frame[i][y])
                        else:
                            if data_frame[i][y].find("+03:00") != -1:
                                data_frame[i][y] = data_frame[i][y].replace("+03:00", "")
                                data_frame[i][y] = datetime.strptime(data_frame[i][y].replace('T', ' '),
                                                                     '%Y-%m-%d %H:%M:%S')
                                data_frame[i][y] = data_frame[i][y].strftime('%d.%m.%Y %H:%M:%S')
        filename = self.export_joinpath + f'\SVO schedule_{"DEPARTURE" if _dir == "D" else "ARRIVAL"}_' \
                                          f'{(date.today() - timedelta(days=1)).strftime("%Y%m%d")}.csv'
        data_frame.to_csv(filename, sep=',', index=False)
        self.logger(f'SVO Parser: CSV file created - {filename}')
        self.svo_decoder(file_in=filename, ap='SVO')
        if _dir == 'D':
            self.files_created['dep'] = filename
        else:
            self.files_created['arr'] = filename

class ParseOVB(ParseAP):
    task_html = ''
    parse_list = []
    parse_dict = {}
    export_joinpath = ''
    data_list_dep = ['Город отправления','Город прибытия', 'Номер рейса', 'Время по расписанию', 'Время расчетное',
                 'Сектор', 'Авиакомпания', 'Тип ВС', 'Стойка регистрации', 'Начало регистрации',
                 'Посадка на борт', 'Сектор выхода на посадку', 'Статус']
    data_list_arr = ['Город отправления', 'Город прибытия', 'Номер рейса', 'Время по расписанию', 'Время расчетное',
                     'Сектор', 'Авиакомпания', 'Тип ВС', 'Лента выдачи багажа', 'Статус']
    files_created = {'arr': None, 'dep': None}

    def __init__(self, start_url):
        self.start_url = start_url

    def run(self):
        self.logger('OVB Parser: Started')

        self.export_joinpath = self.path_check('OVB')
        self.url_configurator_ovb(self.start_url)
        self._parse('D')
        self.save('D')
        self._parse('A')
        self.save('A')
        with open(self.export_path.joinpath('OVB').joinpath('last_parsed.notify'), 'w') as n:
            print(f'{self.files_created["arr"][-33:]}\n{self.files_created["dep"][-35:]}', file=n)
        self.logger('OVB Parser: .notify file is created')
        self.logger('OVB Parser: Stopped')

    def _parse(self, _dir):
        parse_html = bs(self.task_html, "html.parser")
        if _dir == 'D':
            dep = parse_html.find('div', attrs={'class': 'col fl'})
        else:
            dep = parse_html.find('div', attrs={'class': 'col fl unvisible'})
        dev = dep.find_all('div', attrs={'class': 'fi-title'})
        status_html = dep.find_all('span', attrs={'class': 'tth-status'})
        table_rows = dep.find_all('ul')
        res = list()
        res_napr = list()
        res_status = list()
        for sp in status_html:
            st = sp.text.strip()
            if st:
                res_status.append(st)
        for div in dev:
            napr = div.text.strip()
            if napr:
                res_napr.append(napr)
        for i, st in enumerate(res_napr):
            res_napr[i] = st.replace(' → ', ',').split(',', 1)
        for ul in table_rows:
            li = ul.find_all('li')
            row = [li.text.strip() for li in ul if li.text.strip()]
            if row:
                res.append(row)
        for i, i_list in enumerate(res):
            row = i_list
            for y, y_list in enumerate(i_list):
                if y_list.find('Номер рейса:') != -1:
                    res[i][y] = y_list.replace('Номер рейса: ', '')
                if y_list.find('По расписанию:') != -1:
                    res[i][y] = y_list.replace('По расписанию: ', '')
                if y_list.find('Расчетное время:') != -1:
                    res[i][y] = y_list.replace('Расчетное время: ', '')
                if y_list.find('Сектор:') != -1:
                    res[i][y] = y_list.replace('Сектор: ', '')
                if y_list.find('Авиакомпания:') != -1:
                    res[i][y] = y_list.replace('Авиакомпания: ', '')
                if y_list.find('Тип ВС:') != -1:
                    res[i][y] = y_list.replace('Тип ВС: ', '')
                if y_list.find('Стойка регистрации:') != -1:
                    res[i][y] = y_list.replace('Стойка регистрации: ', '')
                if y_list.find('Начало регистрации:') != -1:
                    res[i][y] = y_list.replace('Начало регистрации: ', '')
                if y_list.find('Посадка на борт:') != -1:
                    res[i][y] = y_list.replace('Посадка на борт: ', '')
                if y_list.find('Сектор выхода на посадку:') != -1:
                    res[i][y] = y_list.replace('Сектор выхода на посадку: ', '')
                if y_list.find('Лента выдачи багажа:') != -1:
                    res[i][y] = y_list.replace('Лента выдачи багажа: ', '')
        if _dir == 'D':
            for i, i_list in enumerate(res):
                res[i] = res_napr[i] + i_list + res[i + 1] + res[i + 2]
                res[i].append(res_status[i])
                del res[i + 1]
                del res[i + 1]
        else:
            for i, i_list in enumerate(res):
                res[i] = res_napr[i] + i_list + res[i + 1]
                res[i].append(res_status[i])
                del res[i + 1]
        self.parse_list = res
        self.logger(f'OVB Parser: {"DEPARTURE" if _dir == "D" else "ARRIVAL"} was parsed')

    def url_configurator_ovb(self, url):
        params = {'day': 'yesterday', 'items_count': 0, 'rel': "departure"}
        response = requests.post(url, params=params, headers=self.headers)
        self.task_html = response.content

    def save(self, _dir):
        self.parse_dict = {}
        if _dir == 'D':
            for i in self.data_list_dep:
                self.parse_dict[i] = []
        else:
            for i in self.data_list_arr:
                self.parse_dict[i] = []
        for i, i_list in enumerate(self.parse_list):
            counter = 0
            for list_dict in self.parse_dict:
                self.parse_dict[list_dict].append(i_list[counter])
                counter += 1
        data_frame = pd.DataFrame(self.parse_dict)
        filename = self.export_joinpath + f'\OVB schedule_{"DEPARTURE" if _dir == "D" else "ARRIVAL"}_' \
                                          f'{(date.today() - timedelta(days=1)).strftime("%Y%m%d")}.csv'
        data_frame.to_csv(filename, sep=',', index=False)
        self.logger(f'OVB Parser: CSV file created - {filename}')
        self._decoder(file_in=filename, ap='OVB')
        if _dir == 'D':
            self.files_created['dep'] = filename
        else:
            self.files_created['arr'] = filename


if __name__ == '__main__':
    svo_url = 'https://www.svo.aero/bitrix/timetable/'
    ovb_url = 'https://tolmachevo.ru/ajax/ttable.php'

    svo_parser = ParseSVO(svo_url, delay=0.5)
    svo_parser.run()
    ovb_parser = ParseOVB(ovb_url)
    ovb_parser.run()
