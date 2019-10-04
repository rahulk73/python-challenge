#http://www.pythonchallenge.com/pc/def/channel.html
import zipfile,re
try:
    archive=zipfile.ZipFile('data/channel.zip','r')
    nothing='90052'
    f2=open('data/level6output.txt','w')
    while True:
        f=open('./data/level6-channel/'+nothing+'.txt','r')
        line=f.read()
        #print(line)
        match=re.search('\D+(\d{1,})',line)
        nothing=match.group(1)
        f2.write(archive.getinfo(nothing+'.txt').comment.decode('utf8'))
        f.close()
except KeyboardInterrupt:
    pass
except Exception as e:
    print(e)
finally:
    f2.close()
    f.close()
