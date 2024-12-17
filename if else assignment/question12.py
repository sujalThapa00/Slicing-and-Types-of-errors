char = input("Enter a character: ")
if len(char) == 1:
    if char.isupper():
        print(f"{char} is an uppercase letter.")
    elif char.islower():
        print(f"{char} is a lowercase letter.")
    elif char.isdigit():
        print(f"{char} is a digit.")
    else:
        print(f"{char} is neither an uppercase letter, a lowercase letter, nor a digit.")
else:
    print("Invalid input! Please enter a single character.")