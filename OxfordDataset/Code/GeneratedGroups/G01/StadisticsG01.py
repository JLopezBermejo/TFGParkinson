import pandas as pd
import os

directory = os.getcwd()

df = pd.read_csv(directory + '\G01.txt')
df = pd.DataFrame(df)
#total sanos y enfermos
sanos = 0
enfermos = 0
for index, row in df.iterrows():
    if(int(row['status']) == 0):
        sanos += 1
    else:
        enfermos += 1

#Para 2Nclusters

nHitsN2SanosC1 = 0
nHitsN2NoSanosC1 = 0

for index, row in df.iterrows():
    if(row['2Nclusters'] == 1):
        if(int(row['status']) == 0):
            nHitsN2SanosC1 += 1
        else:
            nHitsN2NoSanosC1 += 1
nHitsN2SanosC2 = 0
nHitsN2NoSanosC2 = 0
for index, row in df.iterrows():
    if(row['2Nclusters'] == 2):
        if(int(row['status']) == 0):
            nHitsN2SanosC2 += 1
        else:
            nHitsN2NoSanosC2 += 1
            
print('sanos totales: ' + str(sanos) + ' enfermos totales: ' + str(enfermos))

print('-----------------Porcentaje de aciertos para el 2Nclusters--------------------------------')
print('Aciertos para sanos en el cluster 1: ' + str((nHitsN2SanosC1/(nHitsN2SanosC1 + nHitsN2NoSanosC1))*100) + '% y sobre el total de sanos: '
      + str(100*nHitsN2SanosC1/(sanos)) + '%')


print('Aciertos para enfermos en el cluster 1: ' + str((nHitsN2NoSanosC1/(nHitsN2SanosC1 + nHitsN2NoSanosC1))*100) + '% y sobre el total de enfermos: '
      + str(100*nHitsN2NoSanosC1/(enfermos)) + '%\n')


print('Aciertos para sanos en el cluster 2: ' + str((nHitsN2SanosC2/(nHitsN2SanosC2 + nHitsN2NoSanosC2))*100) + '% y sobre el total de sanos: '
      + str(100*nHitsN2SanosC2/(sanos)) + '%')


print('Aciertos para enfermos en el cluster 2: ' + str((nHitsN2NoSanosC2/(nHitsN2SanosC2 + nHitsN2NoSanosC2))*100) + '% y sobre el total de enfermos: '
      + str(100*nHitsN2NoSanosC2/(enfermos)) + '%\n\n')

print('-----------------Porcentaje de aciertos para el 3Nclusters--------------------------------')

nHitsN2SanosC1 = 0
nHitsN2NoSanosC1 = 0

for index, row in df.iterrows():
    if(row['3Nclusters'] == 1):
        if(int(row['status']) == 0):
            nHitsN2SanosC1 += 1
        else:
            nHitsN2NoSanosC1 += 1
nHitsN2SanosC2 = 0
nHitsN2NoSanosC2 = 0
for index, row in df.iterrows():
    if(row['3Nclusters'] == 2):
        if(int(row['status']) == 0):
            nHitsN2SanosC2 += 1
        else:
            nHitsN2NoSanosC2 += 1

nHitsN2SanosC3 = 0
nHitsN2NoSanosC3 = 0
for index, row in df.iterrows():
    if(row['3Nclusters'] == 3):
        if(int(row['status']) == 0):
            nHitsN2SanosC3 += 1
        else:
            nHitsN2NoSanosC3 += 1

print('Aciertos para sanos en el cluster 1: ' + str((nHitsN2SanosC1/(nHitsN2SanosC1 + nHitsN2NoSanosC1))*100) + '% y sobre el total de sanos: '
      + str(100*nHitsN2SanosC1/(sanos)) + '%')


print('Aciertos para enfermos en el cluster 1: ' + str((nHitsN2NoSanosC1/(nHitsN2SanosC1 + nHitsN2NoSanosC1))*100) + '% y sobre el total de enfermos: '
      + str(100*nHitsN2NoSanosC1/(enfermos)) + '%\n')


print('Aciertos para sanos en el cluster 2: ' + str((nHitsN2SanosC2/(nHitsN2SanosC2 + nHitsN2NoSanosC2))*100) + '% y sobre el total de sanos: '
      + str(100*nHitsN2SanosC2/(sanos)) + '%')


print('Aciertos para enfermos en el cluster 2: ' + str((nHitsN2SanosC2/(nHitsN2SanosC2 + nHitsN2NoSanosC2))*100) + '% y sobre el total de enfermos: '
      + str(100*nHitsN2NoSanosC2/(enfermos)) + '%\n\n')

print('Aciertos para sanos en el cluster 3: ' + str((nHitsN2SanosC3/(nHitsN2SanosC3 + nHitsN2NoSanosC3))*100) + '% y sobre el total de sanos: '
      + str(100*nHitsN2SanosC3/(sanos)) + '%')


print('Aciertos para enfermos en el cluster 3: ' + str((nHitsN2NoSanosC3/(nHitsN2SanosC3 + nHitsN2NoSanosC3))*100) + '% y sobre el total de enfermos: '
      + str(100*nHitsN2NoSanosC3/(enfermos)) + '%\n\n')



print('-----------------Porcentaje de aciertos para el 4Nclusters--------------------------------')

nHitsN2SanosC1 = 0
nHitsN2NoSanosC1 = 0

for index, row in df.iterrows():
    if(row['4Nclusters'] == 1):
        if(int(row['status']) == 0):
            nHitsN2SanosC1 += 1
        else:
            nHitsN2NoSanosC1 += 1
nHitsN2SanosC2 = 0
nHitsN2NoSanosC2 = 0
for index, row in df.iterrows():
    if(row['4Nclusters'] == 2):
        if(int(row['status']) == 0):
            nHitsN2SanosC2 += 1
        else:
            nHitsN2NoSanosC2 += 1

nHitsN2SanosC3 = 0
nHitsN2NoSanosC3 = 0
for index, row in df.iterrows():
    if(row['4Nclusters'] == 3):
        if(int(row['status']) == 0):
            nHitsN2SanosC3 += 1
        else:
            nHitsN2NoSanosC3 += 1


nHitsN2SanosC4 = 0
nHitsN2NoSanosC4 = 0
for index, row in df.iterrows():
    if(row['4Nclusters'] == 4):
        if(int(row['status']) == 0):
            nHitsN2SanosC4 += 1
        else:
            nHitsN2NoSanosC4 += 1

print('Aciertos para sanos en el cluster 1: ' + str((nHitsN2SanosC1/(nHitsN2SanosC1 + nHitsN2NoSanosC1))*100) + '% y sobre el total de sanos: '
      + str(100*nHitsN2SanosC1/(sanos)) + '%')


print('Aciertos para enfermos en el cluster 1: ' + str((nHitsN2NoSanosC1/(nHitsN2SanosC1 + nHitsN2NoSanosC1))*100) + '% y sobre el total de enfermos: '
      + str(100*nHitsN2NoSanosC1/(enfermos)) + '%\n')


print('Aciertos para sanos en el cluster 2: ' + str((nHitsN2SanosC2/(nHitsN2SanosC2 + nHitsN2NoSanosC2))*100) + '% y sobre el total de sanos: '
      + str(100*nHitsN2SanosC2/(sanos)) + '%')


print('Aciertos para enfermos en el cluster 2: ' + str((nHitsN2NoSanosC2/(nHitsN2SanosC2 + nHitsN2NoSanosC2))*100) + '% y sobre el total de enfermos: '
      + str(100*nHitsN2NoSanosC2/(enfermos)) + '%\n\n')

print('Aciertos para sanos en el cluster 3: ' + str((nHitsN2SanosC3/(nHitsN2SanosC3 + nHitsN2NoSanosC3))*100) + '% y sobre el total de sanos: '
      + str(100*nHitsN2SanosC3/(sanos)) + '%')


print('Aciertos para enfermos en el cluster 3: ' + str((nHitsN2NoSanosC3/(nHitsN2SanosC3 + nHitsN2NoSanosC3))*100) + '% y sobre el total de enfermos: '
      + str(100*nHitsN2NoSanosC3/(enfermos)) + '%\n\n')

print('Aciertos para sanos en el cluster 4: ' + str((nHitsN2SanosC4/(nHitsN2SanosC4 + nHitsN2NoSanosC4))*100) + '% y sobre el total de sanos: '
      + str(100*nHitsN2SanosC4/(sanos)) + '%')


print('Aciertos para enfermos en el cluster 3: ' + str((nHitsN2NoSanosC4/(nHitsN2SanosC4 + nHitsN2NoSanosC4))*100) + '% y sobre el total de enfermos: '
      + str(100*nHitsN2NoSanosC4/(enfermos)) + '%\n\n')








