#Dictionary in python

d={1:'vijay',2:'nani',3:7896}
print(type(d))
print(d)



#Dictionary Methods
'''
1.get ()
2.Items ()P
3.Keys ()
4.update ()
5.values ()
6.clear ()

'''
#1.get ()
d={1:'abhi',45:'vishanu',3:'krishna'}
print(d.get(3))

#2. Items ()
vijay={1:'abhi',45:'vishanu',3:'krishna'}
print(vijay.items())

#3.Keys ()
vijay={1:'abhi',45:'vishanu',3:'krishna'}
print(vijay.keys())

#4.values()
vij={1:'abhi',45:'vishanu',3:'krishna'}
print(vij.values())

#5.update ()P
vijay={8:'rama',7:'shiva',6:'krishna'}
vijay.update({78:'vijay'})
print(vijay)

#6.pop ()
vijay={1:'viiii',34:'erd',85:'dcsa'}
print(vijay.pop(34))

#7.clear ()
vijay={1:'abhi',78:'bgty'}
vijay.clear()
print(vijay)