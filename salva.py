"""Feito para salvar as despesas por ano a partir do ano de 2008 em um csv"""



import urllib.request
from datetime import datetime
ano = 2007
data = datetime.now()
while ano < 2017:
    ano = ano + 1
    nome = str(data.day)+'-'+str(data.month)+'-'+str(data.year) + '-'+str(ano)+".csv"
    url_pura = 'http://riotransparente.rio.rj.gov.br/arquivos/Open_Data_Desp_'+str(ano)+'.asp'
    print(url_pura)
    local_filename,  headers  = urllib.request.urlretrieve(url_pura, nome)
    print(nome)


