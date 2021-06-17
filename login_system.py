import csv,random,string,sys

#generate random password
def randompass():
    while True:
        spc_charac="!@#$%&?<>"
        print("--------------------Automatic Password Generator--------------------")
        N=eval(input("Enter the length of the password you want. Minimum length must be 5: "))
        if N>=5:
            password=''.join(random.choices(string.ascii_letters+string.digits+spc_charac, k=N))
            print("Please note down the generated password:\n",password)
            return password
        else:
            print("Invalid")

#write new user name and password   
def write_csv(use,password):
    with open('C:\\Users\\Admin\\Downloads\\project\\login_details.csv','a', newline='') as filew1:
        fieldnames=['Username', 'Password']
        writer1=csv.DictWriter(filew1,fieldnames=fieldnames)
        writer1.writerow({'Username': use, 'Password': password})

#check for if user is registered
def check(usertmp):
    x=""
    with open('C:\\Users\\Admin\\Downloads\\project\\login_details.csv','r', newline='') as filer1:
        reader1=csv.DictReader(filer1)
        for lines in reader1:
            if lines['Username']!=usertmp:
                x="NO"
            else:
                x="YES"
                break
        return x
                

  

 #check if password and username is correct       
def checkuserpass(username,password):
    with open('C:\\Users\\Admin\\Downloads\\project\\login_details.csv','r', newline='') as filer2:
        reader2=csv.DictReader(filer2)
        for lines in reader2:
            if (lines['Username'] == username) and (lines['Password']==password):
                return True
            else:
                pass

#register new user 
def register():
    condition=""
    print("----------------Register------------------")
    while True:
        user=input("Enter Username: ")
        condition=check(user)
        if condition=="NO":
            while True:
                print("Do you want to use random password genrator module to generate password?")
                dec=input("Press 'Y' if u want to use or 'N': ")
                if dec.lower()=="y":
                    passw1=randompass()
                    break
                elif dec.lower()=="n":
                    while True:
                        passw0=input("Enter Password: ")
                        passw1=input("Confirm Your Password: ")
                        if len(passw1)>=5:
                            if passw0==passw1:
                                break
                            else:
                                print("Passwords Don't Match")
                        else:
                            print("Password too short!")
                            continue
                    break
            write_csv(user,passw1)
            print("Successfully Registered")
            break
        else:
            print("Username Exists!")
            pass
        main()
    login()    
   

#login registered user
def login():
    print("----------------Login------------------")
    condition=False
    while True:
        user=input("Enter Username: ")
        passw=input("Enter Password: ")
        condition=checkuserpass(user,passw)
        if condition== True:
            print("Successfully Logged In.")
            sys.exit()
        else:
            print('Wrong Username or Password. Please Check.')
    
    




#check if the file exists
def trying():
    try:
        with open('C:\\Users\\Admin\\Downloads\\project\\login_details.csv','r', newline='') as filer3:
            reader3=csv.DictReader(filer3)
    except FileNotFoundError:
        with open('C:\\Users\\Admin\\Downloads\\project\\login_details.csv','w', newline='') as filew3:
            fieldnames=['Username', 'Password']
            writer3=csv.DictWriter(filew3,fieldnames=fieldnames)
            writer3.writeheader()
            writer3.writerow({'Username':'ADMIN', 'Password':'ADMIN'})
            
#main
def main():
    while True:
        print("Do You want to login or Register?")
        choice=input("Type 1 for Login and 2 for Registering as a new user: \n>")
        trying()
        if choice=="1":
            login()
            break
        elif choice == "2":
            register()
            break

if __name__=="__main__":
    main()
    
