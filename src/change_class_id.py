import os
import glob

# Define the directory containing the files
directory_path = '/Users/ahmedsaidgulsen/Desktop/deneme'

# List of substrings to look for in file names
substrings = ['yayagecidi', 'donelkavsak', 'sagmecburiyon', 'solmecburiyon', 'ilerimecburi']

# Use glob to find all files containing any of the specified substrings in their names
files = []
for substring in substrings:
    file_pattern = os.path.join(directory_path, f'*{substring}*.txt')
    files.extend(glob.glob(file_pattern))

# Iterate through each file
a = 0
for file_path in files:
    # Read the file content
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    modified_lines = []
    for line in lines:
        # Split the line into elements
        elements = line.split()
        
        if elements:
            # Modify the first element assuming it's an integer
            elements[0] = str(int(elements[0]) + 16)
        
        # Reconstruct the line
        modified_lines.append(' '.join(elements) + '\n')
    
    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)
    a += 1
    print(f"Updated file: {file_path}")

print(a)