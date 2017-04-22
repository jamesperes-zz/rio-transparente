"""Feito para salvar as despesas por ano a partir do ano de 2008 em um csv"""
import urllib.request
from datetime import datetime

start_year = 2008
current_date = datetime.today()

raw_url = 'http://riotransparente.rio.rj.gov.br/arquivos/Open_Data_Desp_{year}.asp'
raw_filename = '{extract_date}_{reference_year}.csv'

for year in range(start_year, current_date.year + 1): # include current year in loop
    url = raw_url.format(year=year)
    filename = raw_filename.format(extract_date=current_date.strftime('%Y%m%d'), reference_year=year)
    urllib.request.urlretrieve(url, filename)