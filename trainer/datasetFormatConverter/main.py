import csv

# Open the input and output files
with open('labels.txt', 'r') as infile, open('labels.csv', 'w', newline='') as outfile:
    reader = infile.readlines()
    writer = csv.writer(outfile)
    
    # Write the header
    writer.writerow(['filename', 'words'])
    
    # Process each line in the input file
    for line in reader:
        parts = line.strip().split(' ', 1)  # Split only at the first space
        writer.writerow(parts)

print("Conversion completed successfully.")