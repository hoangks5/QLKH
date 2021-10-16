import requests
import urllib
def check():
    my_ip = requests.get('https://api.ipify.org').text   # IP của máy
    listtk = []
    with urllib.request.urlopen('https://raw.githubusercontent.com/hoangks5/QLKH/main/forwardchanel.txt') as url:  # Url danh sách IP có thể sử dụng
        s = url.read()
        key = s.decode("utf-8")
        key = key.splitlines()
        #print(key)
        for k in key:
            keyz = k.split(';')
            listtk.append(keyz[0])
    if my_ip not in listtk:
        while True:
            print('Key lỗi')

        
