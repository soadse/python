import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://g1.globo.com/')
except urllib.error.URLError:
    print('O site G1 não está acessível no momento.')
else:
    print('Consegui acessar o site G1 com sucesso!')
    print(site.read())
