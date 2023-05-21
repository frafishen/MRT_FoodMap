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

# 00000000: null person ID  #, p2_ID = "00000000"
def new_event(p1_ID, time, food_type, station):
    try:
        conn = pymysql.connect(db_settings)
        
        with conn.cursor() as cursor:            
            command = f'''INSERT INTO event(P1_ID, P2_ID, Time, FoodType, StationID) 
	VALUES("{p1_ID}", "00000000", "{time}", "{food_type}", "{station}")'''
            
    except Exception as ex:
        print(ex)

# "2023-05-20 12:00:00"