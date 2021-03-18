import requests as req
from bs4 import BeautifulSoup
from time import sleep as wait
from emailer import main as send_mail

def get_price(link):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    res = req.get(link, headers=headers)
    content = res.content
    site = BeautifulSoup(content, 'html.parser')
    price_str = site.find('span', 'price-template__text')
    price = float(price_str.text.replace(',', '.'))
    
    while True:
        if price < 799.0:
            #if send.lower() == 'e':
            email = input('Informe seu e-mail: ')
            send_mail(email, link)
            break
        else:
            pass
        wait(18000)
'''
def setup():
    link = input('Insira o link do produto: ')
    global send
    send = input('Deseja receber notificação no e-mail ou SMS? (e/s) ')
    if 'magazineluiza.com.br' not in link.lower():
        print('envie um link correto. (magaine luiza apenas)')
        wait(1)
        setup()
    else:
        get_price(link)
setup()
'''
send_mail('jvdebossan@gmail.com', 'funcionando')
get_price('https://www.magazineluiza.com.br/cadeira-gamer-moobx-gt-racer-preto-bela/p/ac8e1haage/mo/mecg/')