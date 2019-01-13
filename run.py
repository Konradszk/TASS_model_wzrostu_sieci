from main import main

print('Autorzy: Konrad Szczepaniak, Hubert Krawczak')
print('Skrypt wykonany na przedmot TASS 18Z')

# URL_TEST
url_test = 'https://fakty.interia.pl/malopolskie/news-tatry-ze-schroniska-ewakuowano-turystow,nId,2766003#comments4-1'

# PPOLSKA
# 1 119 comments 179 comments
url_ppolska = 'https://fakty.interia.pl/swiat/news-niezapowiedziana-wizyta-kim-dzong-una-w-chinach,nId,2772303#comments4-1'

# KGP1
# 1 1600 comments 2600 comments 2800 comments
url_KGP1 = 'https://fakty.interia.pl/polska/news-kgp-w-calym-kraju-kaskadowe-kontrole-predkosci,nId,2772281#comments4-1'
################################

# SZPIT
url_SZPIT = 'https://fakty.interia.pl/polska/news-nasz-dziennik-brak-personelu-w-szpitalach-ciecia-na-oddziala,nId,2774072#comments4-1'

# PIS
url_PIS = 'https://fakty.interia.pl/prasa/news-rz-pis-szykuje-sie-na-czarny-scenariusz,nId,2774097#comments4-1'

# PREMIER 400
url_PREMIER = 'https://fakty.interia.pl/raporty/raport-ue-przed-wyborami-europejskimi/artykuly/news-morawiecki-o-robieniu-z-polski-kozla-ofiarnego,nId,2774122#comments4-1'

print('Program został uruchomiony')
main(url=url_test, database_suffix='TOPR', should_ws=False, should_analyze=True)
print('Zakończono działanie programu')
