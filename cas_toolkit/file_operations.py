import csv
from datetime import datetime
import os

def read_csv(file_path):
    group_names = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  # Skip empty rows
                group_names.append(row[0].strip())
    return group_names

def write_output_csv(results, input_file):
    # Generate output filename
    directory, filename = os.path.split(input_file)
    name_without_ext = os.path.splitext(filename)[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(directory, f"{name_without_ext}_output_{timestamp}.csv")
    
    # Write results to CSV
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['name', 'status', 'id', 'message']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    
    return output_file