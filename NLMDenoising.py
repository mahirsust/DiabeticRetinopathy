import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('H:/xampp/htdocs/DiabeticRetinopathy/new_images/img/12_right.jpeg')

b,g,r = cv2.split(img)           # get b,g,r
rgb_img = cv2.merge([r,g,b])     # switch it to rgb

# Denoising
dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

b,g,r = cv2.split(dst)           # get b,g,r
rgb_dst = cv2.merge([r,g,b])     # switch it to rgb

cv2.imwrite("H:/xampp/htdocs/DiabeticRetinopathy/Denoised_Images/12_right_denoised.jpeg", dst)

plt.subplot(211),plt.imshow(rgb_img)
plt.subplot(212),plt.imshow(rgb_dst)
plt.show()