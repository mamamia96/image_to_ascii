import img_processing
import os
from os import system  
import platform
import random
import time
import sys



class console_painter:


    def __init__(self,console_w, console_h):
        self.console_w = console_w
        self.console_h = console_h

    def create_window(self):
        os.system('mode con: cols=' + str(self.console_w) + 'lines=' + str(self.console_h))            

    def fill_screen(self,char='.'):
        for h in range(self.console_h):
            for w in range(self.console_w):
                print(char,end='')
    
    #for painting individual points
    def paint_point(self,x,y,char='$',fill_char=' '):
        for h in range(self.console_h):
            for w in range(self.console_w):
                if w + 1 == x and h - 1 == y:
                    print(char,end='')
                else:
                    print(fill_char,end='')
            
    def paint_points(self,coords, char='$',fill_char=' '):
        for h in range(self.console_h):
            for w in range(self.console_w):
                # char = random.choice([0,1])
                if (w, h, '$') in coords:
                    print('$',end='')
                elif (w,h,'.') in coords:
                    print('.',end='')
                else:
                    print(fill_char,end='')




    def clean(self):
        """
        Clears the console
        """
        os_name = platform.system().lower()
        if 'windows' in os_name:
            system('cls')
        else:
            system('clear')
print(len(sys.argv))
img_arg = ''
if len(sys.argv) > 1:
    img_arg = sys.argv[1]
else:
    img_arg = input('enter image path: ')

im = img_processing.image_coords(path=img_arg)
c = console_painter(im.get_width(),im.get_height())
c.create_window()
c.clean()
c.paint_points(im.return_cross())
input('press enter to exit...')
        
