n = int(input("Enter an integer: "))
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 5 == 0:
    print("Buzz")
elif n % 3 == 0:
    print("Fizz")
else:
    print(n)



char = input("Enter a character: ").lower()
if len(char) == 1 and char.isalpha():
    if char in 'aeiou':
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Invalid input! Please enter a single alphabet character.")
    
    

marks = int(input("Enter your marks: "))

if 90 <= marks <= 100:
    print("Grade: A")
elif 80 <= marks <= 89:
    print("Grade: B")
elif 70 <= marks <= 79:
    print("Grade: C")
elif marks < 70:
    print("Grade: Fail")
else:
    print("Invalid input! Marks should be between 0 and 100.")
