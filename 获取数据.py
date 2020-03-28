import pymysql
import openpyxl
import matplotlib.pyplot as plt 
import pandas as pd 

def readExcel(a):
    cell=[]
    data=openpyxl.load_workbook(a)
    sheet=data.get_sheet_by_name('Data')

    for row in list(sheet.rows)[26:]:
        cell.append([column.value for column in row])
    return cell

con=pymysql.connect(host='localhost',port=3306,user='root',passwd='syy981027',db='data',charset='utf8')
cur=con.cursor()



a='出生率.xlsx'
cell=readExcel(a)

cur.execute("DROP TABLE IF EXISTS birthrate")
cur.execute("create table birthrate(Date date not null,Value float(10) not null)")

for x,y in cell:
    
    sql="insert ignore into birthrate(Date,Value) values('%s','%f')" %(x,y)
    cur.execute(sql)
    con.commit()



a='死亡率.xlsx'
cell=readExcel(a)

cur.execute("DROP TABLE IF EXISTS deathrate")
cur.execute("create table deathrate(Date date not null,Value float(10) not null)")

for x,y in cell:
    
    sql="insert ignore into deathrate(Date,Value) values('%s','%f')" %(x,y)
    cur.execute(sql)
    con.commit()


    
a='人口增长率.xlsx'
cell=readExcel(a)

cur.execute("DROP TABLE IF EXISTS PGrate")
cur.execute("create table PGrate(Date date not null,Value float(10) not null)")
  
for x,y in cell:
    
    sql="insert ignore into PGrate(Date,Value) values('%s','%f')" %(x,y)
    cur.execute(sql)
    con.commit()



a='失业率.xlsx'
cell=readExcel(a)

cur.execute("DROP TABLE IF EXISTS unemploymentrate")
cur.execute("create table unemploymentrate(Date date not null,Value float(10) not null)")
  
for x,y in cell:
    
    sql="insert ignore into unemploymentrate(Date,Value) values('%s','%f')" %(x,y)
    cur.execute(sql)
    con.commit()



a='债务总额.xlsx'
cell=readExcel(a)

cur.execute("DROP TABLE IF EXISTS debt")
cur.execute("create table debt(Date date not null,Value float(10) not null)")

for x,y in cell:
    
    sql="insert ignore into debt(Date,Value) values('%s','%f')" %(x,y)
    cur.execute(sql)
    con.commit()



a='M2货币供应总量.xlsx'
cell=readExcel(a)

cur.execute("DROP TABLE IF EXISTS M2")
cur.execute("create table M2(Date date not null,Value float(10) not null)")

for x,y in cell:
    
    sql="insert ignore into M2(Date,Value) values('%s','%f')" %(x,y)
    cur.execute(sql)
    con.commit()


    
a='CPI.xlsx'
cell=readExcel(a)

cur.execute("DROP TABLE IF EXISTS cpi")
cur.execute("create table cpi(Date date not null,Value float(10) not null)")

for x,y in cell:

    sql="insert ignore into cpi(Date,Value) values('%s','%f')" %(x,y)
    cur.execute(sql)
    con.commit()



a='进口总额.xlsx'
cell=readExcel(a)

cur.execute("DROP TABLE IF EXISTS import")
cur.execute("create table import(Date date not null,Value float(10) not null)")

for x,y in cell:
    
    sql="insert ignore into import(Date,Value) values('%s','%f')" %(x,y)
    cur.execute(sql)
    con.commit()

    

a='出口总额.xlsx'
cell=readExcel(a)

cur.execute("DROP TABLE IF EXISTS export")
cur.execute("create table export(Date date not null,Value float(10) not null)")

for x,y in cell:
    
    sql="insert ignore into export(Date,Value) values('%s','%f')" %(x,y)
    cur.execute(sql)
    con.commit()



a='经常项目差额.xlsx'
cell=readExcel(a)

cur.execute("DROP TABLE IF EXISTS CAB")
cur.execute("create table CAB(Date date not null,Value float(10) not null)")

for x,y in cell:
    
    sql="insert ignore into CAB(Date,Value) values('%s','%f')" %(x,y)
    cur.execute(sql)
    con.commit()



a='联邦利率.xlsx'
cell=readExcel(a)

cur.execute("DROP TABLE IF EXISTS federalrate")
cur.execute("create table federalrate(Date date not null,Value float(10) not null)")

for x,y in cell:
    
    sql="insert ignore into federalrate(Date,Value) values('%s','%f')" %(x,y)
    cur.execute(sql)
    con.commit()



cur.close()


con.close()






