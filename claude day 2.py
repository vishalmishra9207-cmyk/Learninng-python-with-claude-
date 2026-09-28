# # # Q1
# def add(a,b):
#     add = a + b 
#     return add

# print(add(4,5))

# # # Q2

# name = input("Enter name : ")

# greeting = "Hello"

# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}!")

# greet("Alex")                 
# greet("Alex", "Good morning")  

# # # Q3

# x = 10

# def my_function():
#     x = 5
#     print("Inside function:", x)

# my_function()
# print("Outside function:", x)

# # # Q4

# n = int(input("Enter the number for check : "))

# def check_num (n):
#     if n > 0 :
#         return "Possitive"
#     elif n < 0 :
#         return "Negtive"
#     else :
#         return "Zero"

# print(check_num(n))

# # Q5

# password = input("Enter your password for checking :")

# def password_check (password) :
#         score = 0 

#         if len(password) >= 8 :
#              score += 1 

#         if any(char.isdigit() for char in password):
#             score += 1 

#         if any(char.isupper() for char in password):
#             score += 1 

#         if score == 3 :
#             return "Strong"
#         elif score == 2 :
#             return "Medium"
#         else :
#             return "Weak"


# print(password_check(password))