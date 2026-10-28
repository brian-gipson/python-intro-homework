# Part 2: Mini-Project — Day Planner

day = input("What day is it? ").strip().lower()
time = input("What time of day? ").strip().lower()

days = [
    "monday", "tuesday", "wednesday", "thursday",
    "friday", "saturday", "sunday"
]

times = [
    "morning", "afternoon", "evening"
]

if day not in days:
    print("Sorry, I don't recognize that day. Try Monday through Sunday.")
elif time not in times:
    print("Sorry, please enter morning, afternoon, or evening.")
elif day == "monday":
    if time == "morning":
        print("Suggestion: Its time to go to work")
    elif time == "afternoon":
        print("Suggestion: Make sure to eat lunch.")
    else:
        print("Suggestion: Get ready for Monday Noght foorball!")
elif day == "saturday":
    if time == "morning":
        print("Suggestion: Get ready for college football!")
    elif time == "afternoon":
        print("Suggestion: Get ready for college football!")
    else:
        print("Suggestion: Enjoy a movie night.")
elif day == "sunday":
    if time == "morning":
        print("Suggestion: Knock out chores before NFL kickoff!")
    elif time == "afternoon":
        print("Suggestion: Get ready for kickoff.")
    elif time == "evening":
        print("Suggestion: Football is over, go to sleep, you have to work tomorrow!")
else:
    print("Suggestion: Make time for a hobby you enjoy!")