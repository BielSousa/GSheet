# gsheet.py
# Copyright (C) 2021 Gabriel Farias (gabrieldesousafarias@gmail.com) and contributors
#
# This module is part of GSheet
""" Module contains all the functionality related to the gsheet """


from bs4 import BeautifulSoup
from pss import print_out
from dsheet import dsheet

class GSheet(object):
    def __init__(self, url_sheet, tab_num=0):
        self.tables = []
        self.table = []
        self.columns = {}
        
        sheet, message = dsheet(url_sheet)
        print(message)
        self.soup = BeautifulSoup(sheet, 'html5lib')
        self.tables = self.soup.find_all('table')
        self.get_tables_names(self.soup)
        
            
            
    def get_tables_names(self, tables):
        _find_tables_names = tables.find_all('li')
        _tables_name = []
        
        for _name in _find_tables_names:
            _tables_name.append(_name.text)
        columns = [_tables_name,'']
        self.tables_name = {}
        
        for i, j in enumerate(_tables_name):
            self.tables_name.update({j:i})
        
        self.tab_names = _tables_name
        print('abas')
        print(self.tab_names)
        print('')   
    def select_table(self, table_name):
        self.tab_name = table_name
        _table = self.tables[self.tables_name[table_name]]
        _rows = _table.find_all('tr')
        
        for _row in _rows[1:]:
            _tds = _row.find_all('td')
            self.table.append([_td.text for _td in _tds])
    
    def show_table(self):    
        print_out(self.table, 'table', self.tab_name)
    
    def get_columns_name(self):
        columns = self.table
        print_out(columns, 'columns')
    
    def get_values(self):
        values = self.table
        print_out(values, 'values')

    def save_table(self, file_name):
        _file_name = file_name + '.txt'    
        with open(_file_name, 'w', encoding='utf-8') as f:
            for row in self.table:
                f.write(str(row).replace('[', '').replace(']', '').replace("'", '').replace(' ', ''))
                f.write('\n')
            f.write(self.tab_name)
        f.close()
        print('sheet saved')
        self.table = []
            
    
    def load_table(self, file_name):
        _file_name = file_name + '.txt'
        values = []
        with open(_file_name, 'r', encoding='utf-8') as f:
             lines = f.read().split('\n')
    
        for line in lines:
            values.append(line.split(','))
        self.table = values[0:-1]
        self.tab_name = str(values[-1]).replace("'", '').replace('[', '').replace(']', '')
        print('sheet loaded')
        #self._print_out(values[0:-1], 'table',str(values[-1]).replace("'", '').replace('[', '').replace(']', ''))
            
''' seleciona coluna
lista = []
lista = [list(zip(*self.table)), '']
print(lista[1])
'''