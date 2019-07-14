#  ex-2.2
width = 17
height = 12.0
delimiter = '.'

x = width/2
y = width/2.0
z = height/3
v = 1+2*5
delim = delimiter*5
print(x , type(x) )
print(y, type(y))
print(z, type(z))
print(v, type(v))
print(delim, type(delim))

#  ex-2.3
#   1
import math
r=5
v = 4/3*math.pi*math.pow(r,5)
print(v)
#2
book = 24.95
book = (book * 40) / 100
print("price of a book ", book)
firstcopy = book + 3
print("price of a first book ", firstcopy)
eachaddcopy = book + 0.75
eachaddcopy = eachaddcopy * 59
print("wholesale cost ", eachaddcopy + firstcopy)

#3
# import datetime
# leave = datetime.time(6,52)
# print (leave.time())
# firstmile = leave + datetime.timedelta(minutes = 8.25)
# threemiles = datetime(firstmile + datetime.time(0,7,12) * 3)
# lastmile = datetime.combine(threemiles + datetime.time(0,8,15))
# print (lastmile)


#2
name = input("enter name: ")
age = int(input("enter age: "))
year = str((2019 - age)+100)
print (name + " will be 100 years old in " + year) 

#3 
asknum = int(input("enter number: "))
if asknum % 2 == 0:
    print ("your num is even")
else: 
    print ("your num is odd")

#4
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for lessf in a:
    if lessf < 5:
        print(lessf)
    else:
        continue         