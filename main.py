
# Student Grade Management System

# Get student details
name = input("Enter Student Name: ")
department = input("Enter Department: ")
semester = input("Enter Semester: ")

# Get subject marks
print("Enter marks for three subjects")

mark1 = float(input("Enter Subject 1 marks: "))
mark2 = float(input("Enter Subject 2 marks: "))
mark3 = float(input("Enter Subject 3 marks: "))

# Validate marks
if not all(0 <= mark <= 100 for mark in [mark1, mark2, mark3]):
    print("Invalid marks! Enter marks between 0 and 100.")

else:
    # Calculate average
    average = (mark1 + mark2 + mark3) / 3

    # Assign grade
    if average >= 90:
        grade = "S"
    elif average >= 80:
        grade = "A"
    elif average >= 65:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    # Display result
    print("\n----- STUDENT DETAILS -----")
    print("Name:", name)
    print("Department:", department)
    print("Semester:", semester)
    print("Average:", round(average, 2))
    print("Grade:", grade)
