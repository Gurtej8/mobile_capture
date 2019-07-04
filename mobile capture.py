import urllib
import cv2
import numpy as np
url='http://10.1.2.14:8080/shot.jpg'
while True:
    imgResp=urllib.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    cv2.imshow('test',img)
    if ord('q')==cv2.waitKey(10):
        exit(0)