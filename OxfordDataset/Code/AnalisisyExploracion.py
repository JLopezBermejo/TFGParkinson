import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import os
import sklearn.compose
from scipy.stats import kurtosistest




directoryRoot = os.getcwd()
directoryRoot = os.path.join(directoryRoot, os.pardir)
directoryPlot = directoryRoot + '/plotImages'

df = pd.read_csv(directoryRoot + '\data\parkinsons.data.txt')


print('Cantidad de valores nulos o vacíos: ', df.isnull().sum().sum())





dfNumerico = df
dfNumerico = dfNumerico.drop('name', axis=1)


def savePlots(df):
    directory = os.getcwd()
    directory = os.path.join(directory, os.pardir)
    directory += '/plotImages'
    
    if(not os.path.exists(directory)):
        os.mkdir(directory)
        if(not os.path.exists(directory + '/individual')):
            os.mkdir(directory + '/individual')
        if(not os.path.exists(directory + '/global')):
            os.mkdir(directory + '/global')
        
    for column in dfNumerico.columns:

            
        fig,ax= plt.subplots(nrows=1,ncols=2,figsize=(10, 4))
        sn.kdeplot(data=dfNumerico[column],ax=ax[0])
        sn.boxplot(data=dfNumerico[column],ax=ax[1])
        
        if(column.find(':')):
            column = column.replace(':','')
        
        plt.savefig(directory + '/individual/' + column)
        plt.close()
    sn.set(rc={'figure.figsize':(40,9)})
    sn.boxplot(data=df)
    plt.savefig(directory + '/global/globalBoxplot')
    plt.close()
    
savePlots(dfNumerico)  
    
print('\n\nIntroduzca cualquier valor para guardar las estadísticas de los Outliers en el fichero Outliers.txt')
input()
    
    
#Con la siguiente función podremos ver los outliers   
def outliers(column):
    # Rango intercuartil
    iqr = (np.quantile(column, 0.75))-(np.quantile(column, 0.25))
    # Limite superior
    upper_bound = np.quantile(column, 0.75)+(1.5*iqr)
    # Limite inferior
    lower_bound = np.quantile(column, 0.25)-(1.5*iqr)
    outliers = []
    
    # Si algún valor se sale de los límites lo añadimos a outliers
    for value in column:
        if value > upper_bound:
            outliers.append(value)
        elif value < lower_bound:
            outliers.append(value)
    
    pros = len(outliers)/len(column)*100
    strOutliers = 'IQR:' + str(iqr) + '\n' + 'Upper Bound: ' + str(upper_bound) + \
                  '\n' + 'Lower Bound: ' + str(lower_bound) + '\n' + \
                  'percentage outliers: ' + str(pros) + '\n' + 'total outliers: ' \
                  + str(len(outliers)) + '\n\n\n'
    return(strOutliers)



if(not os.path.exists(directoryRoot + '/stadistics')):
    os.mkdir(directoryRoot + '/stadistics')
     
f = open(directoryRoot + '/stadistics/Outliers.txt', 'w')


for column in dfNumerico.columns:
    f.write('Estadísticas de la columna :' + column)
    f.write('\n')
    f.write(outliers(dfNumerico[column]))
    
    
f.close()

print('\n\nIntroduzca cualquier valor para pasar a guardar la matriz de correlacion')
input()


sn.set(rc={'figure.figsize':(18,18)})
correlationMatrix = df.corr().abs()

correlationMatrix06 = correlationMatrix[(correlationMatrix>0.6)]

sn.heatmap(correlationMatrix, annot=True, cmap='Blues')
plt.savefig(directoryPlot + '/global/CorrelationMatrix')
plt.close()

sn.heatmap(correlationMatrix06, annot=True, cmap='Greens')
plt.savefig(directoryPlot + '/global/CorrelationMatrix06')
plt.close()


print('\n\nIntroduzca cualquier valor para estimar la normalidad \
      de cada característica y del Dataset (se almacenará en Kurtosis.txt)')
input()

if(not os.path.exists(directoryRoot)):
   os.mkdir(directoryRoot)
   if(not os.path.exists(directoryRoot + '/stadistics')):
      os.mkdir(directoryRoot + '/stadistics')
f = open(directoryRoot + '/stadistics/Kurtosis.txt', 'w')    

for column in dfNumerico.columns:
    zscore,pvalue = kurtosistest(dfNumerico[column])
    f.write('KurtosisTest de la columna :' + column + '\npvalor= '+ str(pvalue))
    f.write('\n')


zscore,pvalue = kurtosistest(dfNumerico)
f.write('\n\n KurtosisTest del dataset entero: ' + str(pvalue))
    
f.close()  
    
    
    
    
    
print('\n\nIntroduzca cualquier valor para estandarizar los datos y obtener el diagrama de bigotes')
input()



status = dfNumerico['status']

dfNumerico = dfNumerico.drop('status', axis=1)

dfNumerico =pd.concat([pd.DataFrame(dfNumerico), status], axis=1)

transformacion = sklearn.compose.ColumnTransformer(transformers=[
    ('MetodoDeEstandarizacion', sklearn.preprocessing.StandardScaler(), [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]),
    ('passthrough', 'passthrough',[22])
]);





dfScaled = pd.DataFrame(transformacion.fit_transform(dfNumerico), columns=dfNumerico.columns)


if(not os.path.exists(directoryPlot)):
   os.mkdir(directoryPlot)
   if(not os.path.exists(directoryPlot + '/individual')):
        os.mkdir(directoryPlot + '/individual')
   if(not os.path.exists(directoryPlot + '/global')):
        os.mkdir(directoryPlot + '/global')
    
directoryPlot += '/global'


sn.set(rc={'figure.figsize':(40,9)})


sn.boxplot(data=dfScaled)
plt.savefig(directoryPlot + '/globalBoxplotScaled')
plt.close()

sn.set(rc={'figure.figsize':(20,9)})
sn.kdeplot(data=dfScaled)
plt.savefig(directoryPlot + '/globalDistributionPlotScaled')
plt.close()

















