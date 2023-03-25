import pandas as pd
import sklearn.compose

sourceDirectory = 'D:\TFGParkinson\OxfordDataset'

df = pd.read_csv(sourceDirectory + '\data\parkinsons.data.txt')



nameStatus = pd.concat([df['name'],df['status']],axis=1)

df = df.drop('name', axis=1)
df = df.drop('status', axis=1)
df = df.drop('MDVP:Jitter(%)', axis=1)
df = df.drop('MDVP:RAP', axis=1)
df = df.drop('Jitter:DDP', axis=1)
df = df.drop('DFA', axis=1)
df = df.drop('NHR', axis=1)
df = df.drop('MDVP:Fhi(Hz)', axis=1)

print()
transformacion = sklearn.compose.ColumnTransformer(transformers=[
    ('MetodoDeEstandarizacion', sklearn.preprocessing.StandardScaler(), [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
]);


dfScaled = pd.DataFrame(transformacion.fit_transform(df), columns=df.columns)

dfFinal = pd.concat([dfScaled,nameStatus],axis=1)

dfFinal.to_csv('G03_SF_16_10x10.csv', index=False)







