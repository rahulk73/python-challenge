#http://huge:file@www.pythonchallenge.com/pc/return/bull.html
a = [1, 11, 21, 1211, 111221,312211,]
def look_and_say(index):
    prev = next='1'
    for i in range(index):
        next=''
        j=1
        val = [1,prev[0]]
        while j < len(prev):
            if prev[j] == val[1]:
                val[0]+=1
            else:
                next+=str(val[0])+val[1]
                val = [1,prev[j]]
            j+=1
        next+=str(val[0])+val[1]
        prev = next
    return prev
print(len(look_and_say(30)))

import re
def describe(s):
    return "".join([str(len(m.group(0))) + m.group(1)
                    for m in re.finditer(r"(\d)\1*", s)])
seq = '1'
for i in range(30):
    seq = describe(seq)
print(len(seq))