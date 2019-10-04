#http://www.pythonchallenge.com/pc/def/peak.html
import pickle
f=open('data/level5.txt','rb')
f2=open('data/level5output.txt','w')
l1=pickle.load(f)
print(l1)
for sublist in l1:
    for subtuple in sublist:
        f2.write((subtuple[0]*subtuple[1]))
    f2.write('\n')
f.close()
f2.close()