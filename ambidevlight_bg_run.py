import sys
import threading

from PIL import Image
from mss import mss
from screeninfo import get_monitors

from api import Api
from imageReader import ImageReader

api = Api()
sct = mss()


def showMonOnStrip(mon, leds):
    sct_img = sct.grab(mon)
    img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, "raw", "BGRX")
    imr = ImageReader(img, leds)
    colors = imr.getEdgeArray()
    data = [{'repeat': 1, 'leds': colors}]
    api.sendCustom(data)


def loop(mon, leds):
    ticker = threading.Event()
    while not ticker.wait(0.1):
        showMonOnStrip(mon, leds)


monitors = get_monitors()
mon = monitors[int(sys.argv[1])]
show_mon = {"left": mon.x, "top": mon.y, "width": mon.width, "height": mon.height}
print("test")
loop(show_mon, (int(sys.argv[2]), int(sys.argv[3])))
