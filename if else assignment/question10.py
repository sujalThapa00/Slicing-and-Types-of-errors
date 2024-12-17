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
