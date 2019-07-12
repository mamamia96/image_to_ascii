import PIL
from PIL import ImageStat
import random as ra
import time
from PIL import Image
class image_stuff:
    def __init__(self, path=''):
        if len(path) < 5:
            self.img = Image.open('download.png')
        else:
            self.img = Image.open(path)
    def return_cross(self):
        
        rgb_im = self.img.convert('RGB')

        pix = []

        for x in range(self.img.width):
            for y in range(self.img.height):
                r, g, b = rgb_im.getpixel((x, y))
                if r + g + b < 350:
                    pix.append((x,y,'$'))

                
        return pix
    
    def get_height(self):
        return self.img.height
    
    def get_width(self):
        return self.img.width

# c = image_stuff()
# i = 0
# for ele in c.return_cross():
#     i += 1
#     if ele[0] != (255,255,255):
#         print(i, ele[0])