from hashlib import new
from pickle import APPEND
from unicodedata import name


x = [100,110,120,130,140,150]
y = [num *5 for num in x]
print(y)

def divisible_by_three (n) :
    for num in range(1,n):
     if(num%3==0):
         print(num)
divisible_by_three(10)

nestedList = [[1,2],[3,4],[5,6]]
newlist = [i for sub_list in nestedList for i in sub_list]
print(newlist)


def smallest(list) :

    print(min(list))

smallest([2,5,6,8,9,1,6])

x = ['a','b','a','e','d','b','c','e','f','g','h']

w = list(set(x))
print(w)

def divisble_by_Seven ():
    new = []
    for m  in range(100,200):
        if (m%7==0):new.append(m)
    print(new)
divisble_by_Seven()


def greeting () :
    students = [{"age" :19,"name":"Eunice"},{"age":21,"name":"Agnes"},{"age":18 ,"name": "Teresa"}, {"age": 22, "name": "Asha"}]
    for name,age in students:
        print("Hello " + name + "and your age is" + age)
greeting()


        



        
       




