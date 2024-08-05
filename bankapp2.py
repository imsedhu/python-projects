import mysql.connector

from tabulate import tabulate
# Connect to the database

#var=packagename.conncet(host,user,password,database,cursorclass)
connection = mysql.connector.connect(host='localhost',
                            user='root',
                            password='1234',
                            database='Bankapp')

#function creation for Data insertion

def insert(no,Cname,bank,amount):
    c=connection.cursor()
    sql="Insert into mytable(sno, name, Bname , Balance) values(%s,%s,%s,%s)"
    c.execute(sql,(no,Cname,bank,amount))
    connection.commit()
    print("Data Insert SuccessFully")

def Update(amount,bank):
    c=connection.cursor()
    sql="update mytable set balance=%s where Bname=%s"
    c.execute(sql,(amount,bank))
    connection.commit()
    print("Data Updates SuccessFully")

def delete(Cname):
    c=connection.cursor()
    sql="delete from mytable where name=%s"
    c.execute(sql,(Cname,))
    print("Data deleted Success Fully")
    connection.commit()

def select():
    c=connection.cursor()
    sql="select * from mytable"
    c.execute(sql)
    x=c.fetchall()
    print(tabulate(x,headers=["SNO","NAME","BANK","BALANCE"]))
    connection.commit()
while(True):
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Delete Data")
    print("4.Select Data")
    print("5.Exit")

    choice=int(input("Enter Your Choice"))
    if(choice==1):
        no=int(input("Enter the Serial Number"))
        Cname=input("Enter the Name")
        bank=input("Enter the Bname")
        amount=int(input("Enter the Amount"))
        insert(no,Cname,bank,amount)
    elif(choice==2):
        bank=input("Enter the Bname")
        amount=int(input("Enter the Amount"))
        Update(amount,bank)
    elif(choice==3):
        Cname=input("Enter the Name")
        delete(Cname)
    elif(choice==4):
        select()
    elif(choice==5):
        quit()
    else:
        print("Invalid Selection Pls Try Again")