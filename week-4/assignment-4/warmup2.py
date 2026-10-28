# Warmup 2: Dictionary Operations

student = {
    "name": "Brian",
    "grade": 10,
    "subjects": ["Math", "Science", "History"]
}

for key, value in student.items():
    print(f"{key}: {value}")

student["graduated"] = False

print("Updated dictionary:",student)