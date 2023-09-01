#args in pyothn
'''
def funargs (*args):
    for item in args:
    
        print (item)


har = ["vipul","yadav" ,"tejashwi" ,"aashu","rjd"]
funargs (*har)
'''

#time moduele in python
'''

import time
intial = time.time()


k= 0
while (k<5):
    print (" Hello i am vipul yadav")
    k+1
    print (" while loop run in ", time .time ()- intial)

intial2 = time.time()
for i in range (6):
    print (" Hello i am vipul yadav")
    print ("for loop run in ", time.time()- intial2 , "seconds")

localtime = time.asctime(time.localtime(time.time))
print(localtime)

'''

 #self __ init__  in python 

'''
class employee:
    no_of_leaves = 8

    def printdetails(self):
        return f" the name is {self.name}.salary is {self.salary} and role is {self.role}"


yadav = employee ()
tejashwi = employee ()

yadav.name = "yadav"
yadav.salary =456
yadav.role = "poltician"


tejashwi.name = "yadav"
tejashwi.salary =786574
tejashwi.role = "big fan of tejashwi yadav"

print (tejashwi.printdetails())

# print (yadav.printdetails())


'''

#single inheritance in python

'''


class employee:
    no_of_leaves = 8 

    def __init__ (self , aname , asalary , arole ):
        self.name = aname 
        self.salary = asalary
        self.role = arole

    def printdetails (self):
        return f"The name is {self.name} . salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("_"))
    
    @staticmethod
    def printgood (string):
        print ("This is good"  + string )

    
class progarmmer(employee):
        def __init__ (self , aname , asalary , arole , alanguage ):
            self.name = aname 
            self.salary = asalary
            self.role = arole    
            self.language = language

        def printprog (self):
            return f"The name is {self.name} . salary is {self.salary} and role is {self.role} . The language are {self.language}"

    
tejashwi = employee("tejashwi", 6889, "poltican")
yadav = employee ("yadav" ,3456,"big fan of tejashwi yadav" )

vipul = programmer ("vipul", 6587,"programmar" ,["python"])
tej  = programmer ("tej", 6587,"programmar" ,["python , cpp" ,])





print(vipul.printprog())


'''

#multipal inheritance in python
 
'''
class employee:
    no_of_leaves = 8 

    def __init__ (self , aname , asalary , arole ):
        self.name = aname 
        self.salary = asalary
        self.role = arole

    def printdetails (self):
        return f"The name is {self.name} . salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("_"))
    
    @staticmethod
    def printgood (string):
        print ("This is good"  + string )


class playar:
    no_of_games = 5
    def  __init__(self,name,game):
        self.name = name 
        self.game = game 

    def printdeatial (self):
        return f"The name is {self.name} . game is {self.game} "
    
class RjdFan ( employee, playar):
    langauge = "c++","java"
    def printlanguage(self):
        print(self.langauge)



    
tejashwi = employee("tejashwi", 6889, "poltican")
yadav = employee ("yadav" ,3456,"big fan of tejashwi yadav" )

vipul = playar ("vipul",["football"])
tej = RjdFan ("tej",6477, "RjdFan")

det = tej.printdetails()
tej.printlanguage()
print(det)


'''

    

    #multilevel inheritance in python

class Dad:
    footboll = 6

class son (Dad):
    dance = 1
    def isdance(self):
      return f"yes i dance {self.dance} no of dance"

class grandson(son):
    dance = 8 
    def isdance (self):
      return f"dance like parabhu deva!"\
           f"yes i dance very nice {self.dance} no of times"
vipul = Dad()
aashu = son()
yadav = grandson()

print (vipul.footboll())
