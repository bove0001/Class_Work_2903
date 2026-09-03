class Student:
    def __init__(self, name, school_id, gpa):
        self.name = name            # student's full name
        self.school_id = school_id  # unique school ID
        self.gpa = gpa              # current GPA

    def __str__(self):
        # returns a readable summary of the student
        return f'Student name: {self.name}, ID: {self.school_id}, current GPA: {self.gpa}'

alex = Student('Alex', 'abcdef', 3.8)  # create a Student object for Alex
print(alex.name)
print(alex.school_id)
print(alex)  # calls __str__ automatically

sam = Student('Sam', 'qwerty', 3.2)  # create a Student object for Sam
print(sam)