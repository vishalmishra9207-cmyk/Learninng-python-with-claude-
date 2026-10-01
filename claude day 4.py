# Q1
text = "the quick brown fox jumps over the lazy dog the fox runs"

words = text.split()

count = {}

for w in words :
    if w in count :
        count[w] += 1 
    else :
        count[w] = 1 

print(count)

#Q2
student = {"Alex": 85, "Sam": 92, "Riya": 78}

def get_student_grade(students_dict, name):
    return students_dict.get(name, "Student not found")

print(get_student_grade(student, "Alex"))

# Q3
numbers = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]

unique = sorted(set(numbers))


# Q4
sentence = "  Python is AMAZING and Powerful  "
proper = sentence.strip()
words_list = proper.split()
print("Total words:", len(words_list))

# Q5
team_a = ["Alex", "Sam", "Riya", "Jon"]
team_b = ["Sam", "Priya", "Jon", "Meera"]

common = list(set(team_a) & set(team_b))

print(common)

team_a_player = list(set(team_a) - set(team_b))
print(team_a_player)

unique_player = list(set(team_a) | set(team_b))
print(unique_player)

# Q6



def most_common_char(word):
    count = {}
    for ch in word:
        count[ch] = count.get(ch, 0) + 1
    char = max(count, key=count.get)
    return char, count[char]

print(most_common_char("programming"))
