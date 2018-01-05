z=int(input('plz input a number for starting(1-50):'))
if z>50 or z<1:
 print('you entered the wrong number!restart!')
 exit()
zz=int(input('plz input a number for ending:(1-50)'))
if zz>50 or z<1:
 print('you entered the wrong number!restart!')
 exit()
jb=input('plz input something:')
g=zz-1
ln=zz-z+1
while z<=zz:
	lns=z*2-1
	print(' '*(g),end=jb*lns)
	print()
	g=g-1
	z=z+1
input('Press [Enter] Plz')