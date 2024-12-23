class Student:

    def __init__(self, first_name, last_name, national_number, student_number, GPA , age ):
        
        self.first_name = first_name 

        self.last_name = last_name

        self.age = age 

        self.national_number = national_number

        self.student_number =  student_number

        self.GPA = GPA
    
      
    def get_age(self):
        return ("The "+self.first_name + 's age is ' + str(self.age))
    
    def get_firsr_name(self):
        return ("The first name: "+ self.first_name)


student_1 = Student('Mohammad ', 'Maleki' ,  '4670360647' , '02121040709018' , 14 , 21)

student_2 = Student('Mehdi ', 'Zamani' ,  '2251973654' , '02121040709016' ,19 , 21)

student_3 = Student('Amir ', 'Kheyri' ,  '0481128328' ,'02120040709014' , 12 , 22)


print(student_3.get_firsr_name())
print(student_3.get_age())

