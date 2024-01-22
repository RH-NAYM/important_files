import os
import shutil
input_dir = 'xx'
output_images_dir = 'imgs'
output_labels_dir = 'lbl'
os.makedirs(output_images_dir, exist_ok=True)
os.makedirs(output_labels_dir, exist_ok=True)
all_files = os.listdir(input_dir)
image_files = [f for f in all_files if f.endswith('.jpg')]
for image_file in image_files:
    image_path = os.path.join(input_dir, image_file)
    label_file = image_file.replace('.jpg', '.txt')
    label_path = os.path.join(input_dir, label_file)

    shutil.move(image_path, os.path.join(output_images_dir, image_file))

    shutil.move(label_path, os.path.join(output_labels_dir, label_file))

print("Dataset organized successfully.")
