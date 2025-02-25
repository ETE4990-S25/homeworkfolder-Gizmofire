import json

# @staticmethod
# def get_next_index():
#     global index 

#     index += 1
#     return index


class Person():
    
    index = 0

    def __init__(self, first, last, age, email, street_address):

        self.first_name = first
        self.last_name = last
        self.age = age
        self.email = email
        self.street_address = street_address

        self.index = Person.index
        Person.index += 1
    
# Student class that inherits from Person class



class Student(Person):
    def __init__(self, first, last, age, email, street_address, student_id):
        super().__init__(first, last, age, email, street_address)
        self.student_id = student_id


# save as json file 
# display JSON
 

# saver method used to call the class and display as JSON
def saver(obj):
    info = json.dumps(obj.__dict__)
    print(info)



# test case for sample data
def main():
    student1 = Student("John", "Doe", 21, "123@gmail.com", "1234 Main St", 123456)
    saver(student1)
    p1 = Person("Jane", "Doe", 2, "11111111@mail.com", "430 St")
    saver(p1)

main()




