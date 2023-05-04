import pandas as pd
import sklearn.compose
import sklearn.feature_selection

sourceDirectory = 'D:\TFGParkinson\OxfordDataset'

df = pd.read_csv(sourceDirectory + '\data\parkinsons.data.txt')



nameStatus = pd.concat([df['name'],df['status']],axis=1)

status = df['status']
df = df.drop('name', axis=1)
df = df.drop('status', axis=1)


transformacion = sklearn.compose.ColumnTransformer(transformers=[
    ('MetodoDeEstandarizacion', sklearn.preprocessing.MinMaxScaler(), [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])
]);

trainedModel = transformacion.fit_transform(df)

dfScaled = pd.DataFrame(trainedModel, columns=df.columns)

mutualInfo = sklearn.feature_selection.mutual_info_classif(dfScaled,status)

totalMutualInfo = sum(mutualInfo)

for i in range(mutualInfo.size):
    mutualInfo[i] = mutualInfo[i] / totalMutualInfo

for i in range(len(trainedModel) - 1):
    for j in range(len(trainedModel[0]) - 1):
        trainedModel[i][j] = trainedModel[i][j] * mutualInfo[j]
        
dfScaled = pd.DataFrame(trainedModel, columns=df.columns)
dfFinal = pd.concat([dfScaled,nameStatus],axis=1)

dfFinal.to_csv('G13_MI_22_10x10.csv', index=False)







