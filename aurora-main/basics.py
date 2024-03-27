import cv2
import numpy as np
import matplotlib.pyplot as plt


 
image = cv2.imread("bird.jpg", cv2.IMREAD_COLOR)
cv2.imshow("image", image)
cv2.waitKey(0)
 
cv2.destroyAllWindows()
