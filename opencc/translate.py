from opencc import OpenCC

def s2twp(content):
    cc = OpenCC('s2twp')  # convert from Simplified Chinese to Traditional Chinese
    # can also set conversion by calling set_conversion
    # cc.set_conversion('s2tw')
    converted = cc.convert(content)
    
    return converted
def txtReadAPI(path):
    f = open(path, encoding="utf-8")
    f.seek(0)
    txt=f.read()
    f.close()
    print(txt)
    return txt
def txtWriteAPI(data,path):
    f = open(path,'w+')
    f.write(data)
    f.close()
    print("write down success! the txt save as %s" %(path))
if __name__ == '__main__':
    # content = input("輸入文章:")
    content = txtReadAPI("simple.txt")
    converted =s2twp(content)
    txtWriteAPI(converted,"traditional.txt")