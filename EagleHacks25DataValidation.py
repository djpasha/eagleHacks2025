import csv
import re
with open('messy_rental_data_updated.csv', mode='r') as file:
    csvFile = csv.reader(file)
    
    # Function to ensure that the number is valid
    def is_valid_phone(phone):
        # Check if the phone number has exactly 10 digits and maybe one hyphen
        pattern = r'^\d{3}-\d{7}$|^\d{10}$'
        return bool(re.match(pattern, phone))

    # Function to check for invalid data
    def check_invalid_data(row):
        valid = True

        # Check Customer_Name, Phone_Number, Email, etc. for invalid data
        for index, field in enumerate(row):
            if field == '???':
                valid = False
                print(f"Incomplete data: Field {header[index]} contains '???'. Please re-enter.")
                row[index] = input(f"Please enter a valid {header[index]}: ")
            elif field == 'XXX-????':
                valid = False
                print(f"Incomplete data: Field {header[index]} contains 'XXX-????'. Please re-enter.")
                row[index] = input(f"Please enter a valid {header[index]}: ")
        
        # Check for invalid phone number (not exactly 10 digits or contains non-digit characters other than '-')
        if not is_valid_phone(row[1]):  # Assuming phone number is at index 1
            valid = False
            print(f"Invalid phone number format: {row[1]}. Please re-enter.")
            row[1] = input("Please enter a valid phone number (10 digits with optional hyphen): ")
        
        return valid, row

    # Read CSV file
    with open('messy_rental_data_updated.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        
        # Read the header row (first line)
        header = next(csv_reader)

        # Process each row
        for row in csv_reader:
            # Print current row for reference
            print(f"\nChecking data: {row}")
            
            # Check and validate the row
            valid, updated_row = check_invalid_data(row)

            # If the row is invalid, prompt the user for corrections
            if not valid:
                print("The data was incomplete or invalid. The corrected data is:")
                print(updated_row)
            
            # The data will be displayed if its valid
            else:
                print("The data is valid:")
                print(updated_row)

            print("\n")

