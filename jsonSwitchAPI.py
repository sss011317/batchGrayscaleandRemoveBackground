## 2021/01/03 write by Ching 
## link => where is your Json File
## DictSource => whats' your Json Types
def jsonSwitch(link,dictSource):
    import requests
    import json
    data =[]
    jsonSource = requests.get(link)
    # res = json.dumps(jsonSource.text, ensure_ascii=False).encode('utf8')
    jsonRes = json.loads(jsonSource.text)
    print("共有筆數:",len(jsonRes))

    
    if dictSource != "":
        for jsondata in jsonRes:
            secdata = []
            for demand in dictSource:
                try:
                    secdata.append(jsondata[demand])
                except:
                    secdata.append("空值")
            data.append(secdata)
    print(data)
    
if __name__=='__main__':
    link= "https://mort.moi.gov.tw/opendata/serviceList.do?method=exportJson"
    dictSource=["placeId","placeName","belongCityId","phone"]
    jsonSwitch(link,dictSource)