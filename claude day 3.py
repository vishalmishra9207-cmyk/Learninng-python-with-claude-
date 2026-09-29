# fruits = ["apple", "banana", "mango", "orange"]

# print(fruits[-1])

# fruits.append("grapes")

# fruits.remove("banana")

# print(fruits)

# numbers = [10, 20, 30, 40, 50, 60, 70, 80]

# print(numbers[0:3])

# print(numbers[-3:])

# print(numbers[::2])

# sq_num = []

# for i in range(1,21):
#     i = i** 2 
#     sq_num.append(i)

# print(sq_num)

# def heighest_num(numbers):
#     big_num = numbers[0]
#     for num in numbers :
#         if num > big_num :
#             big_num = num
#     return big_num

# print(heighest_num(numbers))

# def averag_list(numbers):
#     avg = sum(numbers) / len(numbers)
#     return avg

# print(averag_list(numbers))

# my_tuple = (1, 2, 3)
# my_tuple[0] = 10

sq_num = [i**2 for i in range(1, 21)]
print(sq_num)