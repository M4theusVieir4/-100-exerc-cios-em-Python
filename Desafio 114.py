import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.request.URLError:
    print('Site não está acessível no momento.')
else:
    print('Site está acessível no momento.')
    print(site.read())