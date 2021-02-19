#pip install pymysql
import pymysql

def insertMysql(DataList):
    
    DataToSQL = ",".join(DataList)
    DataToSQL = "(" + DataToSQL + ")"
    try:
        conn = pymysql.connect(
                host='host',
                user='user',
                password='pwd',
                database='db',
                charset="utf8"
                )
        cursor = conn.cursor()
        query = str('INSERT INTO table (q1, q2, q3,)Values %s;'   %(DataToSQL)  )
        cursor.execute(query)
        conn.commit()
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(e)
       
if __name__=='__main__':
    DataList = ["value1","value2","value3"]
    if insertMysql(DataList):
        print("SQL INSERT SUCCESS")