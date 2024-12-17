month = int(input("Enter the month number (1-12): "))
if month in [12, 1, 2]:
    print("Season: Winter")
elif month in [3, 4, 5]:
    print("Season: Spring")
elif month in [6, 7, 8]:
    print("Season: Summer")
elif month in [9, 10, 11]:
    print("Season: Autumn")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")
