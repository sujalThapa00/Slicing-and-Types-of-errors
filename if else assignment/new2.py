#Check whether the user input number is even or odd and display it to user.
def check():
    a= int (input ("enter any number"))
    if a%2==0:
        b=print("the number is even")
    else:
        b=print("the number is odd")
    return b 

 check() 


#Write a program that asks the user for a number in the range of 1 to 12. The program should display the corresponding month, 
# where 1=january, 2=february,3=march,4=april,5=may,6=june,7=july, 8=august,9=september,10=october,11=november,12=december. 
# The program should display an error message if the user enters a numberthat is outside the range of 1 to 12.
# Prompt user for a number between 1 and 12
number = int(input("Enter a number between 1 and 12: "))

# Check the range and display the corresponding month
if number == 1:
    print("January")
elif number == 2:
    print("February")
elif number == 3:
    print("March")
elif number == 4:
    print("April")
elif number == 5:
    print("May")
elif number == 6:
    print("June")
elif number == 7:
    print("July")
elif number == 8:
    print("August")
elif number == 9:
    print("September")
elif number == 10:
    print("October")
elif number == 11:
    print("November")
elif number == 12:
    print("December")
else:
    print("Error: Please enter a number between 1 and 12.")
