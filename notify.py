from plyer import notification as nf
import requests
from bs4 import BeautifulSoup 
import time

def updateMe(title,message):
    nf.notify(title=title,message=message,app_icon="D://python//virus.ico",timeout=5) # give the path of the icon that you want in the alert window

def getData(url):
    req=requests.get(url)
    return req.text

if __name__=="__main__":
    while True:
        html=getData('https://www.mohfw.gov.in/')
        soup=BeautifulSoup(html,'html.parser')
        mydatastr=""
        for tr in soup.find_all('tbody')[7].find_all('tr'):
            mydatastr += tr.get_text()
        mydatastr=mydatastr[1:]  #maintain the pattern of the output so just slice 
        itemlist = mydatastr.split("\n\n")

        Selected_state=['Uttar Pradesh','Delhi','Gujarat']
        for item in itemlist[0:25]:
            datalist=item.split('\n')
            if datalist[1] in Selected_state:
                title='COVID-19 STATUS'
                detail=f"{datalist[1]}\nIndia : {datalist[2]} & Foriegn {datalist[3]}\ncured : {datalist[4]}\nDeaths : {datalist[5]}"
                updateMe(title,detail)
                time.sleep(2)
        time.sleep(1000)
