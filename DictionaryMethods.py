d = {}
d['name']='sujon'
d['age'] = 43
d['address'] = 'dhaka'
print d
return_value = d.clear()
print d
print return_value
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'sujon'
y['machines'].remove('bar')
print x
print y
