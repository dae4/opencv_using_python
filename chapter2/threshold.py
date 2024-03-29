import cv2
import numpy as np
import matplotlib.pyplot as plt

image =cv2.imread('./data/lena.png',0)

thr,mask = cv2.threshold(image,200,1,cv2.THRESH_BINARY)
print('Treshgold used:',thr)

adapt_mask = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,10)

plt.figure(figsize=(10,3))
plt.subplot(131)
plt.axis('off')
plt.title('original')
plt.imshow(image,cmap='gray')
#이미지를 표현하는 cmap 은 컬러맵
plt.subplot(132)
plt.axis('off')
plt.title('binary theshold')
plt.imshow(mask,cmap='gray')

plt.subplot(133)
plt.axis('off')
plt.title('adaptive theshold')
plt.imshow(adapt_mask,cmap='gray')

plt.tight_layout()
plt.show()