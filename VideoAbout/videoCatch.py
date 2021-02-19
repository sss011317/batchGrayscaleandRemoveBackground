# pip install opencv-python
import cv2
import os
def VideoCatchToImg(videoName,videoType,savePath,time):
    if not os.path.exists(savePath): os.makedirs(savePath) #創建資料夾
    vc = cv2.VideoCapture(videoName+videoType) #讀取影片
    c=1
    
    if vc.isOpened(): #判斷檔案是否存在
        print("open film: %s%s -scuess!" %(videoName,videoType))
        rval , frame = vc.read()
    else:
        rval = False
     
    while rval:   #循環讀取頻率
        rval, frame = vc.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #轉灰階
        cv2.imshow(videoName, gray)
        if(c%time == 0): #每隔幾偵儲存圖片
            print('catch frames :' + str(c))
            cv2.imwrite('%s/%s-%s.jpg' %(savePath,videoName,str(c)),gray) #圖片儲存位置
        c = c + 1
        cv2.waitKey(1)


if __name__=='__main__':
    videoName= input("VideoName:")
    videoType = '.mp4'
    savePath = videoName
    time = 10  #影片偵數間格頻率
    VideoCatchToImg(videoName,videoType,savePath,time)
    