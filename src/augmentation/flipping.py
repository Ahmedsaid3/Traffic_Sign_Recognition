import cv2
import os

# Function to apply flipping augmentation to a single image
def apply_flip(image, flip_code):
    # flip_code = 0 for flipping around the x-axis (horizontal flip)
    # flip_code > 0 for flipping around the y-axis (vertical flip)
    flipped_image = cv2.flip(image, flip_code)
    return flipped_image

# Directory containing the original images
original_dir = "/Users/ahmedsaidgulsen/Desktop/yenitabelalar/input/"

# Directory to save the augmented images
augmented_dir = "/Users/ahmedsaidgulsen/Desktop/yenitabelalar/output/"

# Create the augmented directory if it doesn't exist
if not os.path.exists(augmented_dir):
    os.makedirs(augmented_dir)

# List all files in the original directory
files = os.listdir(original_dir)
a = 0
# Iterate through each file in the original directory
for file in files:
    # Read the image
    image_path = os.path.join(original_dir, file)
    image = cv2.imread(image_path)

    # Apply vertical flip
    flipped_vertical = apply_flip(image, flip_code=1)
    # Save the flipped image
    a += 1
    cv2.imwrite(os.path.join(augmented_dir, f"ekrangrntss_flippedtoright{a}.png"), flipped_vertical)

