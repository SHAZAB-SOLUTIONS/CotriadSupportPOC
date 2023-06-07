import cv2

cap = cv2.VideoCapture("rtsp://admin:Shazabadmin123@172.16.1.5:554")

if not cap.isOpened():
    print("Cannot open camera")
    exit()

ret, frame = cap.read()
imagePath = "/home/fuzail/Desktop/interProcessComm/shazabRandD/levelup/getCameraSnapshot/snapShots/image1.png"
cv2.imwrite(imagePath, frame)

# while(True):
#     ret, frame = cap.read()

#     if not ret:
#         print("Cannot read frame")
#         break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     frame = cv2.resize(frame, (1270,720))
#     cv2.imshow('Camera', frame)

#     if cv2.waitKey(5) & 0xFF == ord('q'):
#         break

cap.release()
cv2.destroyAllWindows()
