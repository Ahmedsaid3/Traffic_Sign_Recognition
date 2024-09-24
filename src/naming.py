from PIL import Image
import os

# Directory containing PNG images
jpg_folder = "/Users/ahmedsaidgulsen/Desktop/yenitabelalar/ilerimecburijpg/"

# Directory to save renamed JPG images
renamed_folder = "/Users/ahmedsaidgulsen/Desktop/yenitabelalar/ilerimecburi/"

# Create the output directory if it doesn't exist
if not os.path.exists(renamed_folder):
    os.makedirs(renamed_folder)

# Initialize counter
counter = 0

# Iterate through each file in the JPG folder
for filename in os.listdir(jpg_folder):
    if filename.endswith(".jpg"):
        # Increment counter
        counter += 1

        # Construct new filename
        new_filename = f"ilerimecburi{counter}.jpg"

        # Rename the file
        jpg_image_path = os.path.join(jpg_folder, filename)
        renamed_image_path = os.path.join(renamed_folder, new_filename)
        os.rename(jpg_image_path, renamed_image_path)

        print(f"Renamed {filename} to {new_filename}")

print("Renaming completed")
