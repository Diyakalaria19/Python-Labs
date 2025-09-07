#Question 1
# import numpy as np
# from PIL import Image

# img = Image.open(r"E:\SEM 3\PWP\Class Tutorials\MU.jpg")
# img_array = np.array(img)
# height, width, channels = img_array.shape
# min_blue = img_array[:, :, 2].min()   
# print(f"Image Dimensions: {img_array.shape}")  
# print(f"Height: {height}, Width: {width}, Channels: {channels}")
# print(f"Minimum pixel value in Blue channel: {min_blue}")

#Question 2
# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt

# img = Image.open(r"E:\SEM 3\PWP\Class Tutorials\MU.jpg")
# img_array = np.array(img)
# padded_img = np.pad(img_array, ((50, 50), (100, 100), (0, 0)), mode='constant', constant_values=0)
# plt.figure(figsize=(10,5))
# plt.subplot(1,2,1)
# plt.imshow(img_array)
# plt.title("Original Image")
# plt.axis("off")
# plt.subplot(1,2,2)
# plt.imshow(padded_img)
# plt.title("Padded Image (Black)")
# plt.axis("off")
# plt.tight_layout()
# plt.show()


#Question 3
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open(r"E:\SEM 3\PWP\Class Tutorials\MU.jpg")
img_array = np.array(img)
R = img_array[:, :, 0]
G = img_array[:, :, 1]
B = img_array[:, :, 2]

plt.figure(figsize=(12,4))
plt.subplot(1,3,1)
plt.imshow(R, cmap="Reds")
plt.title("Red")
plt.axis("off")
plt.subplot(1,3,2)
plt.imshow(G, cmap="Greens")
plt.title("Green")
plt.axis("off")
plt.subplot(1,3,3)
plt.imshow(B, cmap="Blues")
plt.title("Blue")
plt.axis("off")
plt.tight_layout()
plt.show()
