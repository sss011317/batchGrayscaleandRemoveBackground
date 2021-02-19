#pip install xlrd
def readProxyHub(path,sheetNameList):
    import xlrd
    print("導入proxy資料中，請稍後...")
    book = xlrd.open_workbook(path)
    # print(book.sheet_names())
    proxies = []
    for sheetName in sheetNameList:
        sh = book.sheet_by_name(sheetName)
        cell=sh.cell(rowx=29, colx=5)
        
        for rows in range(1,sh.nrows):
            cell1 = sh.cell_value(rowx=rows,colx=1)
            cell2 = sh.cell_value(rowx=rows,colx=2)
            cell3 = sh.cell_value(rowx=rows,colx=3)
            cell4 = sh.cell_value(rowx=rows,colx=4)
            cell5 = sh.cell_value(rowx=rows,colx=5)
            data = [cell1,cell2,cell3,cell4,cell5]
            datas.append(data)
        print("讀取%s的proxies成功" %(sheetName)) 
        
    return datas
    
    
if __name__=='__main__':
    sheetNameList=[]
    path= ""
    datas = readProxyHub(path,sheetNameList)