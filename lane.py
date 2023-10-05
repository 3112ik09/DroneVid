import cv2
import numpy as np

# Load the video
cap = cv2.VideoCapture('DJI_0899.MOV')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Define the region of interest (ROI)
    height, width = edges.shape
    roi_vertices = [(0, height), (width / 2, height / 2), (width, height)]
    mask = np.zeros_like(edges)
    cv2.fillPoly(mask, np.array([roi_vertices], np.int32), 255)
    masked_edges = cv2.bitwise_and(edges, mask)

    # Apply Hough Line Transformation
    lines = cv2.HoughLinesP(masked_edges, 2, np.pi / 180, threshold=50, minLineLength=100, maxLineGap=50)

    # Filter and draw lane lines
    left_lane, right_lane = [], []
    
    for line in lines:
        x1, y1, x2, y2 = line[0]
        slope = (y2 - y1) / (x2 - x1)
        if abs(slope) > 0.5:  # Adjust the slope threshold as needed
            if slope < 0:
                left_lane.append(line[0])
            else:
                right_lane.append(line[0])

    # Create lane masks
    mask_left = np.zeros_like(masked_edges)
    mask_right = np.zeros_like(masked_edges)
    
    for line in left_lane:
        x1, y1, x2, y2 = line
        cv2.line(mask_left, (x1, y1), (x2, y2), 255, 5)

    for line in right_lane:
        x1, y1, x2, y2 = line
        cv2.line(mask_right, (x1, y1), (x2, y2), 255, 5)

    # Combine lane masks
    lane_mask = cv2.add(mask_left, mask_right)

    # Overlay lane mask on the original frame
    result = cv2.addWeighted(frame, 1, cv2.cvtColor(lane_mask, cv2.COLOR_GRAY2BGR), 0.3, 0)

    cv2.imshow('Lane Detection', result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
