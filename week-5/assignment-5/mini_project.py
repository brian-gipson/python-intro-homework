# Part 2: Mini-Project — Number Cruncher

numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print("Number Cruncher")
    print("1. Find the minimum number")
    print("2. Find the maximum number")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    choice = input("Choose an option (1-5): ").strip()

    # Option 1: Find the minimum number
    if choice == "1":
        smallest = numbers[0]
        for number in numbers:
            if number < smallest:
                smallest = number

        print(f"The minimum number is {smallest}.")

    # Option 2: Find the maximum number
    elif choice == "2":
        largest = numbers[0]
        for number in numbers:
            if number > largest:
                largest = number

        print(f"The maximum number is {largest}.")

    # Option 3: Search for a number
    elif choice == "3":
        try:
            target = int(input("Enter the number to search for: "))

            found = False

            for index in range(len(numbers)):
                if numbers[index] == target:
                    print(f"Found {target} at index {index}.")
                    found = True

                    break

            if not found:
                print(f"{target} was not in the list.")

        except ValueError:
            print("Please enter a whole number.")

    # Option 4: Sort the list    
    elif choice == "4":
        swapped = True

        while swapped:
            swapped = False

            for index in range(len(numbers) - 1):
                if numbers[index] > numbers[index + 1]:
                    numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
                    
                    swapped = True

        print("The list has been sorted.")

    # Option 5: Quit
    elif choice == "5":
        print("Goodbye!")
        
        break

    else:
        print("Invalid choice. Please try again.")