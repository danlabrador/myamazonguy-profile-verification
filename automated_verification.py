import csv

def check_name_in_email(name, email):
    name_parts = name.strip().lower().split()
    email = email.strip().lower()
    
    if not email:
        return False  # Skip records with no email
    
    return any(part in email for part in name_parts)

def process_csv(file_path, output_file_path):
    with open(file_path, mode='r', encoding='utf-8', newline='') as csvfile, open(output_file_path, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames + ['Result']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            name = (row['First Name'] + ' ' + row['Last Name']).strip()  # Combine and strip spaces
            email = row['Email Address']
            if email:
                result = check_name_in_email(name, email)
                if not(result):
                    row['Result'] = ''
                    writer.writerow(row)

# Change this to the path of your CSV file
file_path = 'data.csv'
output_file_path = 'subject_for_review.csv'

# Process the CSV and export results to a new file
process_csv(file_path, output_file_path)
