import matplotlib.pyplot as plt
from PIL import Image

from imageReader import ImageReader

img = Image.open("./rg.png")

imr = ImageReader()
squares = imr.transfromImage(img, 15)

imgplot = plt.imshow(squares)
plt.show()
