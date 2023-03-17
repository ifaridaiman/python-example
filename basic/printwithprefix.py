# Create the 3 array object
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
        "age": 22,
        "grade": "C"
    }
]

# Read the values based on name
print("this is a without any prefix string with variable for Student Name  {students[0]['name']} {students[0]['age']}")

print(f"this is a formatted string with variable for Student Name {students[0]['name']} {students[0]['age']}")

print(r"this is a raw string with variable for Student Name {students[0]['name']} {students[0]['age']}")
