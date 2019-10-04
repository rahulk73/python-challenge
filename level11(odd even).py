#http://huge:file@www.pythonchallenge.com/pc/return/5808.html
from PIL import Image
im = Image.open('data/level11cave.jpg')
w,h=im.size
pixels = im.load()
i=1
while i < w*h:
    pixels[i%w,i//w]=(0,0,0)
    if i%w == w-1:
        i+=1
    elif i%w == w-2:
        i+=3
    else:
        i+=2
im.show()