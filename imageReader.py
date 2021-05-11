from matplotlib.colors import to_hex
from numpy import asarray


class ImageReader:

    def __init__(self, image, boxes):
        self.data = asarray(image.resize(boxes))
        self.boxes = boxes

    def getEdgeArray(self):
        squares = []
        data = self.data
        boxes = self.boxes
        for x in range(boxes[0]):
            squares.append(to_hex(data[0, x] / 255))
        for y in range(boxes[1] - 1):
            squares.append(to_hex(data[y + 1, boxes[0] - 1] / 255))
        for x in range(boxes[0] - 1, 0, -1):
            squares.append(to_hex(data[boxes[1] - 1, x] / 255))
        for y in range(boxes[1] - 1, 1, -1):
            squares.append(to_hex(data[y, 0] / 255))
        return squares
