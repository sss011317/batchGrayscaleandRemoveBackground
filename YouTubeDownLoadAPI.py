from pytube import YouTube
def YouTubeDownLoadAPI(web,path):
    
    
    yt = YouTube(web)

    video=yt.streams.filter(file_extension='mp4', res='1080p').first()

    video.download(path)
    print("download scuess!! file in '%s'" %(path))

if __name__=='__main__':
    web = input("輸入網址:")
    #path = r'C:\Users\user-50\source\python\youtube'
    path = input("輸入您要存取的位置:")
    path = r'%s' %(path)
    YouTubeDownLoadAPI(web,path)