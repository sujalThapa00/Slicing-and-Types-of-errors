# import random

# def arithmetic_quiz():
#     print("Welcome to the Arithmetic Quiz! Type 'exit' to stop.")

#     while True:
#         num1, num2 = random.randint(1, 30), random.randint(1, 30)
#         correct_answer = num1 * num2

#         user_input = input(f"What is {num1} * {num2}? ")
#         if user_input.lower() == "exit":
#             print("bye!")
#             break

#         if user_input.isdigit() and int(user_input) == correct_answer:
#             print("Correct!")
#         else:
#             print("Incorrect, try again.")

# if __name__ == "__main__":
#     arithmetic_quiz()




# while True:
#     user_input = input("Enter your age (or type 'stop' to exit): ").strip()
#     if user_input.lower() == "stop":
#         break
#     if user_input.isdigit():
#         age = int(user_input)
#         if age < 18:
#             print("You are a minor.")
#         elif age <= 60:
#             print("You are an adult.")
#         else:
#             print("You are a senior citizen.")
#     else:
#         print("Please enter a valid age or 'stop'.")




# while True:
#     vehicle = input("Enter the name of a vehicle: ").strip().lower()
#     if vehicle == "bus":
#         print("Finally the wait is over.")
#         break
#     else:
#         print("Waiting...")





# while True:
#     fruit = input("Enter the name of a fruit: ").strip().lower()
#     if fruit == "apple":
#         print("You got it!")
#         break
#     else:
#         print("Try again")





# while True:
#     day = input("Enter a day of the week: ")
#     if day.lower() == "saturday":
#         print("Enjoy your weekend!")
#         break
#     else:
#         print("It's not the weekend yet.")




# import random
# random_number = random.randint(1, 10)
# attempts = 0
# while True:
#     guess = int(input("Guess a number between 1 and 10: "))
#     attempts += 1 
#     if guess < random_number:
#         print("Guess higher!")
#     elif guess > random_number:
#         print("Guess lower!")
#     else:
#         print(f"Congratulations! You guessed the correct number {random_number} in {attempts} attempts.")
#         break




# correct_username = "admin"
# correct_password = "1234"

# attempts = 0
# max_attempts = 3

# while attempts < max_attempts:
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     if username == correct_username and password == correct_password:
#         print("Login successful!")
#         break
#     else:
#         attempts += 1
#         print("Invalid credentials, try again.")
#         if attempts == max_attempts:
#             print("Too many failed attempts. You are locked out.")





# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# while True:
#     user_input = input("Enter a number (or type 'exit' to quit): ")
#     if user_input.lower() == "exit":
#         print("Goodbye!")
#         break
#     try:
#         number = int(user_input)
#         if is_prime(number):
#             print("The number is prime.")
#         else:
#             print("The number is not prime.")
#     except ValueError:
#         print("Please enter a valid number or 'exit' to quit.")




# while True:
#     user_input = input("Enter a number (or type 'exit' to quit): ")
    
#     if user_input.lower() == "exit":
#         print("Goodbye!")
#         break
    
#     try:
#         num = int(user_input)
        
#         if num < 2:
#             print("The number is not prime.")
#         else:
#             for i in range(2, num):
#                 if num % i == 0:
#                     print("The number is not prime.")
#                     break
#             else:
#                 print("The number is prime.")
#     except ValueError:
#         print("Please enter a valid number or 'exit' to quit.")





# secret_word = "python"

# while True:
#     guess = input("Guess the secret word (or type 'quit' to exit): ")
    
#     if guess.lower() == "quit":
#         print("Goodbye!")
#         break
    
#     if guess.lower() == secret_word:
#         print("Congratulations, you guessed the word!")
#         break
#     else:
#         print("Incorrect, try again.")





