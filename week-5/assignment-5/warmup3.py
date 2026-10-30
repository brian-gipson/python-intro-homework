# Warmup 3: Linear Search

names = ["Alice", "Bob", "Charlie", "David"]
search_name = input("Enter a name to search for: ")

found = False
for i in range(len(names)):
    
    if names[i] == search_name:
        print(f'found "{search_name}" at index {i}.')
        found = True

        break

if not found:
    print(f'Name "{search_name}" was not found in this list.')