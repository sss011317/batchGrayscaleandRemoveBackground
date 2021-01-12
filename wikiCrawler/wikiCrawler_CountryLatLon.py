import requests
from bs4 import BeautifulSoup
def txtWriteAPI(path):
    f = open(path,encoding='utf-8')
    citys = []
    for city in f.readlines():
        city = city.strip("\n")
        city = city.strip(" ")
        citys.append(city)
    wikiCrawler(citys)
    #print(citys)
def excelConvertAPI(res,path,sheetName):
    import xlwt
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheetName)
    for a in range(len(res[0])):
        for b in range(len(res)):
                sheet.write(b,a,res[b][a])
    workbook.save(path)
    print("save scuess!! the excel save as %s" %(path))    
    
def wikiCrawler(citys):
    citysData = []
    for city in citys:
        cityLonLat =[]
        try:

            path = "https://en.wikipedia.org/wiki/" + city
            response = requests.get(path)
            soup = BeautifulSoup(response.text, "html.parser")
            #namee = soup.find("h1")
            latitude = soup.find("span","latitude")
            longitude = soup.find("span","longitude")

            print("city:" + city+"  latitude:"+ latitude.text , "  longitude:"+longitude.text)

            cityLonLat.append(city)
            #cityLonLat.append(namee.text)
            cityLonLat.append(latitude.text)
            cityLonLat.append(longitude.text)
            citysData.append(cityLonLat)

        except:

            cityLonLat.append(city)
            cityLonLat.append("-")
            cityLonLat.append("-")
            citysData.append(cityLonLat)
    
    
    excelConvertAPI(citysData,"country.xls","latlon")
    
    
    
if __name__=='__main__':
    txtWriteAPI("country.txt")
    #wikiCrawler(["承德市","沧州市"])