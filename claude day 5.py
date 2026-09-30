notes = ["Learning Python " ,  "Day 5 of 30 " , "File handling is fun"]

# with open ("notes.txt" , "w") as f:
#     for items in notes:
#         f.write(items+ "\n")


# with open("notes.txt" , "r") as f :
#     data = f.read()
#     print(data)

# with open("notes.txt" , "r") as f :
#     for lines in f :
#         print(lines)

# with open("notes.txt" , "r") as f :
#     data = f.readlines()
#     print(data)

# with open("notes.txt" , "a") as f :
#     data = f.write("This line was added later \n")


# with open("notes.txt" , "r") as f :
#     data = f.read()

# lines = data.splitlines()
# words = data.split()

# print(f"Total lines in file is : {len(lines)}")
# print(f"Total words in file is : {len(words)}")

# def write_log(message):
#     with open("activity.log", "a") as f:
#         f.write(f"LOG: {message}\n")

# write_log("Script started")
# write_log("Processing data")
# write_log("Script finished")

# with open("activity.log", "r") as f:
#     print(f.read())


def filter_numbers(input_file, output_file):
    with open(input_file, "r") as f:
        lines = f.readlines()
    
    numbers_only = []
    for line in lines:
        clean_line = line.strip()          
        if clean_line.isdigit():           
            numbers_only.append(clean_line)
    
    with open(output_file, "w") as f:
        for num in numbers_only:
            f.write(num + "\n")

filter_numbers("data.txt", "filtered_numbers.txt")