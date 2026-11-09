import csv
import requests
from docx import Document

BASE_URL = "https://jsonplaceholder.typicode.com"


# STAGE 1: fetch_json (same as Day 13)
def fetch_json(url, params=None):
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None
    else:
        return response.json()


# STAGE 2: keep only name, email, city
def build_short_users(users):
    short_users = []
    for user in users:
        short_users.append({
            "name": user["name"],
            "email": user["email"],
            "city": user["address"]["city"],
        })
    return short_users


# STAGE 3: save to CSV
# data is already the short list, so city is read directly (no ["address"])
def save_csv(data, csv_path):
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "email", "city"])
        for user in data:
            writer.writerow([user["name"], user["email"], user["city"]])


# STAGE 4: save to Word (.docx)
def save_docx(data, docx_path):
    doc = Document()
    doc.add_heading("User Report", level=1)

    table = doc.add_table(rows=1, cols=3)
    table.style = "Table Grid"
    table.rows[0].cells[0].text = "Name"
    table.rows[0].cells[1].text = "Email" 
    table.rows[0].cells[2].text = "City"

    for user in data:
        cells = table.add_row().cells
        cells[0].text = user["name"]
        cells[1].text = user["email"]
        cells[2].text = user["city"]

    doc.save(docx_path)


# STAGE 5: main() is your task. It goes here.


if __name__ == "__main__":
    # Temporary test lines, move this logic into main() in Stage 5
    users = fetch_json(f"{BASE_URL}/users")
    short_users = build_short_users(users)
    save_csv(short_users, "users.csv")
    save_docx(short_users, "users_report.docx")
    print("Files saved")



def main():
    csv_path = "users.csv"
    docx_path = "users_report.docx"
    users = fetch_json(f"{BASE_URL}/users")
    if users is None:
        print("Failed to fetch users")
        return
    short_users = build_short_users(users)
    save_csv(short_users, csv_path)
    save_docx(short_users, docx_path)
    print(f"Files saved {len(short_users)} users to {csv_path} and {docx_path}")

main()