import os
import shutil
import cv2


source_directory = 'frames2'

# Destination directory where selected frames will be copied
destination_directory = 'segment'

# Create the destination directory if it doesn't exist
os.makedirs(destination_directory, exist_ok=True)

# List all files in the source directory
files = os.listdir(source_directory)

files.sort()
# Iterate through the files and copy every 20th frame
frame_count = 0
frame_interval = 20

for file_name in files:
    if file_name.endswith('.jpg'):  # You can adjust the file extension if needed
        
        if frame_count % frame_interval == 0:
            # Construct the full source and destination paths
            source_path = os.path.join(source_directory, file_name)
            destination_path = os.path.join(destination_directory, file_name)
            
            # Copy the selected frame to the destination directory
            shutil.copyfile(source_path, destination_path)
        frame_count += 1
print(f"Selected and copied {frame_count // frame_interval} frames to the destination directory.")
