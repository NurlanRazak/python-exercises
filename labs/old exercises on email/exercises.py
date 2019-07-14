#Nurlan Razak
#4

x = int(input("enter some number: "))
ran = list(range (1, x+1))
s = []
for elem in ran:
    if x % elem == 0:
        s.append(elem)

print (s)

#5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

elem = []
for i in a and b:
    if i in a and b:
        elem.append(i)

print(elem)

#6

somstr = input("enter word: ")
somstr = str(somstr)
rvrs = somstr[::-1]
if somstr==rvrs:
    print("this word is palindrome: ", somstr)
else:
    print("it's not palindrome!")

#7

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for i in a:
    if i%2 == 0:
        print(i)
    else:
        print("its not")

a = [i for i in a if i%2==0]
print(a)

#8

player1 = input("Player1 enter rock or paper or scissors as r, p, s: ")
player2 = input("Player2 enter rock or paper or scissors as r, p, s: ")
def rps(p1, p2):
    if player1=='s' and player2=='r':
        return("Player2 is winner")
    elif player1=='r' and player2=='s':
        return("Player1 is winner")
    elif player1=='s' and player2=='p':
        return("Player1 is winner")
    elif player1=='p' and player2=='s':
        return("Player2 is winner")
    elif player1=='p' and player2=='r':
        return("Player1 is winner")
    elif player1=='r' and player2=='p':
        return("Player2 is winner")

print(rps(player1, player2))
while True:
    cont = input("do u want to continue? [y/n] ")
    if cont == 'y':
        player1 = input("Player1 enter rock or paper or scissors as r, p, s: ")
        player2 = input("Player2 enter rock or paper or scissors as r, p, s: ")
        print(rps(player1, player2))
    else:
        break


#9

import random
a = random.randint(1,9)
userask = int(input("guess the number: "))
def guessnum(num1, num2):
    if userask == a:
        return("exactly right!")
    elif userask < a:
            return("too low")
    elif userask > a:
            return("to high")    

print(guessnum(a, userask))
while True:
    cont = input("do you want to continue? [y/n] ")
    if cont == 'y':
        a = random.randint(1,9)
        userask = int(input("guess the number: "))
        print(guessnum(a, userask))
    else:
        break    

#10
import random
a = random.sample(range(60),10)
print(a)
b = random.sample(range(100),15)
print(b)
commonnums = [x for x in a and b if x in a and b]
print(commonnums)

#11
def get_num():
   return int(input("enter number: "))

somenum = get_num()
s = [elem for elem in range(2, somenum) if somenum % elem == 0]

def is_prime(n):
	if somenum > 1:
		if len(s) == 0:
			print('prime')
		else:
			print('NOT prime')
	else:
		print('NOT prime')
	
is_prime(somenum)

#12 
a = [5, 10, 15, 99, 20, 25]
print(len(a))
print(a[len(a)-1])
def nlist(s):
    return [s[0], s[len(s)-1]]

print(nlist(a))

#13
# def fibon():
#     numask = int(input("how many Fibonnaci numbers to generate: "))
#     f = 0
#     second = 1
#     for i in range(0, numask):
#         if i <= 1:
#             next = i 
#         else:
#             next = f + second
#             f = second
#             second = next
#         # print(next)
#         return next        
# print(fibon())