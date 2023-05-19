import pymysql

def register(name, password, location='臺北市'):
    # 資料庫參數設定
    db_settings = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "221003red",
        "db": "mrt_foodmap",
        "charset": "utf8"
    }
    try:
        # 建立Connection物件
        conn = pymysql.connect(**db_settings)
        # 建立Cursor物件
        with conn.cursor() as cursor:
            # 新增資料SQL語法
            command_check_name = "SELECT Name FROM person"
            cursor.execute(command_check_name)
            name_list_res = cursor.fetchall()
            name_list = [name_list_res[i][0] for i in range(len(name_list_res))]
            # print(name_list)
            if name in name_list: #名稱需唯一
                return 'This name already exists'
            command_get_pID = "SELECT Max(PersonID) FROM person;"
            cursor.execute(command_get_pID)
            # PersonID 設置以及格式調整
            pID = cursor.fetchall()[0][0]
            pID = str(1 + int(pID))
            pID = pID.zfill(8)
            # 將使用者資料匯入資料庫
            command = f"INSERT INTO person VALUES('{pID}', '{name}', '{password}', '{location}')"
            # print(command)
            cursor.execute(command)
            message = cursor.fetchwarnings()
            print('message: {message}')
            # 儲存變更
            conn.commit()
    except Exception as ex:
        print(ex)
    # return pID


def log_in(name, password):
    # 資料庫參數設定
    db_settings = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "221003red",
        "db": "mrt_foodmap",
        "charset": "utf8"
    }
    try:
        # 建立Connection物件
        conn = pymysql.connect(**db_settings)
        # 建立Cursor物件
        with conn.cursor() as cursor:
            # 新增資料SQL語法
            command_check = f"SELECT Name, Password FROM person WHERE Name = '{name}'"
            print(command_check)
            cursor.execute(command_check)
            response = cursor.fetchall()[0]
            conn.commit()
            
            print(response)
            if password != response[1]:
                return False
            else:
                return True
            
    except Exception as ex:
        print(ex)
    # return pID

# register('candy', '000098')
print(log_in('candy', '000098'))