#http://www.pythonchallenge.com/pc/def/map.html
import string
mylist=list("map")
for i in range(len(mylist)):
  str=mylist[i]
  if(str.isalpha()):
    char_num=ord(str)-97
    char=chr(((char_num+2)%26)+97)
    mylist[i]=char
print(''.join(mylist))
str="map"
str=str.maketrans(string.ascii_lowercase,string.ascii_lowercase[2:]+string.ascii_lowercase[:2])
print(str)