from functools import cache
from operator import le


name = "Susan"
print(name)
# operators in pythhon
amount = 2000 + 4000
print(amount)
modulus = 10 % 3
print(modulus)
division = 20/10
print(division)
multiply = 10 *1000
print(multiply)
#String concatination
full_Name = "Nakimuli" + " Mary " + name
print(full_Name)
print('Hello World')
myname = 'Susan'
print('What is your name')
myname = input(myname)
print(myname)
#print('It is good to meet you,' + myname)
if (2>1):
    print('2 is greater than 1')
x = 'AkiraChix'
print(x)
x,y,z = 'Banana' , 'Pineapple' , 'Apple'
print(x)
print(y)
print(y)

print(10 < 5)

#Understanding lists basics in python
a = [5,10,15,20,25,30,35,40]
b = a[:3]
print(b)
#adding items in a list 
a.append(45)
print(a)
#removing items in a list
a.remove(10)
print(a)
#del keyword to remove specified item index
del a[2]
print(a)
# clearing the items in the list to be empty
a.clear()
print(a)
#deleting the entire list
#del a 
#print(a)
# trying out lists looping using a for loop
thislist = ["AkiraChix" , "codeHive" , "2022" , "year"]
for x in thislist:
    print(x)

#looping through their indices
mylist = ["Susan" , "Mary" , "Aicets" , "Francis"]
for y in range(len(mylist)):
    print(mylist[y])

def capitalize_first_last_letters(str1):
     str1 = result = str1.title()
     result =  ""
     for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]  
     
print(capitalize_first_last_letters("i love akirachix"))
print(capitalize_first_last_letters("w3resource"))
print(capitalize_first_last_letters('tessa'))
m = "milk"
j = m[:-1]
print(j)
e = m[-1]
print(e)

#Looping through a list using a while loop

names = ["Akuot","Effence","Queenter","Grace"]

i = 0

while i < len(names):
    print(names[i])
    i = i + 1 

#shorthand for looping using list comprenhension
cities = ["Kamapla" , "Capetown" , "Nairobi" , "Kigali"]
[print (x) for x in cities]
new = []
for w in cities:
    if "e" in w:
        new.append(w)
        print(new)
# short way of list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "r" in x]

print(newlist)

n = [u for u in fruits if u!= "apple"]
print(n)

numbers = [g for g in range(10) if g < 8]
print(numbers)

balance = 600

def withdraw():  # asks for withdrawal amount, withdraws amount from balance, returns the balance amount
    counter = 0
    while counter <= 2:
        while counter == 0:
            withdraw = int(input("Enter the amount you want to withdraw: AED "))
            counter = counter + 1
        while ((int(balance) - int(withdraw)) < 0):
            print("Error Amount not available in card.")
            withdraw = int(input("Please enter the amount you want to withdraw again: AED "))
            continue
        while ((float(balance) - float(withdraw)) >= 0):
            print("Amount left in your account: AED" + str(balance - withdraw))
            return (balance - withdraw)
        counter = counter + 1
        print(balance)

        withdraw()
        