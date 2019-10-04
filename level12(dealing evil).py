#http://huge:file@www.pythonchallenge.com/pc/return/evil.html
# ❯ curl -u huge:file http://www.pythonchallenge.com/pc/return/evil4.jpg
# Bert is evil! go back!
file = open('data/evil2.gfx','rb').read()
for i in range(5):
    open('data/%d.jpg'%i,'wb').write(file[i::5])