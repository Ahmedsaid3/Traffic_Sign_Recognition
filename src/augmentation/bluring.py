import os
import cv2
import numpy as np
import random

# Function to apply sharpening to a single image
def apply_sharpening(image):
    # Define sharpening kernel
    sharpening_kernel = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])

    # Apply sharpening filter to the image
    sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)
    return sharpened_image

# Directory containing the original images
original_dir = "/Users/ahmedsaidgulsen/Desktop/yenitabelalar/input/"

# Directory to save the augmented images
augmented_dir = "/Users/ahmedsaidgulsen/Desktop/yenitabelalar/output/"

# Create the output directory if it doesn't exist
if not os.path.exists(augmented_dir):
    os.makedirs(augmented_dir)

# List all files in the input directory
files = os.listdir(original_dir)

# Iterate through each file in the input directory
for file in files:
    # Read the image
    image_path = os.path.join(original_dir, file)
    image = cv2.imread(image_path)

    # Apply sharpening augmentation
    sharpened_image = apply_sharpening(image)

    # Save the sharpened image
    
    sharpen_output_path = os.path.join(augmented_dir, f"ilerimecburi_blured_{file}")
    cv2.imwrite(sharpen_output_path, sharpened_image)


