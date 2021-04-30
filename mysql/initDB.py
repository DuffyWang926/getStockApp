import pymysql
import time

def initMysql(param):
    method = param['method']
    dataBase = 'test'
    tableName = param['tableName']
    allNum = param.get('allNum')
    nowPrice = param.get('nowPrice')
    db = pymysql.connect(host='localhost',
                             user='wefRoot',
                             password='wefRoot',
                             db=dataBase)
    cursor = db.cursor()
    
    # cursor.execute("CREATE DATABASE IF NOT EXISTS '%s' CHARACTER SET UTF8" % (dataBase)) 
    # sql="CREATE TABLE IF NOT EXISTS fuyuan0(ID INT UNSIGNED AUTO_INCREMENT,allNum VARCHAR (15)NOT NULL,availableNum VARCHAR (15)NOT NULL,date DATE,PRIMARY KEY (ID))"
    if allNum:
        sql="CREATE TABLE IF NOT EXISTS `%s`(ID INT UNSIGNED AUTO_INCREMENT,allNum VARCHAR (15)NOT NULL,availableNum VARCHAR (15)NOT NULL,date DATE,PRIMARY KEY (ID))"  % (tableName)
    elif nowPrice:
        sql="CREATE TABLE IF NOT EXISTS `%s`(ID INT UNSIGNED AUTO_INCREMENT,nowPrice float(10,3)NOT NULL,maxPrice float(10,3)NOT NULL,minPrice float(10,3)NOT NULL,percentage VARCHAR (10)NOT NULL,recordTime VARCHAR (15)NOT NULL,date DATE,PRIMARY KEY (ID))"  % (tableName)
    cursor.execute(sql)
    if method == 0:
        insertData(db, cursor, param)
   
def insertData(db, cursor, param):
    tableName = param['tableName']
    allNum = param.get('allNum')
    availableNum = param.get('availableNum')
    nowPrice = param.get('nowPrice')
    maxPrice = param.get('maxPrice')
    minPrice = param.get('minPrice')
    percentage = param.get('percentage')
    recordTime = param.get('recordTime')
    date = time.strftime("%Y-%m-%d", time.localtime())
    if allNum and availableNum:
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
    elif nowPrice:
        insert_sql = "insert into `%s` (`nowPrice`, `maxPrice`, `minPrice`, `percentage`,`recordTime`, `date`)values('%s','%s','%s','%s','%s','%s')" % (tableName, nowPrice, maxPrice, minPrice, percentage, recordTime, date)
        try:
            select_sql = "select `recordTime` from `%s` where `recordTime`='%s'" % (tableName, recordTime)
            response = cursor.execute(select_sql)
            db.commit()
            if response == 1:
                print('该数据已存在...')
            else:
                try:
                    cursor.execute(insert_sql)
                    db.commit()
                    print('插入成功...')
                except Exception as e:
                    print('插入错误...', e)
                    db.rollback()
        except Exception as e:
            print('查询错误...', e)
            db.rollback()
        finally:
            cursor.close()
            db.close()

