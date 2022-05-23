# importing packages in my script inorder to access the python library
import random
import string

print ('Hello welcome to password generator!!!')

# ask for the length of the password from the user 
length = int(input('\n Enter the length of the password: '))

# using the string module  to define data.
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# combine the data we have stored above into all
all = lower + upper + num + symbols

# making use of the random module to generate the password
temp = random.sample(all,length)
password = "".join(temp)

print(password)


# import random
# characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@€$#%({)}],/<\.>[*^&"

# while 1:
#     length = int(input("What length would you like your password to be ? :"))
#     count = int(input("How many passwords would you like ? "))
#     for x in range(0, count):
#         password = ""
#         for x in range(0, password_len):
#             password_characters = random.choice(characters)
#             password      = password + password_characters
#         print("Here is your password : ",password)
