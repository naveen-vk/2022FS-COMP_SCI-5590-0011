import cv2
import sys

imgPath = "naveen.jpg"
cascPAth = "Desktop/haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPAth)

image = cv2.imread(imgPath)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces