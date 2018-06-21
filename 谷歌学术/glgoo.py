from bs4 import BeautifulSoup
import requests
import csv
import time


cook='xid=32201de47f1134227ed0937e1a129a55; NID=127=NpUXpvnAcVqGWvfYgaDn6sdKHBnk-QWTxD7H05Zmj5iPQ8j25wGD3TZq0SDbwy5L-IREwAzWWDvwyEudzqow6cn26UWwTx0qWpWSTb0d4jgdRBmwsmNsk7ka5lj8kHQ9; GSP=LM=1522932836:S=PT0o0jpvf6yxnAVf; Hm_lvt_0f47b9feac1b36431493d82d708e859a=1522932846; Hm_lpvt_0f47b9feac1b36431493d82d708e859a=1522933318'
headers = {
    "Cookie":cook,
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}



def getObj(url):
    try:
        html=requests.get(url,headers=headers,timeout=10)
        html.encoding="UTF-8"
    except HTTPError as e:
        print('HTTPError')
        return None
    try:
        bsObj = BeautifulSoup(html.text,'html.parser')
    except AttributeError as e:
        print('AttributeError')
        return None
    return bsObj

def crawl(url,csv_write):
    bsObj=getObj(url)
    divlist=bsObj.find('div',{'id':'gs_res_ccl_mid'}).find_all('div',class_='gs_ri')
    print('该页面文章个数为'+str(len(divlist)))
    for div in divlist:
        url=''
        try:
            a=div.find('h3').find('a')
            title=a.get_text()
            url=a.attrs['href']
        except:
            title=div.find('h3').get_text()
        yearin=div.find('div',class_='gs_a').get_text()
        spli=yearin.find('201')
        year=yearin[spli:spli+4]
        csv_write.writerow([title,url,year])
        print(title,url,year)

urlroot1='https://xues.glgoo.com/scholar?start='
urlroot2='&q=%E5%AE%A1%E6%9F%A5%E9%80%AE%E6%8D%95%E5%90%AC%E8%AF%81&hl=zh-CN&as_sdt=0,5&as_ylo=2013&as_yhi=2017'
f=open('glgoo.csv','a',newline='',encoding='gb18030')
csv_write=csv.writer(f)
# csv_write.writerow(['标题','链接','年份'])
for i in range(18,28):
    newUrl=urlroot1+str(i*10)+urlroot2
    print('即将爬取第'+str(i)+"页,链接为"+newUrl)
    crawl(newUrl,csv_write)
    time.sleep(20)