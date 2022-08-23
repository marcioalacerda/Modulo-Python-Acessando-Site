'''Programa que teste se o site está acessível pelo computador usado, mostrar status de resposta do site e abrir o navegador.'''
import urllib.request
import webbrowser
from time import sleep

try:
    site = urllib.request.urlopen('http://www.globo.com') # verifica se o site esta acessível
except urllib.error.URLError:
    print('\033[31mO site Pudim não está acessivél no momento.\033[m')
else:
    print('Resposta do estado: ', str(site.getcode())) # mostra o codigo de estado
    site = webbrowser.open('http://www.globo.com') # abri a web browser do site
    print('\033[34mAbrindo site...\033[m')
    sleep(1)
    print('\033[32mConsegui acessar o site Globo com sucesso!\033[m')
    #print(site.read()) # serve para ver o comando html