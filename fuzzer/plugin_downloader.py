import requests
import os
from bs4 import BeautifulSoup as bs

def find_plugins_list(url, i):
    if i == 1:
        url = "https://wordpress.org/plugins/browse/popular/"
        res = requests.get(f'{url}')
        if res.status_code != 200:
            return False
        soup = bs(res.text, "html.parser")
        entries = soup.select("h3.entry-title > a") 
        for entry in entries:
            plugin_list.append(entry.attrs['href'])
    else:
        res = requests.get(f'{url}/{i}/')
        if res.status_code != 200:
            return False
        soup = bs(res.text, "html.parser")
        entries = soup.select("header.entry-header > h3.entry-title > a")  
        for entry in entries:
            plugin_list.append(entry.attrs['href'])
        
def download_plugins_from_list(url):
    res = requests.get(f'{url}')
    #print(res.text)
    soup = bs(res.text, "html.parser")
    a_tags = soup.find_all('a', class_="wp-block-button__link wp-element-button")

# 조건에 맞는 href 값 출력
    for a in a_tags:    
        if 'download' in a['href']:
            temp = a['href']
            res = requests.get(temp)
            filename = os.path.basename(temp)
            with open(filename, 'wb') as file:
                file.write(res.content)
                

WP_PLUGINS = "https://wordpress.org/plugins/browse/popular/page/"
plugin_list = []
i = 1 # page number

while i < 3:
    if i == 1:   # i가 1인 경우는 /browse/popular로 자동 리디렉 돼서 스킵함.
        url = "https://wordpress.org/plugins/browse/popular/"
        status = find_plugins_list(url, i)
        if status == False : pass 
    else:
        status = find_plugins_list(WP_PLUGINS, i)   
        if status == False : pass

    i += 1 

for p_url in plugin_list:
    download_url = download_plugins_from_list(p_url) # list에 저장된 다운 받을 플러그인 url을 넘겨서 다운진행.