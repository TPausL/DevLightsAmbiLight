import numpy as np
from numpy import asarray, uint8


class ImageReader:
    def transfromImage(self, image, boxCount):
        boxCount = min(boxCount, min(image.size[0], image.size[1]))
        self.img = image
        self.data = asarray(image, dtype=uint8)
        boxWidth = image.size[0] // boxCount
        boxHeight = image.size[1] // boxCount
        squares = np.zeros(shape=(boxCount, boxCount, 3))
        for gY in range(boxCount):
            if gY == 0 or gY == boxCount - 1:
                for gX in range(boxCount):
                    squares[gY][gX] = self.calcSqaure((gX * boxWidth, gY * boxHeight), (boxWidth, boxHeight))
            else:
                squares[gY][0] = self.calcSqaure((0, gY * boxHeight), (boxWidth, boxHeight))
                squares[gY][(boxCount - 1)] = self.calcSqaure(((boxCount - 1) * boxWidth, gY * boxHeight),
                                                              (boxWidth, boxHeight))
        return squares

    def calcSqaure(self, point, box):
        colors = np.zeros(shape=3)
        for x in range(box[0]):
            for y in range(box[1]):
                colors += self.data[point[1] + y][point[0] + x]
        return colors / (box[0] * box[1])
