# Create the 13 array object
students = [
    {
        "name": "Alice",
        "age": 20,
        "grade": "A"
    },
    {
        "name": "Bob",
        "age": 21,
        "grade": "B"
    },
    {
        "name": "Charlie",
        "age": 30,
        "grade": "C"
    },
    {
        "name": "David",
        "age": 23,
        "grade": "A"
    },
    {
        "name": "Emily",
        "age": 20,
        "grade": "B"
    },
    {
        "name": "Frank",
        "age": 21,
        "grade": "A"
    },
    {
        "name": "Grace",
        "age": 22,
        "grade": "B"
    },
    {
        "name": "Henry",
        "age": 30,
        "grade": "C"
    },
    {
        "name": "Isabelle",
        "age": 16,
        "grade": "A"
    },
    {
        "name": "Jack",
        "age": 21,
        "grade": "D"
    },
    {
        "name": "Katie",
        "age": 20,
        "grade": "D"
    },
    {
        "name": "Liam",
        "age": 22,
        "grade": "C"
    },
    {
        "name": "Mia",
        "age": 23,
        "grade": "A"
    }
]

#Variable
below_18 = 0
above_18_below_25 = 0
above_25 = 0
student_pass = 0
student_failed = 0

#function to check grade
def check_grade(grade, pass_count, failed_count):
    if grade == "A":
    pass_count +=1
        return "Pass",pass_count,failed_count
    elif grade == "B":
        pass_count +=1
        return "Pass",pass_count,failed_count
    elif grade == "C":
        pass_count +=1
        return "Pass",pass_count,failed_count
    else:
        failed_count +=1
        return "Failed",pass_count,failed_count
        
#loop with nested if else combine with function
for student in students:
    if student['age'] < 18:
        result, student_pass, student_failed = check_grade(student['grade'], student_pass, student_failed)
        print(f"{student['name']} is below 18 and {result}")
        below_18 += 1
    elif student['age'] >= 18 and student['age'] <= 25:
        result, student_pass, student_failed = check_grade(student['grade'], student_pass, student_failed)
        print(f"{student['name']} is below 25 and above 18 and {result}")
        above_18_below_25 +=1
    else:
        result, student_pass, student_failed = check_grade(student['grade'], student_pass, student_failed)
        print(f"{student['name']} is above 25 and {result}")
        above_25 += 1


#printing results.
print(f"..................................................")
print(f"Student below 18 : {below_18}" )
print(f"Student above 18 but below 25 : {above_18_below_25}" )
print(f"Student above 25 : {above_25}" )
print(f"..................................................")
print(f"Student passed: {student_pass}")
print(f"Student failed: {student_failed}")


