#dsheet.py (download sheet)
# Copyright (C) 2021 Gabriel Farias (gabrieldesousafarias@gmail.com) and contributors
#
# This module is part of GSheet
""" ? """
import requests

def dsheet(url_sheet):
    request = requests.get(url_sheet)
    if request:
        return request.content,'\nPlanilha acessada com sucesso!\n'
    else:
        return '','Erro ao acessar planilha'