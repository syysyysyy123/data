import pymysql
import matplotlib.pyplot as plt 
import pandas as pd 


conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='syy981027',db='data',charset='utf8')

d = pd.read_sql('select Date,Value from cpi',con=conn)
x = list(d.Date) 
y = list(d.Value)
plt.plot(x,y,label='CPI')
plt.legend()
plt.xlabel("date") 
plt.ylabel("CPI(compared/%)")
plt.title('CPI')
plt.show()



d = pd.read_sql('select Date,Value from birthrate',con=conn)
x = list(d.Date) 
y1 = list(d.Value)
d = pd.read_sql('select Value from deathrate',con=conn)
y2 = list(d.Value)
d = pd.read_sql('select Value from pgrate',con=conn)
y3 = list(d.Value*10)
plt.plot(x,y1,label="birthrate")
plt.plot(x,y2,label='deathrate')
plt.plot(x,y3,label='pgrate')
plt.legend()
plt.xlabel("date") 
plt.ylabel("rate(1/1000)")
plt.title('birth&death&populationgrowth rate')
plt.show()



d = pd.read_sql('select Date,Value from export',con=conn)
x = list(d.Date) 
y1 = list(d.Value)
d = pd.read_sql('select Value from import',con=conn)
y2 = list(d.Value)
plt.plot(x,y1,label='export')
plt.plot(x,y2,label='import')
plt.legend()
plt.xlabel("date") 
plt.ylabel("Value/bn")
plt.title('export&import')
plt.show()


d = pd.read_sql('select Date,Value from unemploymentrate',con=conn)
x = list(d.Date) 
y = list(d.Value)
plt.plot(x,y,label='uneploymentrate')
plt.legend()
plt.xlabel("date") 
plt.ylabel("rate/%")
plt.title('uneploymentrate')
plt.show()




d = pd.read_sql('select Date,Value from cab',con=conn)
x = list(d.Date) 
y = list(d.Value)
plt.plot(x,y,label='cab')
plt.legend()
plt.xlabel("date") 
plt.ylabel("Value/mn")
plt.title('current account balance')
plt.show()




d = pd.read_sql('select Date,Value from debt',con=conn)
x = list(d.Date) 
y = list(d.Value)
plt.plot(x,y,label='debt')
plt.legend()
plt.xlabel("date") 
plt.ylabel("Value/mn")
plt.title('debt')
plt.show()




d = pd.read_sql('select Date,Value from m2',con=conn)
x = list(d.Date) 
y = list(d.Value)
plt.plot(x,y,label='M2')
plt.legend()
plt.xlabel("date") 
plt.ylabel("Value/bn")
plt.title('M2')
plt.show()



d = pd.read_sql('select Date,Value from federalrate',con=conn)
x = list(d.Date) 
y = list(d.Value)
plt.plot(x,y,label='federalrate')
plt.legend()
plt.xlabel("date") 
plt.ylabel("Value/mn")
plt.title('federalrate/% pa')
plt.show()
conn.close()



