from matplotlib.colors import to_hex
from numpy import asarray


class ImageReader:

    def __init__(self, image, boxes):
        self.data = asarray(image.resize(boxes))
        self.boxes = boxes

    def getEdgeArray(self):
        squares = []
        for x in range(self.boxes[0]):
            squares.append(self.rgbToHex(self.data[0, x]))
        for y in range(self.boxes[1] - 1):
            squares.append(self.rgbToHex(self.data[y + 1, self.boxes[0] - 1]))
        for x in range(self.boxes[0] - 1, 0, -1):
            squares.append(self.rgbToHex(self.data[self.boxes[1] - 1, x]))
        for y in range(self.boxes[1] - 1, 1, -1):
            squares.append(self.rgbToHex(self.data[y, 0]))
        return squares

    def rgbToHex(self, rgb):
        return to_hex(rgb / 255)
