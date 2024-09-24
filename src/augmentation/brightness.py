import cv2
import os
import numpy as np
import random

# Function to apply random brightness and contrast adjustment to a single image
def apply_random_brightness_contrast(image, brightness_range=(-50, 50), contrast_range=(0.5, 1.5)):
    if image is None:
        return None
    
    # Generate random brightness and contrast values within the specified ranges
    random_brightness = random.randint(brightness_range[0], brightness_range[1])
    random_contrast = random.uniform(contrast_range[0], contrast_range[1])

    # Apply brightness and contrast adjustment
    adjusted_image = cv2.addWeighted(image, random_contrast, 
                                      np.zeros(image.shape, dtype=image.dtype), 
                                      0, random_brightness)
    return adjusted_image

# Directory containing the original images
original_dir = "/Users/ahmedsaidgulsen/Desktop/yenitabelalar/input/"

# Directory to save the adjusted images
augmented_dir = "/Users/ahmedsaidgulsen/Desktop/yenitabelalar/output/"

# Create the output directory if it doesn't exist
if not os.path.exists(augmented_dir):
    os.makedirs(augmented_dir)

# List all files in the input directory
files = os.listdir(original_dir)

# Parameters for brightness and contrast adjustment
brightness_range = (-50, 50)
contrast_range = (0.5, 1.5)

# Iterate through each file in the input directory
a = 0
for file in files:
    # Read the image
    image_path = os.path.join(original_dir, file)
    image = cv2.imread(image_path)

    # Check if the image was read successfully
    if image is None:
        print(f"Failed to read image: {file}")
        continue

    # Apply brightness and contrast adjustment
    adjusted_image = apply_random_brightness_contrast(image, 
                                                       brightness_range=brightness_range, 
                                                       contrast_range=contrast_range)

    # Check if the adjustment was successful
    if adjusted_image is None:
        print(f"Failed to apply adjustment to image: {file}")
        continue

    # Save the adjusted image
    a += 1
    output_path = os.path.join(augmented_dir, f"ilerimecburi_brightness{a}.png")
    cv2.imwrite(output_path, adjusted_image)


