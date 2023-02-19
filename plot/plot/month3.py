import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
def month(a):
    l=a[0][6]
    i=0
    M=np.zeros((175))
    M[i]=0
    for m in range(len(a)):
        if a[m][6]!=l :#a.iloc
            i=i+1
            l=a[m][6]
            M[i]=m
    return M
def plott(CLOSE,file,M,v ):
    plt. style.use(['dark_background'])
    A=np.zeros((2))
    B=np.zeros((2))
    C=np.zeros((2))
    F=np.zeros((15))
    A=[M[v],M[v+1]]

    max=CLOSE[M[v-1].astype(int):M[v].astype(int)].max()
    min=CLOSE[M[v-1].astype(int):M[v].astype(int)].min()
    F=[0,max-min,(max-min)/2,(max-min)*0.236,(max-min)*0.382,(max-min)*0.618,(max-min)*1.618,(max-min)*2.618,
    (max-min)*(-0.236),(max-min)*(-0.382),(max-min)*(-0.618),(max-min)*(-1.618),(max-min)*(-2.618)]
    mean=CLOSE[M[v-1].astype(int):M[v].astype(int)].mean()
    #mean=HIGH[M[v].astype(int)-77:M[v].astype(int)].mean()
    plt. rcParams. update({'figure.autolayout' : True})
    fig,ax=plt.subplots(figsize=(20,10))
    labels = ax.get_xticklabels()
    plt.setp(labels,rotation=45,horizontalalignment='center')

    ax.set_xlim([M[v-1].astype(int),M[v+1].astype(int)])
    ax.set_ylim(CLOSE[M[v-1].astype(int):M[v+1].astype(int)].min(),CLOSE[M[v-1].astype(int):M[v+1].astype(int)].max(),'c1')
#def fipo
    for f in F:
        C=[min+f,min+f]
        ax.plot(A,C,'--',lw=1,color='grey')
    i=0   
#def gane() :
    while True:
        B=[min+(max-min)*i/4,min+(max-min)*(i-2)/4]
        ax.plot(A,B,'--',lw=1,color='grey')
        if (CLOSE[M[v].astype(int):M[v+1].astype(int)].max())<(min+(max-min)*(i-2)/4): 
            i=0
            break
        i=i+1
    while True:
        B=[min+(max-min)*i/4,min+(max-min)*(i+2)/4]
        ax.plot(A,B,'c1--',lw=1,color='grey')
        if (CLOSE[M[v].astype(int):M[v+1].astype(int)].max())<(min+(max-min)*i/4): 
            i=0
            break
        i=i+1
    while True:
        i=i+1
        B=[min-(max-min)*i/4,min-(max-min)*(i-2)/4]
        ax.plot(A,B,'c1--',lw=1,color='grey')
        if (CLOSE[M[v].astype(int):M[v+1].astype(int)].min())>(min-(max-min)*(i-2)/4): 
            i=0
            break
    while True:
        i=i+1
        B=[min-(max-min)*i/4,min-(max-min)*(i+2)/4]
        ax.plot(A,B,'c1--',lw=1,color='grey')
        if (CLOSE[M[v].astype(int):M[v+1].astype(int)].min())>(min-(max-min)*i/4): 
            i=0
            break
    ma=CLOSE.rolling(20).mean()
    mstd=CLOSE.rolling(20).std()
    ax.plot(ma.index,ma,"b")
    ax.fill_between(mstd.index,ma-2*mstd,ma+2*mstd,color="b",alpha=0.2)
    file.plot(x="<DTYYYYMMDD>",y="<HIGH>",ax=ax,color='g')
    file.plot(x="<DTYYYYMMDD>",y="<LOW>",ax=ax,color='r')
    fig.savefig("plte.png")
    plt.show()
