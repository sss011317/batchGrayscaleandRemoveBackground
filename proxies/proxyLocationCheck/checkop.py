import requests
from bs4 import BeautifulSoup
import threading
from time import sleep
import datetime
datas = []
def checkop(IP):
    global datas
    # IP = "1.20.217.221"
    # datas = []
    try:
        ip = IP[:IP.find(":")]
        data = []
        header = {
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
              "X-Requested-With": "XMLHttpRequest"}
              
        
        url = "https://tw.geoipview.com/?q=%s"  %(ip)
        r = requests.get(url, headers=header)
        soup = BeautifulSoup(r.text)
        infos = soup.find_all(class_="show2")
        dateNowPrint(IP+"  :  "+infos[1].text)
        data.append(IP)
        data.append(infos[1].text)
        datas.append(data)
    except Exception as e :
        dateNowPrint(e)
    
def writeProxyOP(res):
    import xlrd
    from xlutils.copy import copy
    sheetName = "Location"
    path ="proxyLocationCheck.xls"
    rb = xlrd.open_workbook(path, formatting_info=True)
    rows = rb.sheet_by_name(sheetName).nrows  #check the sheet_row
    wb = copy(rb)
    sheet = wb.get_sheet(sheetName)
    
    for a in range(len(res[0])):
            for b in range(len(res)):
                    sheet.write(rows+b,a,res[b][a])
    wb.save(path)        
    dateNowPrint("proxy紀錄儲存成功..")
def readTxt(path):
    f = open(path)
    f.seek(0)
    urls = []
    for url in f.readlines():
        url = url.strip('\n').strip()
        urls.append(url)
    f.close()
    return urls
#時間戳
def dateNowPrint(content):
    dateNow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    datenotprint = "["+dateNow+"] "+str(content)
    print(datenotprint)
if __name__=='__main__':
    ips = readTxt("checkop.txt")
    # ip = "51.158.165.18:8811"
    # print(ip.find(":"))
    # print(ip[:ip.find(":")])
    for ip in ips:
        t = threading.Thread(target=checkop,args=(ip,)) #建立線程
        t.start()
        if threading.active_count() == 200:  # set maximum threads.
            t.join()
    sleep(8)
    writeProxyOP(datas)