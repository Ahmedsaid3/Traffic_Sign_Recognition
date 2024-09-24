import os
import cv2
import numpy as np
import random

# Function to apply shearing transformation to a single image
def apply_shearing(image, shear_range=(-20, 20)):
    # Generate random shearing angle within the specified range
    shear_angle = random.randint(shear_range[0], shear_range[1])

    # Define shearing transformation matrix
    rows, cols, _ = image.shape
    shear_matrix = np.array([[1, np.tan(np.radians(shear_angle)), 0],
                             [0, 1, 0]], dtype=np.float32)

    # Apply shearing transformation to the image
    sheared_image = cv2.warpAffine(image, shear_matrix, (cols, rows), borderMode=cv2.BORDER_REFLECT_101)
    return sheared_image

# Directory containing the original images
original_dir = "/Users/ahmedsaidgulsen/Desktop/yenitabelalar/input/"

# Directory to save the augmented images
augmented_dir = "/Users/ahmedsaidgulsen/Desktop/yenitabelalar/output/"

# Create the output directory if it doesn't exist
if not os.path.exists(augmented_dir):
    os.makedirs(augmented_dir)

# List all files in the input directory
files = os.listdir(original_dir)

# Parameters for shearing augmentation
shear_range = (-20, 20)  # Shearing angle range in degrees

# Iterate through each file in the input directory
for file in files:
    # Read the image
    image_path = os.path.join(original_dir, file)
    image = cv2.imread(image_path)

    # Apply shearing augmentation
    sheared_image = apply_shearing(image, shear_range)

    # Save the augmented image
    output_path = os.path.join(augmented_dir, f"ilerimecburi_sheared_{file}")
    cv2.imwrite(output_path, sheared_image)

print("Shearing augmentation completed successfully.")
