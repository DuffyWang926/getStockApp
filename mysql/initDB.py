import pymysql
import time

def initMysql(param):
    method = param['method']
    dataBase = 'test'
    tableName = param['tableName']
    
    db = pymysql.connect(host='localhost',
                             user='wefRoot',
                             password='wefRoot',
                             db=dataBase)
    cursor = db.cursor()
    
    # cursor.execute("CREATE DATABASE IF NOT EXISTS '%s' CHARACTER SET UTF8" % (dataBase)) 
    # sql="CREATE TABLE IF NOT EXISTS fuyuan0(ID INT UNSIGNED AUTO_INCREMENT,allNum VARCHAR (15)NOT NULL,availableNum VARCHAR (15)NOT NULL,date DATE,PRIMARY KEY (ID))"
    sql="CREATE TABLE IF NOT EXISTS `%s`(ID INT UNSIGNED AUTO_INCREMENT,allNum VARCHAR (15)NOT NULL,availableNum VARCHAR (15)NOT NULL,date DATE,PRIMARY KEY (ID))"  % (tableName)

    cursor.execute(sql)
    if method == 0:
        insertData(db, cursor, param)
    
   
def insertData(db, cursor, param):
    tableName = param['tableName']
    allNum = param['allNum']
    availableNum = param['availableNum']
    date = time.strftime("%Y-%m-%d", time.localtime())
    insert_sql = "insert into `%s` (`allNum`, `availableNum`, `date`)values('%s','%s','%s')" % (tableName,allNum, availableNum, date)
    try:
        select_sql = "select `allNum` from `%s` where `allNum`='%s'" % (tableName, allNum)
        response = cursor.execute(select_sql)
        db.commit()
        if response == 1:
            print('该数据已存在...')
        else:
            try:
                cursor.execute(insert_sql)
                db.commit()
                print('更新成功...')
                print(allNum)
                print(availableNum)
            except Exception as e:
                print('更新错误...', e)
                db.rollback()
    except Exception as e:
        print('查询错误...', e)
        db.rollback()
    finally:
        cursor.close()
        db.close()


