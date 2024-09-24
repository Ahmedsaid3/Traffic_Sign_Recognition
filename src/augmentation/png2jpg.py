from PIL import Image
import os

# Directory containing PNG images
png_folder = "/Users/ahmedsaidgulsen/Desktop/pngfolder"

# Directory to save converted JPG images
jpg_folder = "/Users/ahmedsaidgulsen/Desktop/"

# Create the output directory if it doesn't exist
if not os.path.exists(jpg_folder):
    os.makedirs(jpg_folder)

# Iterate through each file in the PNG folder
for filename in os.listdir(png_folder):
    if filename.endswith(".png"):
        # Open the PNG image
        png_image_path = os.path.join(png_folder, filename)
        png_image = Image.open(png_image_path)

        # Convert PNG to JPG format
        jpg_image_path = os.path.join(jpg_folder, filename[:-4] + ".jpg")  # Remove ".png" extension and add ".jpg"
        png_image.convert("RGB").save(jpg_image_path, "JPEG")

        print(f"Converted {filename} to JPG format")

print("Conversion completed")
