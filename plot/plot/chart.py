import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
from month3 import month
import matplotlib.dates as mdates
def plott(HIGH,file,M,v ):
    A=np.zeros((2))
    B=np.zeros((2))
    F=np.zeros((15))
    A=[M[v],M[v+1]]
    max=HIGH[M[v-1].astype(int):M[v].astype(int)].max()
    min=HIGH[M[v-1].astype(int):M[v].astype(int)].min()
    F=[(max+min)/2,(max-min)*0.236,(max-min)*0.382,(max-min)*0.618,(max-min)*1.618,(max-min)*2.618,
    (max-min)*(-0.236),(max-min)*(-0.382),(max-min)*(-0.618),(max-min)*(-1.618),(max-min)*(-2.618)]
    mean=HIGH[M[v-1].astype(int):M[v].astype(int)].mean()
    plt. rcParams. update({'figure.autolayout' : True})
    fig,ax=plt.subplots(figsize=(20,10))
    labels = ax.get_xticklabels()
    plt.setp(labels,rotation=45,horizontalalignment='center')
    ax.set_xlim([M[v-1].astype(int),M[v+1].astype(int)])
    ax.set_ylim(HIGH[M[v-1].astype(int):M[v+1].astype(int)].min(),HIGH[M[v-1].astype(int):M[v+1].astype(int)].max(),'c1')
    file.plot(x="<DTYYYYMMDD>",y="<HIGH>",ax=ax,color='grey')
    file.plot(x="<DTYYYYMMDD>",y="<LOW>",ax=ax,color='r')
    plt.show()
locator=mdates.DayLocator(bymonthday=[1,5,10,15])
formatter=mdates.DateFormatter('%b %d')
plt. style.use(['dark_background'])
file=pd.read_csv('EURUSD240.csv',sep=';')
M=np.zeros((175))
M=month(file["<DTYYYYMMDD>"])
plott(file["<HIGH>"],file,M,173)

#file.axvspan(file.iloc["<DTYYYYMMDD>"][0],file.iloc["<HIGH>"][1], facecolor='g' , alpha=0.5)
#ax.xaxis.set_major_locator(locator)
#ax.xaxis.set_major_formatter(formatter)
#file.plot(x="<DTYYYYMMDD>",y="<HIGH>",ax=ax,color='grey')
#ax.plot(a,b)
#file.plot(x="<DTYYYYMMDD>",y="<HIGH>",ax=ax)
#plt.axvspan(1.25, 1.55, facecolor='g' , alpha=0.5)
#plt.show()
