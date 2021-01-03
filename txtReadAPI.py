def txtWriteAPI(path):
    f = open(path)
    f.seek(0)
    txt=f.read()
    f.close()
    print(txt)

if __name__=='__main__':
    path ="133127.txt"
    txtWriteAPI(path)