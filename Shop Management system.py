import mysql.connector
print ("                             ---SHOP MANAGEMENT SYSTEM--- ")
print("♦️════════════════════════════════════════════♦️")
print("╔════════════════════════════════════════════╗")
print("║                                ♦️ WELCOME TO OUR SHOP ♦️                                               ║")
print("╚════════════════════════════════════════════╝")
print("♦️════════════════════════════════════════════♦️")
mydb=mysql.connector.Connect(host="localhost",user='root',passwd='admin@3890')
mycursor=mydb.cursor()
mycursor.execute("create database if not exists sales_new")
mycursor.execute("use sales_new")
mycursor.execute("create table if not exists login(username varchar(25)not null,password varchar(25) not null)")
mycursor.execute("create table if not exists purchase(date date not null,name varchar(25) not null,code int not null,amount int not null)")
mycursor.execute("create table if not exists stock(code int not null,name varchar(25) not null,quantity int not null,price int not null)")
mydb.commit()
z=0
mycursor.execute("select * from login")
for i in mycursor:
    z+=1
if z==0:
    mycursor.execute("insert into login values('username','ng')")
    mydb.commit()    
while True:
    print(" → →→→→→→ ")
    print(" 1.Admin")
    print(" 2.Customer")
    print(" 3.Exit")
    print(" → →→→→→→ ")
    ch=int(input("Enter your choice:"))
    if ch==1:
        passs=input("Enter password:")
        mycursor.execute("select * from login")
        for i in mycursor:
            username,password=i
        if passs==password:

#ADMIN SECTION

            print("✯✯✯✯✯✯✯✯✯")
            print(" WELCOME, ADMIN!")
            print("✯✯✯✯✯✯✯✯✯")
            loop2='y'
            while(loop2=='y'or loop2=='y'):
                print("1.Add new price ")
                print("2.Updating price")
                print("3.Deleting price")
                print("4.Display all items")
                print("5.To change the password")
                print("6.Log Out")
                ch=int(input("Enter your choice:"))
                if ch==1:
                    loop='y'
                    while(loop=='y' or loop=='y'):
                        pcode=int(input("Enter code"))
                        pname=input("Enter product name")
                        quantity=int(input("Enter product quantity"))
                        price=int(input("Enter product price:"))
                        mycursor.execute("insert into stock values('"+str(pcode)+"','"+pname+"','"+str(quantity)+"','"+str(price)+"')")
                        mydb.commit()
                        print("Record Succesfully inserted! ✔")
                        loop=input("Do you want to enter more items(y/n):")
                    loop2=input("Do you want to continue editing stock(y/n): ")
                elif(ch==2):
                    loop='y'
                    while(loop2=='y' or loop2=='Y'):
                        code=int(input("Enter product code:"))
                        new_price=int(input("Enter new price:"))
                        mycursor.execute("update stock set price='"+str(new_price)+"'where code='"+str(code)+"'")
                        mydb.commit()
                        loop=input("Do you want to change price of any other item(y/n):")
                    loop2=input("Do you want to continue editing stock(y/n):")
                elif(ch==3):
                    loop='y'
                    while(loop=='y' or loop=='Y'):
                        code=int(input("Enter product code:"))
                        mycursor.execute("Delete from stock where code='"+str(code)+"'")
                        mydb.commit()
                        loop=input("Do you want to delete any other data(y/n): ")
                    loop2=input("Do you want to continue editing stock(y/n):")
                elif(ch==4):
                    mycursor.execute("select * from stock")
                    print("CODE || NAME || QUANTITY || PRICE")
                    for i in mycursor:
                        t_code,t_name,t_quan,t_price=i
                        print(f"{ t_code}||{t_name}||{t_quan}||{t_price}")
                elif(ch==5):
                    old_pass=input("Enter old password:")
                    mycursor.execute("select * from login")
                    for i in mycursor:
                        username,password=i
                    if(old_pass==password):
                        new_pass=input("Enter new password")
                        mycursor.execute("update login set password='"+new_pass+"'")
                        mydb.commit()
                elif(ch==6):
                    break
        else:
            print("OOPS! Your password was incorrect!")

#CUSTOMER SECTION
            
    elif(ch==2):
        print("1.Item bucket")
        print("2.Payment")
        print("3.View available items")
        print("4.Go back")
        ch2=int(input("Enter your choice:"))             
        if(ch2==1):
            name=input("Enter your name:")
            code=int(input("Enter product code:"))
            price=int(input("Enter product price:"))
            quantity=int(input("Enter product quantity:"))
            t_price=0
            t_quan=0
            mycursor.execute("select * from stock where code='"+str(code)+"'")
            for i in mycursor:
                t_code,t_name,t_quan,t_price=i
                break
            else:
                print("ERROR! Product you entered was not found")
            net_quan=t_quan-quantity
            amount=t_price*quantity
            mycursor.execute("update stock set quantity='"+str(net_quan)+"' where code='"+str(code)+"'")
            mycursor.execute("insert into purchase values(now(),'"+name+"','"+str(code)+"','"+str(amount)+"')")
            mydb.commit()
        elif(ch2==2):
               print(f"Amount to be paid{amount}")
        elif(ch2==3):
            print("CODE||NAME||PRICE")
            mycursor.execute("select * from stock")
            for i in mycursor:
                t_code,t_name,t_quan,t_price=i
                print(f"{ t_code}||{t_name}||{t_price}")
        elif(ch2==4):
            break
        elif(ch==3):
            break
