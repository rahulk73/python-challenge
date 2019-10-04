#http://www.pythonchallenge.com/pc/def/linkedlist.php
import urllib.request
import urllib.error
import re
try:
    flag=0
    file=open('data/level4.txt','w')
    base_url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    #next_url=base_url+'12345'
    #next_url=base_url+str(16044/2)
    next_url=base_url+'63579'
    next_site=urllib.request.urlopen(next_url)
    for i in range(400):
        bytedata=next_site.read()
        string=bytedata.decode('utf8')
        print(string)
        file.write(string)
        file.write('\n')
        nothing=''.join(re.findall('and the next nothing is (\d{1,})',string))
        next_url=base_url+nothing
        next_site=urllib.request.urlopen(next_url)
        try:
            url='http://www.pythonchallenge.com/pc/def/'+nothing+'.php'
            site=urllib.request.urlopen(url)
        except urllib.error.HTTPError:
            continue
        else:
            flag+=1
            break
    print(flag)
    print(url)
    print(site.geturl())
except NameError:
    print("not found")
except KeyboardInterrupt:
    pass
finally:
    file.close()

    

