import pandas as pd
import os
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

directory = os.getcwd()

df = pd.read_csv(directory + '\G05.csv')
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

def printDifSanosEnfermos(df,red):
    for index,row in df.iterrows():
        neurona = row['neurona'] - 1
        neuronaRow = int(neurona / 10)
        neuronaColumn = neurona % 10
        if(row['status'] == 0):
            red[neuronaRow][neuronaColumn] += 1
        else:
            red[neuronaRow][neuronaColumn] -= 1
    neuronaReves = red[::-1]
    neuronaReves = pd.DataFrame(neuronaReves)
    s = sn.heatmap(neuronaReves, annot=True,cmap = 'PiYG',xticklabels = False, yticklabels = False)
    sn.set(rc={'figure.figsize':(10,10)})
    s.set_xlabel('Mapa de Sanos y Enfermos combinado', fontsize=20)
    plt.savefig(directory + '/DifSanosEnfermos')
    plt.close()

def getCoordinateMax(red):
    mejor = 0
    posx = 0
    posy = 0
    for i in range(len(red)):
        for j in range(len(red)):
            if(red[i][j] >= mejor):
                mejor = red[i][j]
                posx = i
                posy = j
    return(posx*10 + posy)    
            
            
    
    
    
    
red = np.zeros((10,10),int)
printSanosOEnfermos(df,0,red)
Neuronaconsanos = getCoordinateMax(red)
print(Neuronaconsanos)
red = np.zeros((10,10),int)
printSanosOEnfermos(df,1,red)
Neuronaconenfermos = getCoordinateMax(red)
print(Neuronaconenfermos)
red = np.zeros((10,10),int)
printDifSanosEnfermos(df,red)

df = pd.read_csv(directory + '\G05Pesos.csv')
df = pd.DataFrame(df)
sn.set(rc={'figure.figsize':(40,5)})
plt.plot(df.iloc[Neuronaconsanos],label='Neurona con mayor número de sanos')
plt.plot(df.iloc[Neuronaconenfermos],label='Neurona con mayor número de enfermos')
plt.legend(loc="upper left")
plt.ylabel('Pesos de las neuronas')
plt.savefig(directory + '/PesosMayorSanosEnfermos')
plt.close()
