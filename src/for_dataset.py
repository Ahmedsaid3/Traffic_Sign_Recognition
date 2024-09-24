import os
import shutil

dataset_path = '/Users/ahmedsaidgulsen/Downloads/dataset1'
destination_1 = "test_new.txt"
destination_2 = "/Users/ahmedsaidgulsen/Desktop/dataset_new_copy"

# Write file paths to the destination text file
jpg_ls = []
txt_ls = []
for b in range(0,16):
    a = 0
    for filename in os.listdir(dataset_path):
        if filename.endswith('.txt'):
            txt_file_path = os.path.join(dataset_path, filename)
            with open(txt_file_path, 'r') as txt_file:
                content = txt_file.read()
                list = content.split()
                if str(b) in list[0]:
                    txt = txt_file_path.split("/")
                    jpg = txt[-1].replace('.txt', '.jpg')
                    with open(destination_1, 'a') as f:
                        image_path = os.path.join("/content/darknet/build/darknet/x64/data/obj/", jpg)
                        a += 1
                        if a < 2:
                            f.write(image_path + '\n')
                            print(f"appended {image_path}")
                            jpg_ls.append(jpg)
                            txt_ls.append(txt[-1])
  


def move_jpg_txt_files(source_dir, destination_dir):

    # Get a list of all files in the source directory
    files = os.listdir(source_dir)

    # Iterate through each file
    for file in files:
        # Check if the file is a JPG file
        if file in jpg_ls:

            # Construct paths for source and destination
            source_path = os.path.join(source_dir, file)
            destination_path = os.path.join(destination_dir, file)

            # Move the file
            shutil.move(source_path, destination_path)
            print(f"Moved '{file}' to '{destination_dir}'.")
        
        elif file in txt_ls:

            # Construct paths for source and destination
            source_path = os.path.join(source_dir, file)
            destination_path = os.path.join(destination_dir, file)

            # Move the file
            shutil.move(source_path, destination_path)
            print(f"Moved '{file}' to '{destination_dir}'.")


move_jpg_txt_files(dataset_path, destination_2)

   