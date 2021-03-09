from PIL import Image
import os
def get(file):
    for img in os.listdir(file):
        imgfile = file +"\\"+ img
        changebackColor(imgfile)
def changebackColor(imgfile):
    im = Image.open(imgfile)
    x,y = im.size
    try:
      p = Image.new('RGBA', im.size, (255,255,255))
      p.paste(im, (0, 0, x, y), im)
      p.save(imgfile)
      print(imgfile  + "success change!")
    except Exception as e:
      print(e)
if __name__=='__main__':
    while True:
        file = input("輸入要轉換的資料夾:")
        file = r"%s" %(file)
        get(file)
        if file == "end":
            break