import cv2
import os

frame_directory = 'frames2/'


output_video_filename = 'left.mp4'


frame_files = sorted(os.listdir(frame_directory))
# print(frame_files)

output_video = None

for frame_file in frame_files:
    
    frame = cv2.imread('frames2/'+frame_file)
    mask = cv2.imread('mask/'+frame_file, cv2.IMREAD_GRAYSCALE)
    
    if frame.shape[:2] != mask.shape:
        raise ValueError(f"Frame and mask dimensions do not match for {frame_file}.")
    
    
    # create a blurred version of the frame
    # blurred_frame = cv2.GaussianBlur(frame, (3, 3), 0)  # aadjust the kernel size 
    
    # Apply the mask to the original frame and blur the rest
    result = cv2.bitwise_and(frame, frame, mask=mask)

   
    if output_video is None:
        height, width, layers = result.shape
        output_video = cv2.VideoWriter(output_video_filename, cv2.VideoWriter_fourcc(*'mp4v'), 23, (width, height))
    
    
    output_video.write(result)
