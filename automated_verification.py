import csv

def check_name_in_email(name, email):
    name_parts = name.lower().split()
    email = email.lower()
    return any(part in email for part in name_parts)

def process_csv(file_path, output_file_path):
    with open(file_path, newline='') as csvfile, open(output_file_path, 'w', newline='') as outfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames + ['Result']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            email = row['Email Address']
            if email:  # Only process rows where email is not empty
                first_name = row['First Name']
                result = check_name_in_email(first_name, email)
                row['Result'] = 'Pass' if result else 'Fail'
                writer.writerow(row)

# Change this to the path of your CSV file
file_path = 'data.csv'
output_file_path = 'subject_for_review.csv'

# Process the CSV and export results to a new file
process_csv(file_path, output_file_path)
