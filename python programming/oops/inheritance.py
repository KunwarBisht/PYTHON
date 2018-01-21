#inheritance

class schoolmember:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print("initalizing schoolmember {}".format(self.name))

    def tell(self):
        print('Name:"{}" Age:"{}" Gender:"{}"'.format(self.name,self.age,self.gender), end=" ")


class teacher(schoolmember):

    def __init__(self,name,age,gender,salary):
        schoolmember.__init__(self,name,age,gender)
        self.salary=salary

        print("initalizing teacher {}".format(self.name))

    def tell(self):
        schoolmember.tell(self)
        print("salary {:d}".format(self.salary))


class student():
    def __init__(self,name,age,gender,grades):
        schoolmember.__init__(self,name,age,gender)
        self.grades=grades

        print("initalizing studen {}".format(self.name))

    def tell(self):
        schoolmember.tell(self)
        print("Grades {}".format(self.grades))


t=teacher("kunwar",22,"male",8900000)
s=student("Kide",18,"female",85)

t.tell()

s.tell()






        
        


