## 2021/01/03 write by Ching 
##Notice: For entiry data, like  [["type","value"],["type1","valu1"],["type2","value2"]]
## res => write your data
## path => where do you wanna save your excel
## SheetName => Create your SheetName
def excelConvertAPI(res,path,sheetName):
    import xlwt
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheetName)
    for a in range(len(res[0])):
        for b in range(len(res)):
                sheet.write(b,a,res[b][a])
    workbook.save(path)
    print("save scuess!! the excel save as %s" %(path))
if __name__=='__main__':
    res = [["type","value"],["type1","valu1"],["type2","value2"]]
    path = "datatest.xls"
    sheetName = "ConvertTest"
    excelConvertAPI(res,path,sheetName)