#ffmpeg -i  C:\Users\user-50\source\test\12789.m3u8 -c copy video.mp4
#import urllib.request import urlretrieve

#pip install m3u8
#pip install ffmpy

import urllib.request
import m3u8
import ffmpy
def m3u8download(m3u8url,saveFile):
    Tscount =0 
    uri = m3u8url.rsplit('/',1)[0] +"/"
    m3u8FileName = m3u8url.split('/')[-1]
    urllib.request.urlretrieve(m3u8url,saveFile+m3u8FileName) #存取m3u8檔案
    print("m3u8: "+ m3u8FileName +" 下載成功!")
    m = m3u8.load(m3u8url)
    key = m.data['segments'][0]['key']['uri'] # 因為該網址的影片都只有一個key，為節省網路，不一一確認key是否正確
    urllib.request.urlretrieve(uri+key,saveFile+key) #存取key(XXX.ts)檔案
    print("key: "+ key +" 下載成功!")
    totalTsFile = len(m.data['segments'])
    print("開始下載ts種子...")
    for i in m.data['segments']: #從m3u8檔案內擷取ts路徑
        Tscount +=1
        print("進度:"+str(Tscount)+"/"+str(totalTsFile))
        urllib.request.urlretrieve(uri+i['uri'],saveFile+i['uri'])
    print("下載完成!")
    combineTs(m3u8FileName,saveFile)
    

def combineTs(m3u8FileName,saveFile):
    resFileName = 'test.mp4'
    ff = ffmpy.FFmpeg(
    inputs={saveFile+m3u8FileName: None},
    outputs={saveFile+resFileName: '-c copy'}
    )
    ff.run()
    print("合併成功，檔名為:" + resFileName)
if __name__=='__main__':
    m3u8url = 'https://tggfk0.cdnlab.live/hls/zrWMq0QSQKaUUTDwDmQfYQ/1610631861/9000/9671/9671.m3u8'
    saveFile = './'
    m3u8download(m3u8url,saveFile)
