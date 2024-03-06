from datetime import datetime

# Get the start date from the user
start_date_input = input("Enter the start date (YYYY-MM-DD): ")

# Convert the start date string to a datetime object
start_date = datetime.strptime(start_date_input, "%Y-%m-%d")

# Get the current date
current_date = datetime.now()

# Calculate the length of time worked
length_of_time_worked = current_date - start_date

# Print the result
print(f"Length of time worked: {length_of_time_worked}")