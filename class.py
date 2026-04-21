class Student:
    
    def __init__(self, name, age, mobile):
        self.name = name
        self.age = age
        self.mobile = mobile

    def studentinfo(self):
        return f"{self.name}, {self.age}, {self.mobile}"


s1 = Student("Jyoti", 22, "9876543210")
s2=Student("shivam",27,"8275712800" )
print(s1.studentinfo())
print(s1.studentinfo())
