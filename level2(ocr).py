#http://www.pythonchallenge.com/pc/def/ocr.html
d={}
for c in open("data/level2.txt","r").read():
    if(c in d):
        d[c]+=1
    else:
        d[c]=1
print(''.join(c for c in open("file_leve2.txt","r").read() if d[c] == 1))