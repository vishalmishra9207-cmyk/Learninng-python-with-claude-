# # for i in range (1,51):
# #     if i % 3 ==0 and i % 5 == 0 :
# #         print("FizzBuzz")
# #     elif i % 3 == 0:
# #         print("Fizz")
# #     elif i % 5 == 0 :
# #         print("Buzz")
# #     else :
# #         print(i)

# # # q2

# # c = int(input("Enter the temperature in celsius:  "))

# # f = 1.8 * c + 32

# # print(f"Temperature in fahrenheit is {f}")

# # # Q3

# # password = input("Enter your password for checking : ")

# # score = 0 

# # if len(password) >= 8 :
# #     score += 1 

# # if any(char.isdigit() for char in password):
# #     score += 1 

# # if any(char.isupper() for char in password):
# #     score += 1 

# # if score == 3 :
# #     print("Strong")
# # elif score == 2 :
# #     print("Medium")
# # else :
# #     print("Weak")

# # # Q4

# # sum = 0 

# # for i in range(1,101):
# #     if i % 2 == 0 :
# #         sum = i + sum

# # print(f"Sum of all the even number between 1 to 100 is {sum}")

# # Q5

# import random

# secret_num = random.randint(1, 20)
# attempts = 10

# while attempts > 0:
#     print(f"You have {attempts} attempts left")
#     user_number = int(input("Enter your guess: "))
    
#     if user_number == secret_num:
#         print("You guessed the correct number!")
#         break
#     elif user_number < secret_num:
#         print("Try a higher value")
#     else:
#         print("Try a lower value")
    
#     attempts -= 1
# else:
#     print(f"Out of attempts! The number was {secret_num}")



