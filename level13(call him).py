#http://huge:file@www.pythonchallenge.com/pc/return/disproportional.html
# import xmlrpc.client
# connection = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
# print(connection.system.listMethods())
# print(connection.system.methodHelp('phone'))
# print(connection.system.methodSignature("phone"))
# print(connection.phone('Bert'))
from string import ascii_lowercase
import enchant

l1 = []
d = enchant.Dict("en_US")
for c1 in ascii_lowercase:
    for c2 in ascii_lowercase:
        s = set()
        for c3 in ascii_lowercase:
            w = c1+c3+c2
            if d.check(w) :
                w2 = w
                s.add(w)
        if len(s)==5:
            l1.append({w2:s})
print(l1)