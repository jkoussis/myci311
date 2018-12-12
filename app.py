# import the Python client for PostgreSQL
import bottle_pgsql
import psycopg2 as db
import psycopg2.extras 
import settings
import sys

#login function
def log(l,p):
    postgresConnection = psycopg2.connect("dbname=ci user=postgres password=akis1976") 
    cursorObject = postgresConnection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    query = "SELECT count(*) from users where exists(select user_name,password from users where user_name='"+ l +"' and password='"+ p +"')" ; 	
    cursorObject.execute(query)
    results=0
    results=cursorObject.fetchone()[0]
    if results==0:
        return False
    else:
        return True

#register function		
def regi(l1,p1):
    postgresConnection = psycopg2.connect("dbname=ci user=postgres password=akis1976") 
    cursorObject = postgresConnection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
#First Check for uniqueness
    query1 = "SELECT count(*) from users where exists(select user_name from users where user_name='"+ l1 +"')";
    cursorObject.execute(query1)
    results=0
    results=cursorObject.fetchone()[0]
    if results==0:
#user_name given is unique so go on and register user
        query = "INSERT INTO users(user_name,password) vALUES('"+ l1 +"','"+ p1 +"')" ; 
        cursorObject.execute(query)
        postgresConnection.commit()
        return True
    else:
        return False     

#start of project queries
def qur1(date1,date2):
	
    postgresConnection = psycopg2.connect("dbname=ci user=postgres password=akis1976") 
    cursorObject = postgresConnection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    r = [("Type_id", "total"),]	
    	
    cursorObject.execute("select q1('%s','%s')"%(date1,date2))
    
    results=[]
    rows = cursorObject.fetchall()

    for row in rows:
        results.append(row)
	
    return r+results

def qur2(ty,dat1,dat2):
    
    postgresConnection = psycopg2.connect("dbname=ci user=postgres password=akis1976") 
    cursorObject = postgresConnection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    r = [("Start_date", "total"),]
     
    cursorObject.execute("select q2(%s,'%s','%s')"%(ty,dat1,dat2))
    
    results=[]
    rows = cursorObject.fetchall()

    for row in rows:
        results.append(row)
		
    return r+results
    
		
def qur3(dat):    
    
    postgresConnection = psycopg2.connect("dbname=ci user=postgres password=akis1976") 
    cursorObject = postgresConnection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    r = [("zip1", "max", "zip2", "type", "inc_id"),]
    cursorObject.execute("select q3('%s')"%(dat))	
    results=[]
    rows = cursorObject.fetchall()
    for row in rows:
        results.append(row)
     
    return r + results
	
def qur4(da1,da2):
    r   = [("TYPE_ID","AVERAGE"),]
    postgresConnection = psycopg2.connect("dbname=ci user=postgres password=akis1976") 
    cursorObject = postgresConnection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    cursorObject.execute("select q4('%s','%s')"%(da1,da2))
    results=[]
    rows = cursorObject.fetchall()

    for row in rows:
        results.append(row)
	
    return r + results
	
def qur5(d,x1,x2,y1,y2):    
    postgresConnection = psycopg2.connect("dbname=ci user=postgres password=akis1976") 
    cursorObject = postgresConnection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    r   = [("TYPE","No OF REQUESTS"),]
    cursorObject.execute("select q5('%s',%s,%s,%s,%s)"%(d,x1,x2,y1,y2))
    results=[]
    rows = cursorObject.fetchall()

    for row in rows:
        results.append(row)
	
    return r + results
	
def qur6(sdate1,sdate2):
    r   = [("SSA","NUM","DATE"),]
    postgresConnection = psycopg2.connect("dbname=ci user=postgres password=akis1976") 
    cursorObject = postgresConnection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    cursorObject.execute("select q6('%s','%s')"%(sdate1,sdate2))
    results=[]
    rows = cursorObject.fetchall()

    for row in rows:
        results.append(row)
		
    return r + results
	
def qur7():
    
    postgresConnection = psycopg2.connect("dbname=ci user=postgres password=akis1976") 
    cursorObject = postgresConnection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    r   = [("plate", "count"),]
    cursorObject.execute("select q7()")
    results=[]
    rows = cursorObject.fetchall()

    for row in rows:
        results.append(row)
	
    return r + results
    
def qur8():
    r   = [("color","")]
    postgresConnection = psycopg2.connect("dbname=ci user=postgres password=akis1976") 
    cursorObject = postgresConnection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    cursorObject.execute("select q8()")
    results=[]
    rows = cursorObject.fetchall()

    for row in rows:
        results.append(row)
	
    return r + results
	
def qur9(a):   
    postgresConnection = psycopg2.connect("dbname=ci user=postgres password=akis1976") 
    cursorObject = postgresConnection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    r = [('Rodent')]	
    cursorObject.execute("select q9('%s')"%a)
    results=[]
    rows = cursorObject.fetchall()

    for row in rows:
        results.append(row)
	
    return r+results

def qur10(b):
    postgresConnection = psycopg2.connect("dbname=ci user=postgres password=akis1976") 
    cursorObject = postgresConnection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    r = [("GarbageBaitRequest"),]
    cursorObject.execute("select q10('%s')"%b)
    results=[]
    rows = cursorObject.fetchall()

    for row in rows:
        results.append(row)
	
    return r+results
	
def qur11(c):  
    postgresConnection = psycopg2.connect("dbname=ci user=postgres password=akis1976") 
    cursorObject = postgresConnection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    r = [("RatsBaitRequest"),]
    cursorObject.execute("select q11('%s')"%c)
    results=[]
    rows = cursorObject.fetchall()

    for row in rows:
        results.append(row)
	
    return r+results
	
def qur12(c):  
    postgresConnection = psycopg2.connect("dbname=ci user=postgres password=akis1976") 
    cursorObject = postgresConnection.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    r = [("PoliceDistrict"),]
    cursorObject.execute("select q12('%s')"%c)
    results=[]
    rows = cursorObject.fetchall()

    for row in rows:
        results.append(row)
	
    return r+results

#end of project queries

#start of extra queries
def qur13(z):    
    
    postgresConnection = psycopg2.connect("dbname=ci user=postgres password=akis1976") 
    cursorObject = postgresConnection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    r = [("inc_id","status_id","type_id","date_reported"),]	
    query = "select inc_id,status_id,type_id,start_date from incident where zip="+z+"" ;   
    cursorObject.execute(query)
    results=[]
    rows = cursorObject.fetchall()
    for row in rows:
        results.append(row)
     
    return r + results
	
def qur14(s):    
    
    postgresConnection = psycopg2.connect("dbname=ci user=postgres password=akis1976") 
    cursorObject = postgresConnection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    r = [("inc_id","status_id","type_id","date_reported","addr"),]	
    query = "select inc_id,status_id,type_id,start_date,addr from incident where addr like '%"+ s +"%' " ;   
    cursorObject.execute(query)
    results=[]
    rows = cursorObject.fetchall()
    for row in rows:
        results.append(row)
     
    return r + results
	
def enif(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13):    
    
    postgresConnection = psycopg2.connect("dbname=ci user=postgres password=akis1976") 
    cursorObject = postgresConnection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    r = [("incident added"),]	
    query = "INSERT INTO incident (inc_id,status_id,type_id,start_date,addr,zip,x_coord,y_coord,ward,pol_distr,com_area,lat,long)"\
	" VALUES ("+d1+","+d2+", "+d3+", '"+d4+"','"+d5+"',"+d6+","+d7+","+d8+","+d9+","+d10+","+d11+","+d12+","+d13+")";   
    cursorObject.execute(query)
    postgresConnection.commit()
     
    return r
	
def tree_trim(t1,t2,t3):    
    
    postgresConnection = psycopg2.connect("dbname=ci user=postgres password=akis1976") 
    cursorObject = postgresConnection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    r = [("incident added"),]	
    query = "INSERT INTO tree_trims (tt_id,inc_id,tree_location)"\
	" VALUES ("+t1+","+t2+",'"+t3+"')";  
    cursorObject.execute(query)
    postgresConnection.commit()
     
    return r
	
	
#end of extra queries