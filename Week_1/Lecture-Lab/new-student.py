from dataclasses import dataclass

@dataclass
class Student:
    name: str        # student's full name
    school_id: str    # unique school ID
    gpa: float         # current GPA


def main():
    # create some example Student objects
    alex = Student('Alex', 'abcdef', 3.8)
    sam = Student('Sam', 'qwerty', 3.2)

    print(alex)
    print(sam)


main()