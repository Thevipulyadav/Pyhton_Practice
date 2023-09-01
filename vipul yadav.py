# var1 = 6
# var2 = 56
# var3 = int(input(" enter number"))

# if var3>var2:
#     print ("grater")
# else:
#     print("lesser")    


# sub1 =int(input ("enter your sub1 marks"))

# sub2= int(input ("enter your sub1 marks"))

# sub3 =int(input ("enter your sub1 marks"))

# print("total marks of five subjects is ", sub1+sub2+sub3)


# () -> tuple
# [] -> list
# {} -> dict
# {key: value} -> set




# d={'vipul': '23.4.4000',
# 'yadav': '45.5.6000',
# 'aashu':'33.3.70000',
# 'sunil': "PAPA"
# }
# name = input("enter the name:")
# print (d[name])


'''
# loop progarmm
list1 = ["vipul", 33, "siwan"] ,["yadav", 45, "patna"] ,["tejashwi",64, "patna"],["aashu" ,754, "tejash"]
for item ,seat, vidhan  in list1:
   print (item)
   print(seat)
   print(vidhan) 
   print("")
'''

#loop progarmm 

'''
items = [int, float, "VIPUL" ,4,5,5,6,7,8999,44,33,22,44,555]
for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)
'''

#while loops
'''
i = 0

while(i<=100):
    print (i)
    i = i+ 1

'''
#break $ continue statement 

'''
i = 0

while(True):
    if i+1< 5:
        i = i+ 1
        continue
    print (i + 1 , end = "  " )
    if ( i == 44):
        i = i+ 1
        break              #  iska mtlab loop ko rokna hota hai

    i = i+ 1
'''

#break $ continue statement  user se input le kar 
'''
while(True):
    inp = int (input("enter a number "))
    if inp>100:
        print(" mubarak ho ye number 100 se bada hai\n")
        break
    else:
        print (" phir se try karo ye number 100 se chota hai\n")
        continue
'''
#operator in python

#arithmetic operator
#asssimentic operator
#comparison operator
#logical operator
#identity oprertor
#bitwise opertor

'''

print ("5+ 6 is " ,5+6)
print ("5- 4 is ", 5-4)
print ("3* 5 is" , 3*5)
print ("5/6 is ",5/6)
print ("15//6 is ", 15//6)
'''
#short hand if else notation

'''
a = int (input (" enter a number a \n"))
b = int (input ("enter a number b \n"))
if a>b: 
    print ("a b se bada hai ")
else:
    print("B a se bada hai")
'''

#function and docstrings

#a = 4
#b = 5 
#c = sum ((a , b))
#print (c)

'''
def function1 ( a , b) :
    average = (a+b)/2
    print (average)
    print (" aapka function 1 me swagat hai" , a+b)
(function1 ( 6 ,7))
'''

#try except exception handling 

'''
print  ("enter a number 1")
num1 = input ()
print ("enter a number 2 ")
num2 = input ()
try :
    print ("the sum of two number is  " , int ((num1)+ int (num2)))

except Exception as e:
    print (e)

    print ("ye line bahut jaruri hai isko print karo ")
    
    '''

# open read write file in python

# f = open ("self.py" , "rt")
# content = f. read()
# print (content)
# f. close()

