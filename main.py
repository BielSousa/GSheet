from gsheet import GSheet

PLAN = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRfwMNIJOSi-1BJ0ohLecIO3chCTHOmgi4FSzVnSH7XJm-XeCaci18rquS1fCzQK11NqXVnSqbklmrf/pubhtml'

tabela = GSheet(PLAN)
tabela.select_table('senhas')
tabela.show_table()
tabela.save_table('senhas')
tabela.show_table()
tabela.load_table('senhas')
tabela.show_table()