import pymysql

# 資料庫參數設定
db_settings = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "221003red",
        "db": "mrt_foodmap",
        "charset": "utf8"
    }

def new_event():
    try:
        conn = pymysql.connect(db_settings)
        
    except Exception as ex:
        print(ex)
        