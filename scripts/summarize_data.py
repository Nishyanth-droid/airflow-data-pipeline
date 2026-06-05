import csv

input_path = "/tmp/processed_data.csv"

print("Summarizing data...")

with open(input_path, "r") as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)
    
    print(f"Total rows: {len(rows)}")
    print(f"Columns: {reader.fieldnames}")
    
    sepal_lengths = [float(row["sepal_length"]) for row in rows]
    print(f"Average sepal length: {sum(sepal_lengths)/len(sepal_lengths):.2f}")
    print(f"Max sepal length: {max(sepal_lengths)}")
    print(f"Min sepal length: {min(sepal_lengths)}")

print("Summary complete!")
