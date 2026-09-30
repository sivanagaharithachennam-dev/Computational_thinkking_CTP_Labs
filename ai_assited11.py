vdef calculate_grade(
    name: str,
    mark1: float,
    mark2: float,
    mark3: float
) -> str:

    marks = [mark1, mark2, mark3]

    if any(mark < 0 or mark > 100 for mark in marks):
        return "Invalid marks"

    average = sum(marks) / 3

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    return f"{name}: Grade {grade}"


print(calculate_grade("Yaswanthi", 90, 85, 95))