#2
str = 'Hello World!'
print(str * 2)

#3
# conint = int(str,2)

#4
username = input("enter your name: ")
userbirth = int(input("enter your age: "))
childname = input("enter your child name: ")
childbirth = int(input("enter your child age: "))
yearhund = (2019 - childbirth) + 100
print("the year your child", childname ," will turn 100 is: ", yearhund)

# 5
def threeask():
    firstkask = int(input("enter first number: "))
    secondkask = int(input("enter second number: "))
    thirdkask = int(input("enter third number: "))
    if firstkask > secondkask and firstkask > thirdkask:
        print("first number is largest of three entered numbers!")
    elif secondkask > firstkask and secondkask > thirdkask:
        print("second number is largest of three entered numbers!")
    elif thirdkask > firstkask and secondkask < thirdkask:
        print("thrid number is largest of three entered numbers!")
    else:
        print("something gone wrong!")    

threeask()

#6
cov_price = 24.95
dics = (cov_price * 40) / 100
discprice = cov_price - dics
firstcopy = discprice + 3
eachadd = discprice + 0.75
print(firstcopy + eachadd * 59)

#7
s = 10
t = (43 * 60) + 30
miles = s / 1.61
timepermile = t / miles #seconds in miles
print("seconds in miles: ", timepermile)
timepermile = timepermile / 60 #minutes
print("minutes time per mile: ", timepermile)
avspeed = 60 / timepermile #miles per hour
print("average speed: ", avspeed)


#8
mystring = "testing"
print(float(mystring))

#9
a = [1,2,3,4,5,7,8,9,15,20,25,300]
firstval = a[:1]
lastval = a[-1:]
midval = a[3:10]
print(firstval)
print(lastval)
print(midval)

#10
studlist = {
    "Zhantore":123,
    "Alen": 456,
    "Diana": 789,
    "Kamilla": 321,
    "Adil": 654,
    "Akzhan": 987
    }
print(studlist)

print("Alen's ID: ",studlist.get("Alen"))
for name, id in studlist.items():
    if id == 123:
        print("id 123 student name: ", name)
        break


print("printing all keys: ")
for student in studlist:
    print(student)

print("checking is there Alua: ")
for i in studlist:    
    if "Alua" in studlist:
        print("Alia is there")
        break
    else:
        print("Alua not found")    
        break