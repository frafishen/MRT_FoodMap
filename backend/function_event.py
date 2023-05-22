import pymysql
import random

# 資料庫參數設定
db_settings = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "221003red",
    "db": "mrt_foodmap",
    "charset": "utf8"
}

def new_event(p1_Name, time, food_type, station):
    try:
        conn = pymysql.connect(**db_settings)

        with conn.cursor() as cursor:
            command_getID = f'SELECT PersonID FROM person WHERE Name = "{p1_Name}"'
            cursor.execute(command_getID)
            p1_ID = cursor.fetchall()[0][0]
            # print(p1_ID)
            # 確認這個人在一小時以內有沒有尚未配對的event
            command_time = f"select date_sub('{time}', interval 1 hour);"  # 時間
            cursor.execute(command_time)
            pre_time = cursor.fetchall()[0][0]
            command_check = f'''SELECT * FROM event
WHERE Time BETWEEN	"{pre_time}" AND "{time}"
AND P1_ID = "{p1_ID}"
AND P2_ID = "00000000"'''
            cursor.execute(command_check)
            check = cursor.fetchall()
            
            if len(check) == 0: # no events
                # new event
                command = f'''INSERT INTO event(P1_ID, P2_ID, Time, FoodType, StationID)
VALUES("{p1_ID}", "00000000", "{time}", "{food_type}", "{station}")'''
                cursor.execute(command)
                conn.commit()
                return True
            else:
                print("The person has newed an event within one hour, and hasn't paired yet")
                return False
    except Exception as ex:
        print(ex)
        return False


def random_pair(p2_ID, time, food_type='All', station='All'):
    try:
        conn = pymysql.connect(**db_settings)

        with conn.cursor() as cursor:
            # P2_ID = 00000000, 發起時間在一小時以內，食物種類跟站
            command = f'''SELECT * FROM event
WHERE P2_ID = "00000000"
AND Time between date_sub("{time}", interval 1 hour) and "{time}"'''
            if food_type != 'All':
                command = command + f'\nAND FoodType = "{food_type}"'
            if station != 'All':
                command = command + f'\nAND StationID = "{station}"'
            print(command)
            cursor.execute(command)
            result = cursor.fetchall()
            
            random_choice = random.choice(result)
            print('Choiced: ', random_choice)
            return random_choice
    except Exception as ex:
        print(ex)
        return False

def successfully_pair(p1_ID, p2_ID):
    pass