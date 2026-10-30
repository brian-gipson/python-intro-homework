# Warmup 2: Input Validation with a While Loop 

while True:
    
    try:
        number = int(input("Enter a positive integer: "))

        if number > 0:
            print(f"You entered the number: {number}")
            
            break

        print("Please enter a positive integer. Try again.")

    except ValueError:
        print("Invalid input. Please enter a positive integer.")


