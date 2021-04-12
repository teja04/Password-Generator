import random
import string
import crypt
#random module use for selecting letters randomly form a list
#string module use to declare alphabets, digits, symbols
#crypt module use to encrypt any word using salt

def password_genarator():
    password_size = int(input("Enter the length of password :")
    if password_size >= 8:
        combine = string.ascii_letters + string.digits + string.punctuation
        #ascii_letters gives lower case and upper case alphabets
        #if you want only lower case you can code ascii_lowercase similary ascii_uppercase for upper case alphabets
        #string.digits gives numbers from 0 to 9
        #string.punctuation gives all the symbols

        password = " " #password name define

        for i in range(password_size):
            password = password + random.choice(combine) #random.choice will select randomly from combination of all

        print(password)
    elif password_size < 8:
        print("Password length should be greater than 8")
        return password_genarator() #return command used for recursive function
    else:
        print("Password size is small\nEnter again")
        return password_genarator() #return command used for recursive function


print("Choose your choice: \n1)Want to generate password \n2)Want to encrypt your password")
select = int(input()) 

if select == 1:
    password_genarator()
else:
    password = input("Enter your password :")
    encrypt = crypt.crypt(password,"AZ")
    #Here the encryption is done by adding salt "AZ" to given password

    print("Your encrypted password : {}".format(encrypt))
