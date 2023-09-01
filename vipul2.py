class Employee:
    def __init__(self,fname , lname ):
        self.fname = fname
        self.lname = lname 

    def explanin (self):
        return f"This employee is {self.fname}{self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname ==None:
            return "Email is not set plese set it using setter"
        return f"{self.fname}{self.lname} @bigfanoftejashwi.com"
    
    @email.setter
    def email(self ,string):
        print ("setting now...")
        names = string.split("@")[0]
        self.lname = name.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None
        
Rjd_supporter = Employee("vipul","supporter")
vipul = Employee ("yadav","sunil")

print(Rjd_supporter.email)

skilf = Employee("skill","f")
print(skilf.email)

print(type(skilf))
