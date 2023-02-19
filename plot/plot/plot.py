import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
xx=np.array(2)
yy=np.array(2)
g=0
h=144
file=pd.read_csv('EURUSD240.csv',sep=';')
print(file)
#file.plot(x="<DTYYYYMMDD>",y="<HIGH>",figsize=(100,10))
fig,ax=plt.subplots(figsize=(10,5))
file.plot(x="<DTYYYYMMDD>",y="<HIGH>",ax=ax)
#ax.set_xlim([g,h])
ax.axhline(file["<HIGH>"].iloc[g:h].max(),0.2,0.9)
ax.axhline(file["<HIGH>"].min(),0.2,0.9)
ax.axhline(file["<HIGH>"].mean(),0.2,0.9)
fig.savefig("plte.png")
#print(file["<DTYYYYMMDD>"].dtype)
xxx=file["<DTYYYYMMDD>"].iloc[h]
for m in file["<DTYYYYMMDD>"] :
    print(m)
#for n in xxx :
   # if xxx[m]=
 #   print(xxx[m]=='2')
  #  m=m+1
#print(file["<DTYYYYMMDD>"].iloc[h])
#print(file["<DTYYYYMMDD>"].str.replace('[-\ \:]','').astype(float))
y=file.iloc[144:288,2:3].values
x=np.linspace(0,30,144)
#x=file.iloc[144:288,0:1].values
b=np.array(y.shape)
b=y
a=np.array(x.shape)
a=x
#print(x)
fig ,ax=plt.subplots(figsize=(10,10))
ax.plot(a,b)
ax.set(title="simple plt",
       xlabel="x-axis",
       ylabel="y-axis")
#fig.savefig("plt.png")
#plt.show()
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
def zigzag(CLOSE,A):
    #close
    zig=np.zeros((60000))
    min=CLOSE[0]
    max=CLOSE[0]
    j=0
    m=True
    n=0
    for i in range(len(CLOSE)):
        if(m==True):
            if(CLOSE[i]<min):
                min=CLOSE[i]
                n=i
            if(CLOSE[i]-min>0.002):
                max=CLOSE[i]
                zig[j]=n #min
                j+=1
                m=False
                
        if(m==False):
            if(CLOSE[i]>max):
                max=CLOSE[i]
                n=i
            if(max-CLOSE[i]>0.002):
                min=CLOSE[i]
                zig[j]=n #max
                j+=1
                m=True
    return zig
