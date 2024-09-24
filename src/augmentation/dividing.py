import os
import shutil
import random

# Define paths for original dataset and train/valid/test folders
original_dataset_dir = "/path/to/original/dataset"
train_dir = "/path/to/train"
valid_dir = "/path/to/valid"
test_dir = "/path/to/test"

# Create train/valid/test folders if they don't exist
for directory in [train_dir, valid_dir, test_dir]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Define the ratio of images for train, valid, and test sets (e.g., 70%, 15%, 15%)
train_ratio = 0.7
valid_ratio = 0.15
test_ratio = 0.15

# List all classes in the original dataset
classes = os.listdir(original_dataset_dir)

# Iterate over each class
for class_name in classes:
    class_dir = os.path.join(original_dataset_dir, class_name)
    
    # List all images in the class directory
    images = os.listdir(class_dir)
    random.shuffle(images)  # Shuffle the images

    # Calculate the number of images for each set
    num_images = len(images)
    num_train = int(train_ratio * num_images)
    num_valid = int(valid_ratio * num_images)
    num_test = num_images - num_train - num_valid

    # Allocate images to train, valid, and test sets
    train_images = images[:num_train]
    valid_images = images[num_train:num_train + num_valid]
    test_images = images[num_train + num_valid:]

    # Move images to train folder
    for image in train_images:
        src = os.path.join(class_dir, image)
        dst = os.path.join(train_dir, class_name, image)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy(src, dst)

    # Move images to valid folder
    for image in valid_images:
        src = os.path.join(class_dir, image)
        dst = os.path.join(valid_dir, class_name, image)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy(src, dst)

    # Move images to test folder
    for image in test_images:
        src = os.path.join(class_dir, image)
        dst = os.path.join(test_dir, class_name, image)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy(src, dst)

print("Dataset split completed successfully.")
