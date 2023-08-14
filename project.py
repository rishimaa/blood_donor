import mysql.connector as mcon

mydb=mcon.connect(
    host="localhost",
    user="root",
    password="lead567$",
    database="blood_bank")

mycursor=mydb.cursor()
print('**************************')
print('*********WELCOME**********')
dict1={'ABC':1234,'XYZ':1111,'DEF':2222}

def authenticate():
    uname=input('ENTER USERNAME:')
    pin=int(input('ENTER PIN:'))
    if uname in dict1.keys():
        if pin==dict1[uname]:
            return 1
        else:
            return 0
    else:
        return 0
def enter_details():
    dcode=input('ENTER DONOR CODE:')
    FullName=input('ENTER FULL NAME:')
    BloodGroup=input('ENTER BLOOD GROUP:')
    Gender=input('ENTER GENDER:')
    Age=input('ENTER AGE:')
    mobile=input('ENTER MOBILE NUMBER:')
    email=input('ENTER EMAIL:')
    qry="INSERT INTO DONOR_DETAILS (dcode,FullName,BloodGroup,Gender,Age,mobile,email) values ({},'{}','{}','{}',{},{},'{}')".format(dcode,FullName,BloodGroup,Gender,Age,mobile,email)
    mycursor.execute(qry)
    mydb.commit()

def check_availability():
    BloodGroup=input('ENTER BLOOD GROUP:')
    Units=int(input('ENTER REQUIRED UNITS:'))
    qry="Select * from availability where BloodGroup = '{}'".format(BloodGroup)
    mycursor.execute(qry)
    tup=mycursor.fetchall()
    if Units <= int(tup[0][1]):
        print('Available')
        print('Contact : 044-24788132')
    else:
        print('Not Available')
    

print('******************************')
print('MENU')
print('1. ENTER DONOR DETAILS')
print('2. CHECK AVAILABILITY')
print('3. DISPLAY DONOR DETAILS')
print('4. DISPLAY AVAILABITY')
print('5. QUIT')
print('******************************')


while True:
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice==1:
        flag=authenticate()
        print('******************************')
        if flag==1:
            enter_details()
            print('******************************')
        else:
            print("WRONG USERNAME/PIN")

    elif choice==2:
        check_availability()
        print('******************************')

    elif choice==3:
        flag=authenticate()
        print('******************************')
        if flag==1:
            qry=" select * from DONOR_DETAILS "
            mycursor.execute(qry)
            tup=mycursor.fetchall()
            print("{0:<10s} {1:<15s} {2:<10s} {3:<20s} {4:<15s} {5:<20s} {6:<10s}" .format ('dcode', 'FullName', 'BloodGroup', 'Gender', 'Age','mobile','email'))
            print("______________________________________________________________________________________________________________")
            for row in tup:
                print ("{0:<10s} {1:<15s} {2:<10s} {3:<20s} {4:<15s} {5:<20s} {6:<10s} " .format (str(row[0]),str(row[1]),str( row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6])))
        else:
            print("WRONG USERNAME/PIN")
            
    elif choice==4:        
        flag=authenticate()
        print('******************************')
        if flag==1:
            qry=" select * from AVAILABILITY "
            mycursor.execute(qry)
            tup=mycursor.fetchall()
            print("{0:<10s} {1:<15s}" .format ('BloodGroup', 'Units'))
            print("______________________________________")
            for row in tup:
                print ("{0:<10s} {1:<15s}" .format (str(row[0]),str(row[1])))
        else:
            print("WRONG USERNAME/PIN")
    elif choice==5:
        exit()
        
    else:
        print('WRONG INPUT')
        


    
    
