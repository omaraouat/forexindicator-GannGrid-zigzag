import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
xx=np.array(2)
yy=np.array(2)
g=0
h=144
file=pd.read_csv('EURUSD240.csv',sep=';')

l=file["<DTYYYYMMDD>"].iloc[0][6]
print(file["<DTYYYYMMDD>"].iloc[0])
j: int
i=0
j=0
gg=np.zeros((175))
print(gg)
gg[i]=j
for m in range(len(file["<DTYYYYMMDD>"]) ):
    j=j+1
   # if m[6]!=l :
    if file["<DTYYYYMMDD>"].iloc[m][6]!=l :
        i=i+1
        print(i)
        print(m)
        print( file["<DTYYYYMMDD>"].iloc[m])
        l=m[6]
        gg[i]=j
print(gg.dtype)
print(file["<DTYYYYMMDD>"].iloc[gg[2].astype(int)])
#for n in xxx :
   # if xxx[m]=
 #   print(xxx[m]=='2')
  #  m=m+1
y=file.iloc[144:288,2:3].values
x=np.linspace(0,30,144)


'''
a=np.array(144)
xx=np.array(2)
yy=np.array(2)
file= pd.read_csv('EURUSD240.csv',sep='\t')
y=file.iloc[144:288,2:3].values
y2=file.iloc[144:288,2:4].values
b=np.array(y2.shape)
a=y2
b=y2
max=a.max()
min=a.min()
print(max)
print(min)
xx=[file.iloc[1,2],file.iloc[1,2],file.iloc[142,3],file.iloc[142,3]]
yy=np.array([0,30,0,30])
x=np.linspace(0,30,144)
print(xx)
print(yy)
plt.plot(yy,xx)
plt.plot(x,y)
plt.plot()
plt.show()
'''

