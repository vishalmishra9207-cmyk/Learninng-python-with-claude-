import csv
import json

csv_file = 'students.csv'

with open(csv_file, 'w' , newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["name" , "marks" , "city"])
    students = [
        ["Aarav", 88, "Delhi"],
        ["Priya", 92, "Mumbai"],
        ["Rahul", 75, "Bangalore"]
    ]

    writer.writerows(students)

print("CSV file created successfully.")


with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    next(reader)  
    for row in reader:
        print(row)


# def dict_reader_example(csv_file):
#     with open(csv_file, 'r') as f:
#         reader = csv.DictReader(f)
#         rows = list(reader)
#         total_marks = 0 
#         for row in rows: 
#             print(f"{row['name']} scored {row['marks']}")
#             total_marks += int(row['marks'])

    
#         print(f"Average marks for the class is {sum(int(row['marks']) for row in rows) / len(rows)}")

# dict_reader_example("students.csv")


# data = {"name": "Vishal", "skills": ["Python", "Git"], "active": True}

# json_file = "profile.json"
# compact_file = "profile_compact.json"

# with open(json_file, "w") as f:
#     json.dump(data, f, indent=4)

# with open(compact_file, "w") as f:
#     json.dump(data, f)

# print("Both JSON files created.")


# with open(json_file, "r") as f:
#     data = json.load(f)

# print("Name :" , data["name"])
# print("Skills :" , ", ".join(data["skills"]))
# print("Active :" , data["active"])

def csv_to_json(csv_path , json_path):
    data = []
    try :
        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["marks"] = int(row["marks"])
                data.append(row)

    except FileNotFoundError:
        print("CSV is not found.")

    else :
        with open (json_path, 'w') as out_file:
            json.dump(data, out_file, indent=4)
            print(f"Saved {len(data)} students to {json_path}")


csv_to_json("students.csv" , "students.json")
csv_to_json("missing.csv" , "out.json")