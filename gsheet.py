import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re


class GSheet(object):
    def __init__(self, url_sheet, tab_num=0):
        self.tables = []
        self.table = []
        self.columns = {}
        
        try:
            self.request = requests.get(url_sheet)
            if self.request:
                print('\nPlanilha acessada com sucesso!\n')
            else:
                print('Erro ao acessar planilha')
            self.soup = BeautifulSoup(self.request.content, 'html5lib')
            self.tables = self.soup.find_all('table')
            self._get_tables_names(self.soup)
        except Error as e:
            print(e)
            
    def _print_out(self, data, obj='table', table_name=''):
        if obj == 'table':
            print('-'*(len(table_name)+11))
            print(f'| {obj}: {table_name} |')
            format_col = "|{:>20}|" * (len(data[0]))
            print("--"*11*len(data[0]))
            print(format_col.format(*data[0]))
            print("--"*11*len(data[0]))
            format_row = "|{:>20}|" * (len(data[0]))
            for row in data[1:]:
                print(format_row.format(*row))
            print("--"*11*len(data[0]))
            print('')
        if obj == 'columns':
            print(obj)
            format_col = "|{:>20}|" * (len(data[0]))
            print("--"*11*len(data[0]))
            print(format_col.format(*data[0]))
            print("--"*11*len(data[0]))
        if obj == 'values':
            format_row = "|{:>20}|" * (len(data[0]))
            print(obj)
            print("--"*11*len(data[0]))
            for row in data[1:]:
                print(format_row.format(*row))
            print("--"*11*len(data[0]))
            print('')
            
    def _get_tables_names(self, tables):
        _find_tables_names = tables.find_all('li')
        _tables_name = []
        
        for _name in _find_tables_names:
            _tables_name.append(_name.text)
        columns = [_tables_name,'']
        self.tables_name = {}
        
        for i, j in enumerate(_tables_name):
            self.tables_name.update({j:i})
           
    def select_table(self, table_name):
        self.tab_name = table_name
        _table = self.tables[self.tables_name[table_name]]
        _rows = _table.find_all('tr')
        
        for _row in _rows[1:]:
            _tds = _row.find_all('td')
            self.table.append([_td.text for _td in _tds])
    
    def show_table(self):    
        self._print_out(self.table, 'table', self.tab_name)
    
    def get_columns_name(self):
        columns = self.table
        self._print_out(columns, 'columns')
    
    def get_values(self):
        values = self.table
        self._print_out(values, 'values')

    def save_file(self):
            
        with open('table.txt', 'w', encoding='utf-8') as f:
            for row in self.table:
                f.write(str(row).replace('[', '').replace(']', '').replace("'", '').replace(' ', ''))
                f.write('\n')
            f.write(self.tab_name)
        f.close()
            
    
    def loading_file(self, file):
        _file = "./" + file + '.txt'
        values = []
        with open(_file, 'r', encoding='utf-8') as f:
             lines = f.read().split('\n')
    
        for line in lines:
            values.append(line.split(','))
        self.tables = values[0:-1]
        self.tab_name = str(values[-1]).replace("'", '').replace('[', '').replace(']', '')
        #self._print_out(values[0:-1], 'table',str(values[-1]).replace("'", '').replace('[', '').replace(']', ''))
            
''' seleciona coluna
lista = []
lista = [list(zip(*self.table)), '']
print(lista[1])
'''