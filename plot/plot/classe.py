import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
class classe :
    max=0
    min=0
    fig,ax=plt.subplots(figsize=(20,10))
    def __init__(self,date,CLOSE,file,v ):
        self.A=np.zeros((2))
        B=np.zeros((2))    
        self.F=np.zeros((15))
        self.M=np.zeros((175))
        self.date=date
        self.CLOSE=CLOSE
        self.file=file
        self.v=v
        l=date[0][6]
        i=0    
        self.M[i]=0
        for m in range(len(date)):
            if date[m][6]!=l :#a.iloc
                i=i+1
                l=date[m][6]
                self.M[i]=m
        classe.max=CLOSE[self.M[v-1].astype(int):self.M[v].astype(int)].max()
        classe.min=CLOSE[self.M[v-1].astype(int):self.M[v].astype(int)].min()
        self.F=[0,classe.max-classe.min,(classe.max-classe.min)/2,(classe.max-classe.min)*0.236,(classe.max-classe.min)*0.382,(classe.max-classe.min)*0.618,(classe.max-classe.min)*1.618,(classe.max-classe.min)*2.618,
        (classe.max-classe.min)*(-0.236),(classe.max-classe.min)*(-0.382),(classe.max-classe.min)*(-0.618),(classe.max-classe.min)*(-1.618),(classe.max-classe.min)*(-2.618)]
        mean=CLOSE[self.M[v-1].astype(int):self.M[v].astype(int)].mean()
    
    def plott(self):
        M=self.M       
        print("hello")
        print(M)
        plt.style.use(['dark_background'])      
        labels = self.ax.get_xticklabels()
        plt.setp(labels,rotation=45,horizontalalignment='center')    
        classe.ax.set_xlim([M[self.v-1].astype(int),M[self.v+1].astype(int)])
        classe.ax.set_ylim(self.CLOSE[M[self.v-1].astype(int):M[self.v+1].astype(int)].min(),self.CLOSE[M[self.v-1].astype(int):M[self.v+1].astype(int)].max(),'c1')
        print(classe.max)
        print(classe.min)
        self.file.plot(x="<DTYYYYMMDD>",y="<HIGH>",ax=classe.ax,color='g')
        self.file.plot(x="<DTYYYYMMDD>",y="<LOW>",ax=classe.ax,color='r')
        classe.fig.savefig("plte.png")
        plt.show()
    def fipo(self):
        C=np.zeros((2))
        for f in self.F:
            C=[classe.min+f,classe.min+f]
            self.ax.plot(self.A,C,'--',lw=1,color='grey')

   # def  __init__(self, *args, **kwargs):
    #return super().__init__(*args, **kwargs)
file=pd.read_csv('EURUSD240.csv',sep=';')
c=classe(file["<DTYYYYMMDD>"],file["<CLOSE>"],file,171)
c.plott()
#c.fipo()