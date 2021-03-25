#pss.py (print sheet shell)
# Copyright (C) 2021 Gabriel Farias (gabrieldesousafarias@gmail.com) and contributors
#
# This module is part of GSheet
""" ? """

def print_out(data, obj='table', table_name=''):
    if data:
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
    else:
        print(data)