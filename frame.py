import cv2
import os

video_path = 'DJI_0899.MOV'

output_directory = 'frames/'

os.makedirs(output_directory, exist_ok=True)

cap = cv2.VideoCapture(video_path)


frame_count = 0


while True:
    
    ret, frame = cap.read()

    
    if not ret:
        break

    
    output_filename = os.path.join(output_directory, f'frame_{frame_count:04d}.jpg')


    cv2.imwrite(output_filename, frame)

  
    frame_count += 1


cap.release()

print(f'{frame_count} frames saved.')
