import cv2
import os

# Open the video file
video_capture = cv2.VideoCapture('DJI_0899.MOV')

# Create a directory to save the frames
os.makedirs('frames2', exist_ok=True)

frame_count = 0

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Calculate the starting and ending positions for cropping
    crop_width = 1200
    start_x = (int(frame.shape[1]) - crop_width) // 2
    end_x = start_x + crop_width

    # Crop the frame to the desired width
    cropped_frame = frame[:, start_x:end_x]

    # Save the cropped frame as an image
    frame_filename = os.path.join('frames2', f'frame_{frame_count:04d}.jpg')
    cv2.imwrite(frame_filename, cropped_frame)

    frame_count += 1

# Release the video object
video_capture.release()
cv2.destroyAllWindows()
