import pymysql

# 資料庫參數設定
db_settings = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "",
    "db": "mrt_foodmap",
    "charset": "utfmb4"
}

def new_event(p1_ID, time, food_type, station):
    try:
        conn = pymysql.connect(**db_settings)

        with conn.cursor() as cursor:
            # 確認這個人在一小時以內有沒有尚未配對的event
            command_time = f"select date_sub('{time}', interval 1 hour);"  # 時間
            cursor.execute(command_time)
            pre_time = cursor.fetchall()[0][0]
            print(pre_time)
            command_check = f'''SELECT * FROM event
WHERE Time BETWEEN	"{pre_time}" AND "{time}"
AND P1_ID = "{p1_ID}"
AND P2_ID = "00000000"'''
            cursor.execute(command_check)
            check = cursor.fetchall()
            
            if len(check) == 0:
                command = f'''INSERT INTO event(P1_ID, P2_ID, Time, FoodType, StationID)
VALUES("{p1_ID}", "00000000", "{time}", "{food_type}", "{station}")'''
                cursor.execute(command)
                conn.commit()
                return True
            else:
                print("這個人在一小時內曾發起過event，且尚未配對成功")
                return False
    except Exception as ex:
        print(ex)
        return False


def random_pair(p2_ID, time, food_type='All', station='All'):
    try:
        conn = pymysql.connect(**db_settings)

        with conn.cursor() as cursor:

            command = f''''''
            cursor.execute(command)
            return True
    except Exception as ex:
        print(ex)
        return False
