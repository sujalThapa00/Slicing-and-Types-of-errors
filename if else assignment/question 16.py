menu_option = input("Enter a menu option (Pizza, Burger, Pasta): ").capitalize()
if menu_option == "Pizza":
    print("Price: $10")
elif menu_option == "Burger":
    print("Price: $7")
elif menu_option == "Pasta":
    print("Price: $8")
else:
    print("Invalid menu option! Please choose Pizza, Burger, or Pasta.")

