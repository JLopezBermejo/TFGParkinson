import pandas as pd
import os
import sklearn.feature_selection
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn



directory = os.getcwd()
directory = os.path.join(directory, os.pardir)

df = pd.read_csv(directory + '\data\parkinsons.data.txt')

dfNumerico = df
dfNumerico = dfNumerico.drop('name', axis=1)


status = dfNumerico['status']

dfNumerico = dfNumerico.drop('status', axis=1)


columnas = np.array(dfNumerico.columns)


mutualInfo = sklearn.feature_selection.mutual_info_classif(dfNumerico,status)

scores=pd.DataFrame(mutualInfo)

scores = scores.T

scores.columns=columnas

scores.index=['Scores']


if(not os.path.exists(directory+'/plotImages')):
   os.mkdir(directory+'/plotImages')
   if(not os.path.exists(directory + '/plotImages/global')):
        os.mkdir(directory + '/plotImages/global')
   
scores = scores.sort_values(by='Scores',axis=1)
sn.set(rc={'figure.figsize':(40,5)})

sn.scatterplot(data=scores.T)
sn.lineplot(data=scores.T)
plt.savefig(directory + '/plotImages/global/scoresMutualInformation')
plt.close()

if(not os.path.exists(directory+'/stadistics')):
   os.mkdir(directory+'/stadistics')
f = open(directory + '/stadistics/MutualInformation.txt', 'w')
for column in scores.columns:
    f.write('Score de MutualInformation de la columna :' + column + '\n = '+ str(scores[column]))
    f.write('\n')

f.close()




