import os

source_dir = "/Users/ahmedsaidgulsen/Desktop/newdatas/test/images"
destination_file = "test_new.txt"

# List files in the source directory
image_files = os.listdir(source_dir)

# Write file paths to the destination text file
with open(destination_file, 'a') as f:
    for image_file in image_files:
        image_path = os.path.join("/content/darknet/build/darknet/x64/data/obj/", image_file)
        f.write(image_path + '\n')
        print(f"appended {image_path}")
