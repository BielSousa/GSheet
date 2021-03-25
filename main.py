from gsheet import GSheet

PLAN = 'https://docs.google.com/spreadsheets/d/e/your_key_sheet/pubhtml'

tabela = GSheet(PLAN)
tabela.select_table('senhas')
tabela.show_table()
tabela.save_table('senhas')
tabela.show_table()
tabela.load_table('senhas')
tabela.show_table()
