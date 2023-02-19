import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
from month3 import month
def plott(CLOSE,file,M,v,zig ):
    plt. style.use(['dark_background'])
    A=np.zeros((2))
    B=np.zeros((2))
    C=np.zeros((2))
    plt. rcParams. update({'figure.autolayout' : True})
    fig,ax=plt.subplots(figsize=(20,10))
    labels = ax.get_xticklabels()
    plt.setp(labels,rotation=45,horizontalalignment='center')
    ax.set_xlim([M[v-1].astype(int),M[v+1].astype(int)])
    ax.set_ylim(CLOSE[M[v-1].astype(int):M[v+1].astype(int)].min(),CLOSE[M[v-1].astype(int):M[v+1].astype(int)].max(),'c1')
    for i in range (0,100):
        A=[zig[i],zig[i+1]]
        C=[CLOSE[zig[i].astype(int)],CLOSE[zig[i+1].astype(int)]]
        ax.plot(A,C,'--',lw=1,color='grey')
    A=[zig[2],zig[2]]
    ax.plot(A,C,'--',lw=1,color='grey')
    file.plot(x="<DTYYYYMMDD>",y="<HIGH>",ax=ax,color='g')
    file.plot(x="<DTYYYYMMDD>",y="<LOW>",ax=ax,color='r')
    fig.savefig("plte.png")
    plt.show()

def zigzag(CLOSE,A):
    A=A/10000
    zig=np.zeros((60000))
    j=0
    m=True
    n=0
    for i in range(len(CLOSE)):
        if(m==True):
            if(CLOSE[i]<CLOSE[n]):
                n=i
            if(CLOSE[i]-CLOSE[n]>A):
                zig[j]=n #min
                j+=1
                m=False                
        if(m==False):
            if(CLOSE[i]>CLOSE[n]):
                n=i
            if(CLOSE[n]-CLOSE[i]>A):
                zig[j]=n #max
                j+=1
                m=True
    return zig
#from M[v] to M[v+1]

file=pd.read_csv('EURUSD240.csv',sep=';')
M=[]
M=month(file["<DTYYYYMMDD>"])
zig=[]
print(len(zig))
zig=zigzag(file["<CLOSE>"],50)
print(zig[0:1000])
plott(file["<CLOSE>"],file,M,1,zig)
aa=np.zeros((2))

#for i in range(len(zig)):
 #   C=[zig[i],zig[i+1]]
#    ax.plot(A,C,'--',lw=1,color='grey')