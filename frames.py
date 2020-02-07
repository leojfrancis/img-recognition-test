import cv2
import numpy as np
import os

# Playing video from file:
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('traffic.mp4')
print(cap.get(cv2.CAP_PROP_FPS))
FPS = 5
cap.set(cv2.CAP_PROP_FPS, FPS)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out =cv2.VideoWriter(output.avi, 20.0, (640,480))
try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print('Error: Creating directory of data')

currentFrame = 0
while True:       # or while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("no frame to capture")
        break;

    # if ret == True
    # cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    # cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # out.write(frame)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)

    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
# out.release()
cv2.destroyAllWindows()