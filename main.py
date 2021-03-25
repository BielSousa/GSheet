from gsheet import GSheet

PLAN = 'https://docs.google.com/spreadsheets/d/e/your_key_sheet/pubhtml'

tabela = GSheet(PLAN)
tabela.select_table('plan1')
tabela.show_table()
tabela.save_table('my_table')
tabela.show_table()
tabela.load_table('mytable')
tabela.show_table()
