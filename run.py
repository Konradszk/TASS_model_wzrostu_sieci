from main import main

print('Autorzy: Konrad Szczepaniak, Hubert Krawczak')
print('Skrypt wykonany na przedmot TASS 18Z')

url = 'https://fakty.interia.pl/malopolskie/news-tatry-ze-schroniska-ewakuowano-turystow,nId,2766003#comments4-1'

print('Program został uruchomiony')
main(url, database_sufix='TOPR')
print('Zakończono działanie programu')
