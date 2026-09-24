from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int
    course: str


@dataclass
class Employee:
    name: str
    age: int
    salary: float


# Create objects
student = Student("Haritha", 23, "M.Tech")
employee = Employee("Ravi", 25, 50000)

# Display objects
print("Student:", student)
print("Employee:", employee)