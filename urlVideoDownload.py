import urllib.request
def urlVideoDownload(url,videoName):
    urllib.request.urlretrieve(url,videoName)
    print("下載成功!")
            
        
if __name__=='__main__':
    #url = 'https://mp4-a.udemycdn.com/2020-09-08_06-10-19-a480c2065702a17cb56d95be67a5847c/1/WebHD_720p.mp4?W1zUjS9tKxrNie87aIikib1qofykv9PCiCdLjZy0DWrWWdiId2sQ8kMVUsfHfL3NYrjTXwThfG5y-WKYeihhuLg4pP0nho0P3b50YFFiOPa1xULMnngreu5k2FNFt5TySap9IlG206npSB2LE_z9RWjVVdydn7kGWVhLpa0UvFJgFOTq'
    #videoName = '6-2 【理解】向 API 传入参数.mp4'
    url = input('輸入您要下載的mp4路徑:')
    videoName = input('輸入您要存儲的檔案名稱:')
    videoName = videoName +".mp4"
    urlVideoDownload(url,videoName)