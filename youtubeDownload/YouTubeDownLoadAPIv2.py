#pip install pytube
#pip install bs4
from pytube import YouTube
from bs4 import BeautifulSoup
def YouTubeDownLoadAPI(web,path):
    
    try:
        yt = YouTube(web)
        bsStream = str(yt.streams).replace("Stream:","a")
        try:
            print("該網址畫質:")
            for i in yt.streams:
                bsStream = str(i).replace("Stream:","a")
                soup = BeautifulSoup(bsStream, "html.parser")
                res = soup.find('a')
                if res.get("res") != "None":
                    print("mime_type:" + res.get("mime_type")+ "   type:" + res.get("type") + "   res:" + res.get("res") )
                #print(res.get("res"))
                #print(res.get("type"))
                #print(res.get("mime_type"))
        except:
            a=0
        while True:
            res = input("輸入您要的畫質:")
            video=yt.streams.filter(file_extension='mp4', res=res).first()
            if video is None:
                print("畫質輸入錯誤!")
            else:
                print("影片下載中請稍後......")
                video.download(path)
                print("下載成功!! 檔案存放至: '%s'" %(path))
                break;
    except:
        print("請確認您輸入的youtube網址!")
if __name__=='__main__':
    web = input("輸入網址:")
    #web = "https://www.youtube.com/watch?v=qvUWA45GOMg"
    #path = r'C:\Users\user-50\source'
    path = input("輸入您要存取的位置:")
    path = r'%s' %(path)
    YouTubeDownLoadAPI(web,path)