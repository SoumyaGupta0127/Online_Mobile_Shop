import random

#----------SETTING UP CONNECTION BETWEEN PYTHON AND MYSQL------------------------------------
import sys
try:
    import mysql.connector as mysqlcon
    mycon=mysqlcon.connect(host='127.0.0.1',user='root',passwd='root1234',database='Project')   #DON'T FORGET TO FILL
    cursor=mycon.cursor(buffered=True)
    a=mycon.is_connected()
    if a==False:
        sys.exit()
except Exception as e:
    print(e)
    sys.exit(e)

#----------CREATING TABLES AND DATABASES IN MYSQL--------------------------------------------

cursor.execute('CREATE DATABASE IF NOT EXISTS Computer_Project')

cursor.execute('USE Computer_Project')

cursor.execute('CREATE TABLE IF NOT EXISTS Phones(ProductID INT(5) NOT NULL, Brand VARCHAR(20) NOT NULL,\
Model VARCHAR(50) NOT NULL, Price INT, Availability VARCHAR(30), ContactDealer INT)')

cursor.execute('CREATE TABLE IF NOT EXISTS Orders(OrderID INT(4) NOT NULL, Name VARCHAR(30) NOT NULL,\
City VARCHAR(30), Contact NUMERIC(12) NOT NULL, Product VARCHAR(50),Brand VARCHAR(20) NOT NULL,\
Price INT)')

cursor.execute('CREATE TABLE IF NOT EXISTS OrderStatus(OrderID INT(4) NOT NULL, Name VARCHAR(30) NOT NULL,\
Contact NUMERIC(12) NOT NULL,OrderStatus VARCHAR(20) NOT NULL, PaymentStatus VARCHAR(10) NOT NULL)')

cursor.execute('CREATE TABLE IF NOT EXISTS Stock(Brand VARCHAR(20) NOT NULL, Model VARCHAR(50) NOT NULL,\
InStock INT(5))')

#----------

def option(name,city,contact):
    print('''******************************************************************
    1. View products
    2. Place an order
    3. View order placed
    4. View order status
    5. Cancel order
    6. Back''')
    nam=name
    cit=city
    cont=contact
    
    try:
        
        ah=int(input("Enter a Choice:"))
        if ah==1:
            search(nam,cit,cont)
        elif ah==2:
            place(nam,cont,cit)
        elif ah==3:
            import mysql.connector as mysqlcon
            try:
                
                mycon=mysqlcon.connect(host='127.0.0.1',user='root',passwd='root1234',database='Project')
                cursor=mycon.cursor(buffered=True)
                print()
                cursor.execute('SELECT * FROM orders where Name =%s',(nam,))
                y=cursor.fetchall()
                if not y:
                    print()
                    print()
                    print("No orders placed yet")
                    print()
                    print()
                else:
                    print()
                    print('OrderID, Name, City, Contact, Product, Brand, Price,ProductID')
                    for r in y:
                        print(r)
            except Exception as e:
                print("Could not connect with the server.")
            c=0
            while c==0:
                b=int(input('''Enter 0 to go back'''))
                try:
                    
                    if b==0:
                        c+=1
                        option(nam,cit,cont)
                    else:
                        c=0
                except:
                    pass
            cursor.close()
            mycon.close()
                
        elif ah==4:
            import mysql.connector as mysqlcon
            try:
                mycon=mysqlcon.connect(host='127.0.0.1',user='root',passwd='root1234',database='Project')
                cursor=mycon.cursor(buffered=True)

                print()
                cursor.execute('SELECT * FROM orderstatus where Name =%s',(nam,))
                x=cursor.fetchall()
                if not x:
                    print()
                    print()
                    print("No orders placed yet")
                    print()
                    print()
                else:
                    print()
                    print('OrderID, Name, Contact, OrderStatus, PaymentStatus')
                    for r in x:
                        print(r)
            except Exception as e:
                print("Could not connet with ther server")
            c=0
            while c==0:
                try :
                    b=int(input('''Enter 0 to go back'''))
                    if b==0:
                        c+=1
                        option(nam,cit,cont)
                    else:
                        c=0
                except:
                    pass
            cursor.close()
            mycon.close()
        elif ah==5:
            cancel(nam,cit,cont)
        elif ah==6:
            home()
        else:
            print("Please enter a valid choice...")
            option(nam,cit,cont)
    except:
        print("Please enter a valid choice")
        option(nam,cit,cont)




def search(name,city,contact):
    print('''******************************************************************
1. List all Products
2. Back''')
    nam=name
    cit=city
    cont=contact
    import mysql.connector as mysqlcon
    try:
        a=(input("Enter a Choice: "))
        a=int(a)
        if a==1:
            import mysql.connector as mysqlcon
            try:
                
                mycon=mysqlcon.connect(host='127.0.0.1',user='root',passwd='root1234',database='Project')
                cursor=mycon.cursor(buffered=True)
                cursor.execute('SELECT * FROM phones')
                x=cursor.fetchall()
                if not x:
                    print()
                    print()
                    print("Sorry no products available yet")
                    print()
                    print()
                else:
                    print()
                    print('ProductID, Brand, Model, Price, Availability, ContactDealer')
                    for r in x:
                        print(r)

                cursor.close()
                mycon.close()
            except Exception as e:
                print("Connection to the server could not be made")
            c=0
            while c==0:
                try:
                    print()
                    b=int(input('Enter 0 to go back to options\n1 to go back to main menu\n2 to place order\n3 to add or read reviews\n4 to view additional info==>'))
                    if b==0:
                        c+=1
                        search(nam,cit,cont)
                    elif b==1:
                        c+=1
                        home()
                    elif b==2:
                        c+=1
                        place(nam,cit,cont)
                    elif b==3:
                        c+=1
                        review(nam,cit,cont)
                    elif b==4:
                        c+=1
                        addinfo(nam,cit,cont)
                    else:
                        print("Please enter a valid choice")
                        c=0
                except:
                    print("Please enter a valid choice")
            
        elif a==2:
            option(nam,cit,cont)
        else:
            print("Please enter a valid choice")
            search(nam,cit,cont)

    except:
        print("Please enter a valid choice")
        search(nam,cit,cont)
    
        



def place(nam,cit,contact):
    import mysql.connector as mysqlcon
    mycon=mysqlcon.connect(host='127.0.0.1',user='root',passwd='root1234',database='Project')
    cursor=mycon.cursor(buffered=True)
    name=nam
    city=cit
    cont=contact
    cursor.execute('SELECT * FROM phones')
    x=cursor.fetchall()
    cursor.execute('SELECT ProductID from phones')
    xy=cursor.fetchall()
    print()
    print('ProductID, Brand, Model, Price, Availability, ContactDealer')
    for row in x:
        print(row)
    l=0
    while l==0:

        try:
            pid=int(input('Enter product ID from above list: '))
            for k in xy:
                aj,=k
                if pid==aj:
                    l=1
                    break
            else:
                print("Incorrect product Id")
                l=0
        except Exception as e:
            print("Incorrect product id")
            l=0
        
    
    cursor.execute('SELECT Brand FROM phones WHERE ProductID=%s'%(pid,))
    X=cursor.fetchall()
    Y=str(X)
    brand=Y[3:-4]
    cursor.execute('SELECT Model FROM phones WHERE ProductID=%s'%(pid,))
    X=cursor.fetchall()
    Y=str(X)
    pr=Y[3:-4]
    cursor.execute('SELECT Price FROM phones WHERE ProductID=%s'%(pid,))
    X=cursor.fetchall()
    Y=str(X)
    price=Y[2:-3]
    
    print('Confirm details:')
    print('Name: ',name)
    print('City: ',city)
    print('Contact: ',cont)
    print('Product: ',pr)
    print('Brand: ',brand)
    print('Price: ',price)
    print()
    
    p=0
    while p==0:
        print('''1. Confirm and Place order
2. Edit order
3. Cancel this order''')
        try:
            import random
            o=random.randint(10000,99999)
            
            q=int(input('Enter choice: '))
            if q==1:
                cursor.execute("""INSERT Into orders values
               ({},'{}','{}','{}','{}','{}','{}',{})""".format(o,name,city,cont,pr,brand,price,pid))
                mycon.commit()
                cursor.execute("""INSERT INTO Orderstatus
                               VALUES({},'{}','{}','{}','{}')""".format(o,name,cont,'Placed','Paid'))
                mycon.commit()
                
                print()
                print('Your OrderID is ',o)
                print()
                c=0
                while c==0:
                    print('1. Place another order,2.Back')
                    try:
                    
                        b=int(input("Enter your choice: "))
                        if b==1:
                            c+=1
                            p+=1
                            place(name,city,cont)
                        elif b==2:
                            c+=1
                            p+=1
                            option(name,city,cont)
                        else:
                            print("Please enter a valid choice")
                            c=0
                    except:
                        print("Please enter a valid choice")
            elif q==2:
                p=1
                place(name,city,cont)
            elif q==3:
                p=1
                print('Current order cancelled!')
                option(name,city,cont)
            else:
                print("Please enter a valid choice")
        except:
            print("Please enter a valid choice")
    cursor.close()
    mycon.close()


def cancel(name,city,contact):
    import mysql.connector as mysqlcon
    mycon=mysqlcon.connect(host='127.0.0.1',user='root',passwd='root1234',database='Project')
    cursor=mycon.cursor(buffered=True)
    nam=name
    cit=city
    cont=contact
    cursor.execute('Select * from Orders where Name =%s',(nam,))
    x=cursor.fetchall()
    try:
        if not x:
            raise Exception('The table is empty')
        print('Orders placed')
        print()
        print("OrderID,Name,City,Contact,Product,Brand,Price,ProductID")
        print()
        for i in x:
            print(i)
        print('******************************************************************')
        c=0
        while c==0:
            try:
                Oid=int(input('Enter OrderID from above:'))
                cursor.execute('Select OrderID from Orders')
                y=cursor.fetchall()
                for j in y:
                    z,=j
                    if Oid==z:
                        c=1
                        break
                else:
                    print("Please enter a valid id")
                    print("If you dont want to cancel the order enter the above id and press 3 on the next query")
                    print("We are sorry for the inconvenience")
                    c=0
            except:
                print("Please enter a valid id")
                print("If you dont want to cancel the order enter the above id and press 3 on the next query")
                print("We are sorry for the inconvenience")
            cursor.execute('SELECT * FROM orders where OrderId={}'.format(Oid,))
            x=cursor.fetchall()
            print()
            print('The entered OrderID is of the given order:')
            print('OrderID, Name, City, Contact, Product, Brand, Price,ProductID')
            for row in x:
                print(row)
            print()
        p=0
        while p==0:
            try:
                print()
                print("1. Confirm cancelling this order","2, Change OrderID","3. Back",sep='\n')
                
                q=int(input('Enter your choice:'))
                if q==1:
                    cursor.execute("UPDATE orderstatus SET OrderStatus='{}' WHERE OrderID={}".format('Cancelled',Oid))
                    mycon.commit()
                    cursor.execute("UPDATE orderstatus SET PaymentStatus='{}' WHERE OrderID={}".format('Refunded',Oid))
                    mycon.commit()
                    cursor.execute("DELETE FROM Orders where OrderID={}".format(Oid,))
                    mycon.commit()
                    print('Order Cancelled successfully!')
                    p=1
                    c=0
                    while c==0:
                        try:
                            
                            print('''1. Cancel another order2. Back''')
                            b=int(input("Enter your choice: "))
                            if b==1:
                                c=1
                                cancel(nam,cit,cont)
                            elif b==2:
                                c+=1
                                option(nam,cit,cont)
                            else:
                                print("Please enter a valid choice")
                                c=0
                        except:
                            print("Please enter a valid choice")
                elif q==2:
                    p=1
                    cancel(nam,cit,cont)
                elif q==3:
                    p=1
                    option(nam,cit,cont)
                else:
                    print("Please enter a valid choice")
                    p=0
            except:
                print("Please enter a valid choice")
                
    except Exception as a:
        print(a)
        option(nam,cit,cont)
    cursor.close()    
    mycon.close()


def review(name,city,contact):
    import mysql.connector as mysqlcon
    mycon=mysqlcon.connect(host='127.0.0.1',user='root',passwd='root1234',database='Project')
    cursor=mycon.cursor(buffered=True)
    cit=city
    cont=contact
    cursor.execute('SELECT * FROM phones')
    x=cursor.fetchall()
    cursor.execute('SELECT ProductID from phones')
    xy=cursor.fetchall()
    print("******************************")
    for i in x:
        print(i)
        print()
        print()
    l=0
    while l==0:
        try:
            pid=int(input('Enter product ID from above list: '))
            for k in xy:
                z,=k
                if pid==z:
                    l=1
                    break

            else:
                print("Incorrect product Id")
                l=0
        except:
            print("Incorrect product id")
            l=0
        
    l=0
    while l==0:
        print("Enter- 1. to add review. 2. to read reviews")
        
        try:
            a=int(input("Enter choice="))
            if a==1:
                b=name
                while l==0:
                    print()
                    c=input("Enter a rating between 1-9=>")
                    try:
                        d=int(c)
                    except:
                        print("Please enter an integer digit b/w 1-9 only")
                    if len(c)!=1:
                        print("Choose between 1-9 only")
                        l=0
                    else :
                        l=1
                l=0
                while l==0:
                    d=input("Enter your review(500 words max)=>")
                    if len(d)>500:
                        print("words used greater than 500")
                    else:
                        l=1
                cursor.execute("INSERT INTO Reviews values({},'{}','{}','{}')".format(pid,b,c,d))
                mycon.commit()
                l=1
                print("Review successfully added")
                g=input("Press Enter to go back")
                search(b,cit,cont)
            elif a==2:
                l=1
                cursor.execute("SELECT * FROM Reviews where ProductID=%s",(pid,))
                h=cursor.fetchall()
                if not h:
                    print()
                    print("No reviews added")
                    print()
                    print("Try entering some other product id")
                    print()
                    b=name
                    l=1
                    search(b,cit,cont)
                else:
                    print("Product ID,Name, Rating out of 9, Review")
                    print()
                    for i in h:
                        pid,b,x,y=i
                        print(pid,b,x,y,sep='\t')
                    g=input("Press enter to go back to options")
                    l=1
                    search(b,cit,cont)
        except Exception as a:
            print("Please enter a valid choice",a)
    cursor.close()    
    mycon.close()






    
def addinfo(name,city,contact):
    import mysql.connector as mysqlcon
    mycon=mysqlcon.connect(host='127.0.0.1',user='root',passwd='root1234',database='Project')
    cursor=mycon.cursor(buffered=True)
    nam=name
    cit=city
    cont=contact
    cursor.execute('SELECT * FROM phones')
    x=cursor.fetchall()
    cursor.execute('SELECT ProductID from phones')
    xy=cursor.fetchall()
    for i in x:
        print(i)
    l=0
    while l==0:
        try:
            pid=int(input('Enter product ID from above list: '))
            for k in xy:
                z,=k
                if pid==z:
                    l=1
                    break
                    
            else:
                print("Incorrect product Id")
                l=0
        except:
            print("Incorrect product Id")

            
    cursor.execute("SELECT * FROM Additional where ProductID =%s",(pid,))
    h=cursor.fetchall()
    if not h:
        print()
        print("Additional info for this product not input yet")
        print()
    else:
        print()
        print("Product ID, Brand, Model,Instock,About")
        for i in h:
            pr,br,Mo,Ins,Ab=i
            print("Product=",pr)
            print("Brand=",br)
            print("Model=",Mo)
            print("Instock=",Ins)
            print("About=",Ab)
    inp=input("Press enter to go back")
    search(nam,cit,cont)
    mycon.close()

def login():
    import mysql.connector as mysqlcon
    mycon=mysqlcon.connect(host='127.0.0.1',user='root',passwd='root1234',database='Project')
    cursor=mycon.cursor(buffered=True)
    print("You have to login or register first.Press enter to continue-")
    a=input()
    print("************************************************************")
    print("************************************************************")
    z=0
    while z==0:
        print("Enter 1 to login to an existing id")
        print("Enter 2 to register a new id")
        print("Enter 3 to go back")
        try:
            ch=int(input("Enter your choice:"))
            if ch==1:
                z=1
                f=0
                while f<3:
            
                    name=input("USERNAME(max 13 characters):")
                    cursor.execute('SELECT UserName FROM login')
                    X=cursor.fetchall()
                    for k in X:
                        Y=str(k)
                        Username=Y[2:-3]
                        if name==Username:
                            l=1
                            f=3
                            break
                    else:
                        f+=1
                        print("Incorrect Username")
                        l=0

                if l==1:
                    g=0
                    while g<3:
                        passw=input("PASSWORD(max 18 characters):")
                        cursor.execute('SELECT Password FROM login')
                        X=cursor.fetchall()
                        for k in X:
                            Y=str(k)
                            Password=Y[2:-3]
                            if passw==Password:
                                m=1
                                g=3
                                break
                        else:
                            print("Incorrect Password")
                            m=0
                            g+=1
    
                if m==1:
                    print("Logged in successfully!")
                    cursor.execute("Select City,Contact from login where UserName = %s",(name,))
                    Y=cursor.fetchall()
                    print("This is your id information")
                    print(name)
                    for i in Y:
                        city,cont=i
                        print(city)
                        print(cont)
                    print()
                    print("Would you like to continue to next options")
                    opt=input("Enter Y if yes or enter anyother key for going back:")
                    if opt.upper()=='Y':
                        print()
                        print("Moving onto next options")
                        option(name,city,cont)
                    else:
                        print()
                        print("Going back")
                        home()
                else:
                    print("Incorrect login info provided try again")
                    login()
            elif ch==2:
                z=1
                l=0
                while l<3:
                    name=input("USERNAME(max 13 characters:")
                    if len(name)>13 or len(name)==0:
                        print("Username cant be greater than 13 characters or equal to 0 characters")
                        l+=1
                        m=0
                    else:
                        cursor.execute('SELECT UserName FROM login')
                        X=cursor.fetchall()
                        for j in X:
                            Y=str(j)
                            Username=Y[2:-3]
                            if name==Username:
                                print("Username already exists try again")
                                m=0
                                l+=1
                                break
                        else:
                            if l<3:
                                m=1
                                l=3
                            else:
                                m=0
                if m==1:
                    l=0
                    while l<3:
                        passw=input("PASSWORD(max 18 characters):")
                        if len(passw)>18 or len(passw)==0:
                            print("Password cant be greater than 18 character and equal to 0 characters")
                            l+=1
                            k=0
                        else:
                            k=1
                            l=3

                if k==1:
                    l=0
                    while l<3:
                        city=input("CITY:")
                        if len(city)>30:
                            print("City name shouldnt be greater than 40 characters")
                            l+=1
                            o=0
                        else:
                            l=3
                            o=1
                if o==1:
                    l=0
                    while l<3:
                
                        cont=input("ContactNo.:")
                        if len(cont)!=10:
                            print('Invalid Contact Number!')
                            l+=1
                            n=0
                        else:
                            try:
                                a=int(cont)
                                l=3
                                n=1
                            except:
                                print('Invalid Contact Number')
                if n==1:
                    print("This is the information you have entered==>")
                    print("USERNAME:",name)
                    print('PASSWORD:',passw)
                    print("CITY:",city)
                    print("Contact no.:",cont)
                    print()
                    print()
                    print("Is this the correct information")
                    cho=input("If yes enter Y otherwise enter any other key")
                    if cho.upper()=='Y':
                        cursor.execute("Insert into login values('{}','{}','{}','{}')".format(name,city,cont,passw))
                        mycon.commit()
                        print("Userid created and logged into.")
                        print("*************************************************")
                        ha=input("Press enter to move onto the next options-")
                        option(name,city,cont)
                    else:
                        print("Try entering the info again")
                        login()
            elif ch==3:
                z=1
                home()
            else:
                print("Please enter a valid choice")
        except:
            print("Please enter a valid choice")
            z=0


def home():
    print('''******************************************************************
1. Visit Online Mobile Shop
2. Exit''')
    try:
        #to counter type error
        ac=int(input("Enter your choice:"))
        if ac==1:
            login()
        if ac==2:
            print('Thank You! You can now close the program.')
            while True:
                break
        if ac not in [1,2]:
            print("Please enter a valid choice")
            home()
    
    except:
        print("Please Enter a valid choice")
        home()
        
if __name__== '__main__':
    home()


