import csv
import os

def generate_contacts_csv():
    # File paths
    txt_file_path = "contacts.txt"
    csv_file_path = "contacts.csv"

    if not os.path.exists(txt_file_path):
        raise FileNotFoundError("Please create number.txt file first!")

    # Define all columns from the template
    fieldnames = [
        "First Name", "Middle Name", "Last Name", "Phonetic First Name",
        "Phonetic Middle Name", "Phonetic Last Name", "Name Prefix",
        "Name Suffix", "Nickname", "File As", "Organization Name",
        "Organization Title", "Organization Department", "Birthday",
        "Notes", "Photo", "Labels", "Phone 1 - Label", "Phone 1 - Value"
    ]

    # Read numbers from .txt
    with open(txt_file_path, "r") as f:
        numbers = [line.strip() for line in f if line.strip()]

    # Create new CSV with all columns but update only First Name and Phone 1 - Value
    with open(csv_file_path, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for i, number in enumerate(numbers, start=1):
            # Create a row with empty values for all fields
            row = {field: "" for field in fieldnames}
            # Update only First Name and Phone 1 - Value
            row["First Name"] = f"aa{i}"
            row["Phone 1 - Value"] = number
            writer.writerow(row)

    print("contacts.csv✅")
    return True

if __name__ == "__main__":
    generate_contacts_csv()
