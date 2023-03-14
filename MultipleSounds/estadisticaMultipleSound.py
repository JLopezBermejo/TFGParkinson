import pandas as pd
import numpy as np
import os


directoryRoot = os.getcwd()
dfTraining = pd.read_csv(directoryRoot + '/train_data.txt')
dfTrainingnumpy = np.array(dfTraining)
print("---------------Training---------------")
print("Filas x Columnas",dfTrainingnumpy.shape)
contEPtraining = 0
contSanostraining = 0
for i in dfTrainingnumpy:
    if(i[28] == 0):
        contSanostraining += 1
    else:
        contEPtraining += 1
print("Num de personas con la EP: ",contEPtraining)
print("Num de personas sanas: ",contSanostraining)

print("---------------Test---------------")

dfTest = pd.read_csv(directoryRoot + '/test_data.txt')
dfTestnumpy = np.array(dfTest)
print("Filas x Columnas",dfTestnumpy.shape)
contEPtest = 0
contSanostest = 0
for i in dfTestnumpy:
    if(i[27] == 0):
        contSanostest += 1
    else:
        contEPtest += 1
print("Num de personas con la EP: ",contEPtest)
print("Num de personas sanas: ",contSanostest)





