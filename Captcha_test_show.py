from PIL import Image
import tesserocr
import time
import matplotlib.pyplot as plt


# for i in range(1,2):
image = Image.open("3.jpg")
plt.subplot(1,4,1)
plt.title('rgb')
plt.imshow(image,cmap='gray')

r,g,b = image.split()
plt.subplot(1,4,2)
plt.title('r')
plt.imshow(r,cmap='gray')
plt.axis('off')

plt.subplot(1,4,3)
plt.title('g')
plt.imshow(g,cmap='gray')
plt.axis('off')

plt.subplot(1,4,4)
plt.title('b')
plt.imshow(b,cmap='gray')
plt.axis('off')
plt.show()


