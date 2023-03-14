from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import sklearn.compose
import os



directory = os.getcwd()
directory = os.path.join(directory, os.pardir)


df = pd.read_csv(directory + '\data\parkinsons.data.txt')




dfNumerico = df
dfNumerico = dfNumerico.drop('name', axis=1)


status = dfNumerico['status']

dfNumerico = dfNumerico.drop('status', axis=1)



transformacion = sklearn.compose.ColumnTransformer(transformers=[
    ('MetodoDeEstandarizacion', sklearn.preprocessing.StandardScaler(), [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])
]);


dfScaled = pd.DataFrame(transformacion.fit_transform(dfNumerico), columns=dfNumerico.columns)


featureselection = SelectKBest(f_classif, k=len(dfScaled.columns))

dfFeatureSelection = featureselection.fit_transform(dfScaled, status)

columnas = np.array(dfNumerico.columns)

scores=pd.DataFrame(featureselection.scores_).T

scores.columns=columnas

scores.index=['Scores']





if(not os.path.exists(directory+'/plotImages')):
   os.mkdir(directory+'/plotImages')
   if(not os.path.exists(directory+'/stadistics')):
        os.mkdir(directory + '/stadistics')
   if(not os.path.exists(directory + '/plotImages/global')):
        os.mkdir(directory + '/plotImages/global')
        
scores = scores.sort_values(by='Scores',axis=1)

sn.set(rc={'figure.figsize':(40,5)})

sn.scatterplot(data=scores.T)
sn.lineplot(data=scores.T)
plt.savefig(directory + '/plotImages/global/scoresFeatureSelection')
plt.close()

f = open(directory + '/stadistics/FeatureSelection.txt', 'w')
for column in scores.columns:
    f.write('Score de FeatureSelection de la columna :' + column + '\npvalor= '+ str(scores[column]))
    f.write('\n')

f.close()


