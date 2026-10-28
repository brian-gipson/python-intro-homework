# Part 2: Mini-Project — Student Roster Analyzer

students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

top_name = students[0]["name"]
highest_score = students[0]["score"]
total_score = 0
subjects = set()
high_scores = []

for student in students:
    if student["score"] > highest_score:
        highest_score = student["score"]
        top_name = student["name"]

    total_score += student["score"]
    
    subjects.add(student["subject"])

    if student["score"] > 75:
        high_scores.append(student["name"])

average = total_score / len(students)

print(f"Top scorer:       {top_name} ({highest_score})")
print(f"Class average:    {average:.2f}")
print(f"Subjects offered: {subjects}")
print(f"High scorers:     {high_scores}")

#learning GITHUB
