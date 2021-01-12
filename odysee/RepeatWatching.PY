
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from time import sleep
def txtWriteAPI(path):
    f = open(path)
    paths = []
    for path in f.readlines():
        paths.append(path)
    f.close()
    #print(paths)
    random(paths)

def random(paths):
    import random
    
    #print(len(paths))
    path = paths[random.randint(0,len(paths)-1)]
    th(path)
def th(path):
    #try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument('blink-settings=imagesEnabled=false')#不加載圖片, 提升速度
        chrome_options.add_argument('--headless') #瀏覽器不提供可視化頁面.
        #chrome_options.add_argument('window-size=640,480') #大小
        chrome_options.add_argument("--mute-audio") #
        driver =webdriver.Chrome(chrome_options=chrome_options)
        driver.get(path)
        for i in range(1,15):
            sleep(1)
            try:
                driver.find_element_by_xpath('//*[@id="vjs_video_3"]/button').click()
                print("影片執行成功!")
                for i in range(1,12):
                    sleep(1)
                    print("開啟影片執行: "+str(i)+"秒")
                print("影片關閉")
                break
            except:
                print("開啟網頁 等待: " +  str(i) + "秒")
                if i ==14:
                    print("等待時間過長網頁重新執行")
        
        #video = driver.find_element_by_xpath('//*[@id="vjs_video_3"]/button').click()
        #video = driver.find_element_by_xpath('//*[@id="app"]/div/header/div/div[1]/a/span/img').click()
        driver.quit()
  #  except:
  #      print("網頁開啟失敗,等待重啟中....")
  #      driver.quit()

if __name__=='__main__':
    while True:
      txtWriteAPI("./RepeatWatchingpath.txt")