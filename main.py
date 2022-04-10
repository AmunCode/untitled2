import cv2
from pyzbar.pyzbar import decode

# img = cv2.imread('testing3.png')
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

camera = True
while camera:
    success, frame = cap.read()

    for code in decode(frame):
        print(code.data)
        cv2.imshow("test code", frame)
        cv2.waitKey(1)
# for code in decode(img):
#     # print(code)
#     # print(type(code))
#     print(code.data.decode('utf-8'))


