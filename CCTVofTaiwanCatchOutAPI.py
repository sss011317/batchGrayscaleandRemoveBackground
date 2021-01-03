## 2021/01/03 write by Ching 
## Catch Out CCTV of Taiwan API from XML
def CCTVofTaiwanCatchOutAPI():
    import requests
    r = requests.get("https://thbapp.thb.gov.tw/opendata/cctv/info/cctvs.xml")
    html = r.content
    html_doc = str(html,'utf-8')

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_doc,'html.parser')
    CCTVofName = 'SurveillanceDescription'
    CCTVofLink = 'VideoStreamURL'
    CCTVofRoadName = 'RoadName'
    CCTVofRoadID = 'RoadID'
    CCTVofNameList = soup.select(CCTVofName)
    CCTVofLinkList = soup.select(CCTVofLink)
    CCTVofRoadNameList = soup.select(CCTVofRoadName)
    CCTVofRoadIDList = soup.select(CCTVofRoadID)
    CCTVofList =[]
    for roadID,name,roadName,link in zip(CCTVofRoadIDList,CCTVofNameList,CCTVofRoadNameList,CCTVofLinkList):
        print(roadID.text,name.text,roadName.text,link.text)
        list = [roadID.text,name.text,roadName.text,link.text]
        CCTVofList.append(list)
    print(CCTVofList)
if __name__=='__main__':
    CCTVofTaiwanCatchOutAPI()