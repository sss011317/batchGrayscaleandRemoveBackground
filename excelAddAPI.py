## 2021/01/03 write by Ching 
##Notice: For entiry data, like  [["type","value"],["type1","valu1"],["type2","value2"]]
## res => write your data
## path => where is your Excel path
## SheetName => Create your SheetName
def ExcelAddAPI(res,path,sheetName):
    import xlrd
    from xlutils.copy import copy
    rb = xlrd.open_workbook(path, formatting_info=True)
    wb = copy(rb)
    sheet = wb.add_sheet(sheetName)
    for a in range(len(res[0])):
            for b in range(len(res)):
                    sheet.write(b,a,res[b][a])
    wb.save(path)        
    
if __name__=='__main__':
    path = input("path:")
    res =  input("res:")
    sheetName = input("sheetName:")
    ExcelAddAPI(res,path,sheetName)