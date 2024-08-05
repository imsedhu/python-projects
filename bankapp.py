import mysql.connector
from tabulate import tabulate

connection = mysql.connector.connect(host='localhost',
                            user='root',
                            password='1234',
                            database='Bankapp')



def insert(no,cname,bank,amount):
  c=connection.cursor()
  sql = "insert into mytable(sno, name, bname, balance) values(%s,%s,%s,%s)"
  c.execute(sql,(no,cname,bank,amount))
  connection.commit()
  print("values successfully inserted")
def update(amount,cname):
  c=connection.cursor()
  sql = "update mytable set balance=%s where name=%s"
  c.execute(sql,(amount,cname)) 
  connection.commit()
  print("values successfully updated") 
def delete(cname):
  c=connection.cursor()
  sql = "delete from mytable where name=%s" 
  c.execute(sql,(cname,))
  connection.commit()
  print("values successfully deleted")
def showtable():
  c=connection.cursor()
  sql = "select * from mytable"
  c.execute(sql)
  x=c.fetchall()
  print(tabulate(x,headers=["SNO","NAME","BANK","BALANACE"]))
  connection.commit() 
  
while(True):
    print("1. insert values")
    print("2. update amount")
    print("3. delete account")
    print("4. display table")
    print("5. quit")
    choice = int(input("enter your choice: "))
    if(choice==1):
      no = int(input("enter the sno: "))
      cname = input("enter the customer name: ")
      bank = input("enter the bank name: ")
      amount = int(input("enter the amount: "))
      insert(no,cname,bank,amount)
    elif(choice==2):
      amount = int(input("enter the amount: ")) 
      cname = input("enter the customer name: ")
      update(amount,cname)
    elif(choice==3):
      cname = input("enter the customer name: ")
      delete(cname)
    elif(choice==4):
      showtable()
    elif(choice==5):
      quit()
    else:
      print("invalid choice pls try again")      