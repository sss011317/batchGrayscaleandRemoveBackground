def txtReadAPI(path):
    f = open(path, encoding="utf-8")
    f.seek(0)
    txt=f.read()
    f.close()
    print(txt)

if __name__=='__main__':
    path ="133127.txt"
    txtReadAPI(path)