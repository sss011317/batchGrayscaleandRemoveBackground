#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import random
from time import sleep
def kuaidailiProxy(page,invisibilities):
    datas = [["IP","匿名度","類型","位置","驗證時間"]]
    for invisibilityUrl in invisibilities:
        for page in range(1,page+1):
            sleep(0.5)
            headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
            url = "https://www.kuaidaili.com/free/%s/%s/" %(invisibilityUrl,page)
            print("爬取網頁資料: " + url)
            r = requests.get(url,headers=headers)
            # print(r.text)
            soup = BeautifulSoup(r.text, 'html.parser')
            tbody = soup.find("tbody")
            # print(tbody)
            ips = (tbody.find_all(attrs={"data-title":"IP"}))
            ports = (tbody.find_all(attrs={"data-title":"PORT"}))
            Invisibilities = (tbody.find_all(attrs={"data-title":"匿名度"}))
            types = (tbody.find_all(attrs={"data-title":"类型"}))
            locations = (tbody.find_all(attrs={"data-title":"位置"}))
            lasttimes = (tbody.find_all(attrs={"data-title":"最后验证时间"}))
            
            for ip,port,invisibility,type,location,lasttime in zip(ips,ports,Invisibilities,types,locations,lasttimes):
                data= [ip.text+":"+port.text,invisibility.text,type.text,location.text,lasttime.text]
                datas.append(data)
            # for data in datas:
                # print(data)
    excelConvertAPI(datas,"kuaidailiProxyPool.xls","ProxyPool")
def excelConvertAPI(res,path,sheetName):
    import xlwt
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheetName)
    for a in range(len(res[0])):
        for b in range(len(res)):
                sheet.write(b,a,res[b][a])
    workbook.save(path)
    print("資料存取成功，存去位置為: %s" %(path))
if __name__=='__main__':
    while True:
        try:
            page = int(input("請輸入要爬取幾頁 : "))
            break
        except:
            print("輸入錯誤請重新輸入!")
    while True:
        try:
            choseInvisibility = int(input("高匿名代理輸入1,普通代理輸入2,兩者都要輸入3:"))
            if choseInvisibility ==1:
                invisibility =["inha"]
                break
            elif choseInvisibility ==2:
                invisibility =["intr"]
                break
            elif choseInvisibility ==3:
                invisibility = ["inha","intr"]
                break
            else:
                print("輸入錯誤請重新輸入!")
        except:
            print("輸入錯誤請重新輸入!")
    kuaidailiProxy(page,invisibility)