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

        # fancy indexing way other passing it as a value to te constructor
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
def saver(obj, name):
    

    with open(name, mode="w", encoding="utf-8") as write_file:
        json.dump(json.loads(json.dumps(obj)), write_file, indent=4)

    print("json: \n", json.dumps(obj, indent=4))
    print("json wrote to file")
        
    

    

# test case for sample data
def main():
    student1 = Student("John", "Doe", 21, "123@gmail.com", "1234 Main St", 123456)
    
    p1 = Person("Jane", "Doe", 2, "11111111@mail.com", "430 St")
    
    combined_data = [
        student1.__dict__,
        p1.__dict__
    ]
    combined_json = json.dumps(combined_data )
    saver(combined_json, "data.json")


    # save 


# main()




