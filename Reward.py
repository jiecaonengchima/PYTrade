duoshao=int(input("plz input the price of this month:"))
zjj=0
x100=0
x60=0
x40=0
x20=0
x10=0
x0=0

if duoshao>1000000:
 x100=(duoshao-1000000)*0.01
 x60=400000*0.015
 x40=200000*0.03
 x20=200000*0.05
 x10=100000*0.075
 x0=100000*0.1
 zjj=x100+x60+x40+x20+x10+x0
 print(x100,'\n',x60,'\n',x40,'\n',x20,'\n',x10,'\n',x0,'\n',zjj)
elif (duoshao<=1000000) and (duoshao>600000):
 x60=(duoshao-600000)*0.015
 x40=200000*0.03
 x20=200000*0.05
 x10=100000*0.075
 x0=100000*0.1
 zjj=x60+x40+x20+x10+x0
 print(x60,'\n',x40,'\n',x20,'\n',x10,'\n',x0,'\n',zjj)
elif (duoshao<=600000) and (duoshao>400000):
 x40=(duoshao-400000)*0.03
 x20=200000*0.05
 x10=100000*0.075
 x0=100000*0.1
 zjj=x40+x20+x10+x0
 print(x40,'\n',x20,'\n',x10,'\n',x0,'\n',zjj)
elif (duoshao<=400000) and (duoshao>200000):
 x20=(duoshao-200000)*0.05
 x10=100000*0.075
 x0=100000*0.1
 zjj=x20+x10+x0
 print(x20,'\n',x10,'\n',x0,'\n',zjj)
elif (duoshao<=200000) and (duoshao>100000):
 x10=(duoshao-100000)*0.075
 x0=100000*0.1
 zjj=x10+x0
 print(x10,'\n',x0,'\n',zjj)
elif duoshao<=100000:
 x0=100000*0.1
 zjj=x0
 print(x0,'\n',zjj)