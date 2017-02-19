# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import re
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

html_tag = 'a'
html_tag2 = 'div'
url = "https://yandex.ru"
url2 = "https://lenta.ru/"

sfclass="link link_black_yes b-afisha__item"
sfclass2="b-yellow-box__wrap"

def func_find(html_tag, arg_url, arg_find):
    url = arg_url
    result=[]
    page=urllib.request.urlopen(url)
    soup=BeautifulSoup(page, 'html.parser')
    counter=0
    sfclass=arg_find
    for tag in soup.find_all(html_tag, class_=arg_find):
        counter=counter+1
        soup2=BeautifulSoup(str(tag),"html.parser")
        element=soup2.find(html_tag).text
        result.append(element)
    return(result)

#print(result)
#print (soup.title.string)

print(func_find(html_tag,url,sfclass))
