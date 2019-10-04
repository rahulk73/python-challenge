#http://www.pythonchallenge.com/pc/def/equality.html
import re
file = open('data/level3.txt','r')
text = file.read()
file.close()
result=''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',text))
print(result)