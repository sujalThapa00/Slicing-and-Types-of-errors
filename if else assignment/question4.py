marks = int(input("Enter your marks: "))

if marks < 25:
    print("Your grade is: F")
elif 25 <= marks < 45:
    print("Your grade is: E")
elif 45 <= marks < 50:
    print("Your grade is: D")
elif 50 <= marks < 60:
    print("Your grade is: C")
elif 60 <= marks < 80:
    print("Your grade is: B")
elif marks >= 80:
    print("Your grade is: A")
else:
    print("Invalid input. Please enter a valid mark.")
