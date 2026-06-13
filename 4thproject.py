import cv2 
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    if not ret:
        break
    cv2.circle(frame, (frame.shape[1]//2, frame.shape[0]//2), 20, (255,0,0),3)
    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()