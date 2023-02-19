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
i=0
gg=np.zeros((175))
gg[i]=0
for m in range(len(file["<DTYYYYMMDD>"]) ):
    if file["<DTYYYYMMDD>"].iloc[m][6]!=l :
        i=i+1
        print(i)
        print(m)
        #print( file["<DTYYYYMMDD>"].iloc[m])
        l=file["<DTYYYYMMDD>"].iloc[m][6]
        gg[i]=m

print(gg.dtype)
print(len(file["<DTYYYYMMDD>"]))
print(file["<DTYYYYMMDD>"].iloc[gg[174].astype(int)])



def plott(HIGH,M,file,j,n=np.zeros((v)) ):
    A=np.zeros((2))
    B=np.zeros((2))
    C=np.zeros((2))
    a=M[1]/M[174]
    b=M[2]/M[174] #file.plot(x="<DTYYYYMMDD>",y="<HIGH>",figsize=(100,10))
    max=HIGH[M[0].astype(int):M[1].astype(int)].max()
    min=HIGH[M[0].astype(int):M[1].astype(int)].min()
    mean=HIGH[M[0].astype(int):M[1].astype(int)].mean()
    fig,ax=plt.subplots(figsize=(20,10))
    ax.set_xlim([M[1].astype(int),M[2].astype(int)])
    ax.set_ylim(min,max)
    ax.axhline(max,0,1)#gold lines
    ax.axhline(min,0,1)
    ax.axhline((max+min)/2,0,1)
    ax.axhline(min+(max-min)*3/4,0,1)
    ax.axhline(min+(max-min)*1/4,0,1)
    ax.axhline(mean,0,1)
    A=[M[1],M[2]]
    i=0
    while True:
        B=[min+(max-min)*i/4,min+(max-min)*(i-2)/4]
        #C=[max-(max-min)*i/4,max-(max-min)*(i+2)/4]
        # ax.plot(A,C)
        ax.plot(A,B)
        if (HIGH[M[1].astype(int):M[2].astype(int)].max())<(min+(max-min)*(i-2)/4): 
            i=0
            break
        i=i+1
    while True:
        B=[min+(max-min)*i/4,min+(max-min)*(i+2)/4]
        ax.plot(A,B)
        if (HIGH[M[1].astype(int):M[2].astype(int)].max())<(min+(max-min)*(i+2)/4): 
            i=0
            break
        i=i+1
    while True:
        i=i+1
        B=[min-(max-min)*i/4,min-(max-min)*(i-2)/4]
        ax.plot(A,B)
        if (HIGH[M[1].astype(int):M[2].astype(int)].min())>(min-(max-min)*i/4): 
            i=0
            break
    while True:
        i=i+1
        B=[min-(max-min)*i/4,min-(max-min)*(i+2)/4]
        ax.plot(A,B)
        if (HIGH[M[1].astype(int):M[2].astype(int)].min())>(min-(max-min)*i/4): 
            i=0
            break
       
    file.plot(x="<DTYYYYMMDD>",y="<HIGH>",ax=ax)
    fig.savefig("plte.png")
    plt.show()
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


