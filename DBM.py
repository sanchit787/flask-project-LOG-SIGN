import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='login')
    
def addEmp(t):
    db=getConnection()
    sql='insert into users values(%s,%s,%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def addInfo(t):
    db=getConnection()
    sql="insert into info1 values(%s,%s)"
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def selectAllinfo():
    db=getConnection()
    sql='select * from info1'
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

    
def deleteInfo(topic):
    db=getConnection()
    sql='DELETE FROM info1 WHERE topic=%s'
    cr=db.cursor()
    cr.execute(sql,topic)
    db.commit()
    db.close()

def selectInfoByTopic(topic):
    db=getConnection()
    sql='select * from info1 where topic=%s'
    cr=db.cursor()
    cr.execute(sql,topic)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist[0]

def updateInfo(t):
    db=getConnection()
    sql='UPDATE info1 SET content=%s WHERE topic=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def log(t):
    db=getConnection()
    sql="select username, password from users where username=%s and password=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data

