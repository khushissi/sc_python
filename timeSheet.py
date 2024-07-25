import csv

# Define the CSV file name
csv_file = 'timesheet.csv'

# Initialize the CSV file with headers if it doesn't exist
def initialize_csv():
    try:
        with open(csv_file, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Serial Number', 'Employee Number', 'Task', 'Time Taken', 'Comments'])
    except FileExistsError:
        pass

# Function to add an entry to the timesheetz
def add_entry(serial_number, employee_number, task, duration, comments):
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([serial_number, employee_number, task, duration, comments])

# Function to display the timesheet
def display_timesheet():
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))

# Main function to handle user commands
def main():
    initialize_csv()
    while True:
        print("\nTimesheet Management System")
        print("1. Add Entry")
        print("2. Display Timesheet")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            serial_number = input("Enter Serial Number: ")
            employee_number = input("Enter Employee Number: ")
            task = input("Enter Task: ")
            duration = input("Enter the time taken to complete the task: ")
            comments = input("Enter Comments: ")
            add_entry(serial_number, employee_number, task, duration, comments)
            print("Entry added successfully!")
        elif choice == '2':
            display_timesheet()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
