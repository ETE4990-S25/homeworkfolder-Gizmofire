import json




class Person():
    """Create a simple model of a person"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_older(self):
        """Age the Person"""
        print(self.name.title() + ', It has been a good year')
        self.age += 1


    def saver(self):
        with open(self.name + ".json", mode="w", encoding="utf-8") as write_file:
            json.dump(json.loads(json.dumps(self.__dict__)), write_file, indent=4)

        print("json: \n", json.dumps(self.__dict__, indent=4))
        print("json wrote to file")

    def toString(self):
        print("print: \n", json.dumps(self.__dict__, indent=4))




def saver(obj, name):
    with open(name + ".json", mode="w", encoding="utf-8") as write_file:
        json.dump(json.loads(json.dumps(obj)), write_file, indent=4)

    print("json: \n", json.dumps(obj, indent=4))
    print("json wrote to file")




class Adult(Person):
    """Create a simple model of a student"""
    def __init__(self, name, age, profession):
        """Initialize name, age, and gpa attributes."""
        self.name = name
        self.age = age
        self.profession = profession

    def change_profession(self, prof):
        self.profession = prof





# stolen from mr powers example but expanded upon while not trying to look at the old cold 
class Kid(Person):
    """Create a simple model of a student"""
    def __init__(self, name, age, gpa, school):
        """Initialize name, age, and gpa attributes."""
        self.name = name
        self.age = age
        self.gpa = gpa
        self.school = school
    
    def study(self):
        """Increase GPA due to studying"""
        print(self.name.title() +  ' has now studyed')
        self.gpa += 0.1
    
    




        
    

    

# test case for sample data
def main():
    # student1 = Student("John", "Doe", 21, "123@gmail.com", "1234 Main St", 123456)
    
    p1 = Person("Jane", 18)
    p2 = Adult("Bass" , 12, "Chef")
    p3 = Kid("Joe", 10, 3.0, "cpp highschool")

    p1.saver()
    p2.saver()
    p3.saver()

    p1.get_older()
    p1.toString

    p2.get_older()
    p2.change_profession("Janitor")
    p2.toString

    p3.get_older()
    p3.study()
    p3.toString()


    p1.saver()
    p2.saver()
    p3.saver()

    combined_data = [
        p1.__dict__,
        p2.__dict__,
        p3.__dict__

    ]
    combined_json = json.dumps(combined_data )
    saver(combined_data, "all data")

    


    # save 


main()




