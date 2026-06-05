import csv

input_path = "/tmp/raw_data.csv"
output_path = "/tmp/processed_data.csv"

print("Processing data...")

with open(input_path, "r") as infile, open(output_path, "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    
    count = 0
    for row in reader:
        if row["species"] == "setosa":
            writer.writerow(row)
            count += 1

print(f"Filtered {count} rows where species is 'setosa'")
print(f"Saved to {output_path}")
