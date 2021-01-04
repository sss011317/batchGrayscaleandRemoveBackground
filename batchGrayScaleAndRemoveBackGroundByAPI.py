
def searchFile():
    import os
    path  =input("輸入要選取的的資料夾:")
    path = r'%s' %(path)
    pathinto = input("輸入要輸出的資料夾:")
    pathinto = r'%s' %(pathinto)
    imagelist = os.listdir(path)#读取images文件夹下所有文件的名字

    functionUse = input("輸入1為灰階,輸入2為去背:")
    if functionUse == "1":
        Grayscale(path,pathinto,imagelist)
    elif functionUse =="2":
        removeBackGroundAPI(path,pathinto,imagelist)
    else:
        print("執行錯誤!")
def Grayscale(path,pathinto, imagelist):
    import cv2
    for image in imagelist:
        try:
            pathandimage = path +"\\"+ image
            #print(pathandimage)
            pathintoandimage = pathinto+"\\" + "gray_"+ image
            #print(">>"+pathintoandimage)
            image = cv2.imread(pathandimage)
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Result',image_gray)
            cv2.imwrite(pathintoandimage,image_gray)
            print("success!   image save to " + pathintoandimage)
        except Exception as e:
            print(image)
def removeBackGroundAPI(path,pathinto,imagelist):
    import requests
    key ='輸入你的KEY(請到該網站申請)'
    picName = 'numberplate2.jpg'
    nobgName= 'nobg_%s.jpg' %(picName)
    for image in imagelist:
        try:
            pathandimage = path + image
            pathintoandimage = pathinto+ "bg_" + image
            response = requests.post(
                'https://api.remove.bg/v1.0/removebg',
                files={'image_file': open(pathandimage, 'rb')},
                data={'size': 'auto'},
                headers={'X-Api-Key': key},
            )
            if response.status_code == requests.codes.ok:
                with open(pathintoandimage, 'wb') as out:
                    out.write(response.content)
            else:
                print("Error:", response.status_code, response.text)
            print("success!   image save to " + pathintoandimage)
        except Exception as e:
            print(image)
    
if __name__=='__main__':
    searchFile()