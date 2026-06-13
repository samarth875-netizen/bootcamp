import cv2
# Load an image
cap = cv2.VideoCapture(0) # Open the default camera (0)
while True:         
    ret, frame = cap.read()  # Capture frame-by-frame
    if not ret:
        break  # If the frame is not captured successfully, exit the loop
    cv2.line(frame, (0,1), (frame.shape[1], frame.shape[0]),(0, 255, 0), 5)
    cv2.line(frame,(0,frame.shape[0]),(frame.shape[1],1),(225,0, 0), 5) # Draw a green line from top-left to bottom-right
    cv2.imshow('Video with Line', frame)  # Display the resulting frame
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on 'q' key press
        break
cap.release()
cv2.destroyAllWindows()