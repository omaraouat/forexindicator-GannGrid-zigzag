import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
from month3 import month,plott
file=pd.read_csv('EURUSD240.csv',sep=';')
M=np.zeros((175))
#zig=np.zeros((60000))
M=month(file["<DTYYYYMMDD>"])
#print(file["<DTYYYYMMDD>"][M[0].astype(int)])

plott(file["<CLOSE>"],file,M,173)
#print(file["<HIGH>"][M[1].astype(int):M[2].astype(int)].max())
#zig=zigzag(file["<HIGH>"],file["<LOW>"],22)