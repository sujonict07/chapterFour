d = {}
print d.has_key('name')
d['name'] = "sujon"
print d.has_key('name')
#using items and iteritems
doc = {'title':'python website','url':'http://www.python.org','spam':0}
print doc.items()
it = doc.iteritems()
print it
print list(it)
#pop // used to get the value corresponding to a given key and than remove the key-value pair from the dectionary
poptest = {'x':1,'y':2}
print poptest
print poptest.pop('x')
print poptest
x = {'title':'python Language website'}
doc.update(x)
print doc
d = {}
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 1
print d.values()