import pandas as pd
import os
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

directory = os.getcwd()

df = pd.read_csv(directory + '\G03.txt')
df = pd.DataFrame(df)



def printSanosOEnfermos(df,sano,red):
    for index,row in df.iterrows():
        if(row['status'] == sano):
            aux = row['neurona'] - 1
            neuronaRow = int(aux / 10)
            neuronaColumn = aux % 10
            red[neuronaRow][neuronaColumn] += 1

    neuronaReves = red[::-1]
    neuronaReves = pd.DataFrame(neuronaReves)
    sn.set(rc={'figure.figsize':(10,10)})
    color = ''
    if (sano == 0):
        color = 'OrRd'
    else:
        color = 'RdPu'
    s = sn.heatmap(neuronaReves, annot=True, cmap=color,xticklabels = False, yticklabels = False)
    if(sano == 0):
        s.set_xlabel('Mapa de Sanos', fontsize=20)
        plt.savefig(directory + '/MapaSanos')
    else:
        s.set_xlabel('Mapa de Enfermos', fontsize=20)
    plt.savefig(directory + '/MapaEnfermos')
    plt.close()


red = np.zeros((10,10),int)
printSanosOEnfermos(df,0,red)
red = np.zeros((10,10),int)
printSanosOEnfermos(df,1,red)
