color = input("Enter the color (Red, Yellow, Green): ").capitalize()
if color == "Red":
    print("Action: Stop")
elif color == "Yellow":
    print("Action: Get Ready")
elif color == "Green":
    print("Action: Go")
else:
    print("Invalid color! Please enter Red, Yellow, or Green.")
