#pip install pytube
#pip install bs4
from pytube import YouTube
from bs4 import BeautifulSoup
import requests
def YouTubeDownLoadAPI(web,path):
    
    try:
        yt = YouTube(web)
        r = requests.get(web)
        soup = BeautifulSoup(r.text, "html.parser")
        print("下載的影片名稱為: " + soup.find("title").text)
        bsStream = str(yt.streams).replace("Stream:","a")
        try:
            videoType = []
            mp4 = []
            webm = []
            print("該網址畫質:")
            for i in yt.streams:
                bsStream = str(i).replace("Stream:","a")
                soup = BeautifulSoup(bsStream, "html.parser")
                res = soup.find('a')
                if res.get("res") != "None":
                    if res.get("mime_type") == "video/mp4":
                        mp4.append([res.get("mime_type"),res.get("type"),res.get("res")])
                    elif res.get("mime_type") == "video/webm":
                        webm.append([res.get("mime_type"),res.get("type"),res.get("res")])
                    # print("mime_type:" + res.get("mime_type")+ "   type:" + res.get("type") + "   res:" + res.get("res") )
                #print(res.get("res"))
                #print(res.get("type"))
                #print(res.get("mime_type"))
            mp4.sort(reverse = True)
            webm.sort(reverse = True)
            for i in mp4:
                print(i)
            for i in webm:
                print(i)
        except:
            a=0
        while True:
            type = input("輸入影片類型 mp4為1 webm為2:")
            if type == "1":
                file_extension = "mp4"
            elif type == "2":
                file_extension = "webm"
            res = input("輸入您要的畫質:")
            res = res +"p"
            video=yt.streams.filter(file_extension=file_extension, res=res).first()
            if video is None:
                print("畫質輸入錯誤!")
            else:
                print("影片下載中請稍後......")
                video.download(path)
                print("下載成功!! 檔案存放至: '%s'" %(path))
                break;
    except Exception as e:
        print("請確認您輸入的youtube網址!")
        print(e)
if __name__=='__main__':
    web = input("輸入網址:")
    #web = "https://www.youtube.com/watch?v=qvUWA45GOMg"
    #path = r'C:\Users\user-50\source'
    path = input("輸入您要存取的位置:")
    path = r'%s' %(path)
    YouTubeDownLoadAPI(web,path)