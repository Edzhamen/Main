import csv

# Specify the path to your CSV file
csv_file_path = "example.csv"

# Open the CSV file in read mode
with open(csv_file_path, mode='r') as file:

    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Read and print each row from the CSV file
    for row in csv_reader:
        print("Name:", row[0])
        print("Age:", row[1])
        print("Location:", row[2])
        print("-" * 20)
