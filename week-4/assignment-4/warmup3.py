# Warmup 3: Set Operations

languages1 = ["Python", "Java", "JavaScript", "C++"]
languages2 = ["Python", "C", "C#", "C++"]

set1 = set(languages1)
set2 = set(languages2)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)