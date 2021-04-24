import cv2 
import uuid 

cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    img_name = 'C:/Users/kctey/OneDrive/Desktop/VSC/ComputerVision/RealTimeMaskDetection/Image_dataset/{}.jpg'.format(str(uuid.uuid1()))
    cv2.imwrite(img_name, frame)
    cv2.imshow('webcam', frame)
    
    if cv2.waitKey(1) == ord('a'):
        break

cap.release()
cap.destroyAllWindows()