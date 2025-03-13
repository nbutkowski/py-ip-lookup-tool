import csv

def read_csv_as_list(file_path):
    """Reads a CSV file and returns its contents as a list of lists."""
    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)  # Convert each row into a list

def read_csv_as_dict(file_path):
    """Reads a CSV file and returns its contents as a list of dictionaries."""
    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [dict(row) for row in reader]  # Convert each row into a dictionary

def write_dict_to_csv(file_path, data, fieldnames):
    """Writes a list of dictionaries to a CSV file, ensuring only valid fields are written."""
    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            filtered_row = {key: row.get(key, "") for key in fieldnames}  # Remove extra keys
            writer.writerow(filtered_row)
