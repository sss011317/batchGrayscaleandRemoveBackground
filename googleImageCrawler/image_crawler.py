#pip install selenium
#pip install requests
from selenium import webdriver
import time
import os
import requests

# 使用代理的方法 ，可以直接windows使用代理，不用這麼麻煩
# browserOptions = webdriver.ChromeOptions()
# browserOptions.add_argument('--proxy-server=ip:port)
# browser = webdriver.Chrome(chrome_options=browserOptions)

#修改keyword便可以修改搜索關鍵詞
keyword = 'fujifilm'
#url = 'https://www.google.com.hk/search?q='+keyword+'&tbm=isch'
##去背
url = 'https://www.google.com.hk/search?q='+keyword+'&tbm=isch&tbs=ic:trans&hl=zh-TW&sa=X&ved=0CAIQpwVqFwoTCOjQ26LEhO4CFQAAAAAdAAAAABAC&biw=1903&bih=937'

class Crawler_google_images:
    # 初始化
    def __init__(self):
        self.url = url

    # 獲得Chrome驅動，並訪問url
    def init_browser(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-infobars")
        browser = webdriver.Chrome(chrome_options=chrome_options)
        # 訪問url
        browser.get(self.url)
        # 最大化視窗，之後需要爬取視窗中所見的所有圖片
        browser.maximize_window()
        return browser

    #下載圖片
    def download_images(self, browser,round=2):
        pathing = 'fujifilm_camera_png'
        picpath = './%s' %(pathing)
        # 路徑不存在時創建一個
        if not os.path.exists(picpath): os.makedirs(picpath)
        # 記錄下載過的圖片地址，避免重復下載
        img_url_dic = []

        count = 0 #圖片序號
        pos = 0
        for i in range(round):
            pos += 500
            # 向下滑動
            js = 'var q=document.documentElement.scrollTop=' + str(pos)
            browser.execute_script(js)
            time.sleep(1)
            # 找到圖片
            # html = browser.page_source#也可以抓取當前頁面的html文本，然後用beautifulsoup來抓取
            #直接通過tag_name來抓取是最簡單的，比較方便

            img_elements = browser.find_elements_by_tag_name('img')
            #遍歷抓到的webElement
            for img_element in img_elements:
                img_url = img_element.get_attribute('src')
                # 前幾個圖片的url太長，不是圖片的url，先過濾掉，爬後面的
                if isinstance(img_url, str):
                    if len(img_url) <= 200:
                        #將乾擾的goole圖標篩去
                        if 'images' in img_url:
                            #判斷是否已經爬過，因為每次爬取當前視窗，或許會重復
                            #實際上這里可以修改一下，將列表只存儲上一次的url，這樣可以節省開銷，不過我懶得寫了···
                            if img_url not in img_url_dic:
                                try:
                                    img_url_dic.append(img_url)
                                    #下載並保存圖片到當前目錄下
                                    filename = "./image/%s/%s.png" %(pathing,str(count))
                                    r = requests.get(img_url)
                                    with open(filename, 'wb') as f:
                                        f.write(r.content)
                                    f.close()
                                    count += 1
                                    print('this is '+str(count)+'st img')
                                    #防止反爬機制
                                    time.sleep(0.2)
                                except:
                                    print('failure')

    def run(self):
        self.__init__()
        browser = self.init_browser()
        self.download_images(browser,10)#可以修改爬取的頁面數，基本10頁是100多張圖片
        browser.close()
        print("Crawler Success!!")


if __name__ == '__main__':
    craw = Crawler_google_images()
    craw.run()