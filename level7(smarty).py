#http://www.pythonchallenge.com/pc/def/oxygen.html
from PIL import Image
import re
im = Image.open('data/level7oxygen.png')
f=open('data/level7output.txt','w+')
x,y=im.size
for i in range(0,x,7):
    px=im.getpixel((i,43))
    char=chr(px[0])
    if px[0]==px[1]==px[2]:
        f.write('{}'.format(char))
    else:
        break
f.close()
f=open('data/level7output.txt','r')
line=f.read()
nums=re.findall('(\d{3})',line)
answer = ''.join([chr(int(num)) for num in nums])
print(answer)
