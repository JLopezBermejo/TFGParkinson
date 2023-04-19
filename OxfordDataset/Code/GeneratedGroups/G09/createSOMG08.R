#ESTE ENTRENAMIENTO CAMBIA LAS CARACTERÍSTICAS QUE SE USAN PARA ENTRENAR, EN ESTE CASO PASAN A SER SOLO 12,
#SIENDO ESTAS LAS QUE MÁS DISTANTES SE ENCUENTRAN SUS PESOS EN LAS NEURONAS CON MÁS PERSONAS SANAS
#Y MAS PERSONAS ENFERMAS. LOS VALORES DE LOS PARÁMETROS SE MANTENDRAN POR DEFECTO PARA, POSTERIORMENTE,
#PODER IR MODIFICANDOLOS PROGRESIVAMENTE E IR BUSCANDO MEJORES RESULTADOS



#cargamos los packetes
library(kohonen)
library(dplyr)
library(aweSOM)


#primeramente ir al directorio con los datos
directory <- paste(dirname(getwd()),'/GeneratedGroups',sep='')

directory <- paste(directory,'/G09/G09_SC_12_10x10.csv',sep='') 
#dependiendo de que grupo queramos utilizar cambiamos el comando anterior al grupo elegido

df <- read.csv(directory)

status <- df$status
name <- df$name

df <- select(df,-name)
df <- select(df,-status)

set.seed(23)

#se utiliza scale() para poder dimensionar bien el dataset y poder entrenar

dfScaled <- scale(df,center=T,scale=T)

#inicializamos la red con la que entrenaremos

redInit <- somInit(dfScaled,8,8,"random")

#ahora entrenamos la red

G09SOM <- som(dfScaled, grid = somgrid(8,8,"hexagonal"), rlen = 1000, init = redInit)

#representamos la red

purple.fade <- function(n){
  return(rgb(0,0,0.2,alpha=seq(0,1,1/n)))}
plot(G09SOM, type="count", shape = "straight", palette.name = purple.fade)

plot(G09SOM, type="dist.neighbours", shape = "straight")

plot(G09SOM, shape = "straight")

#Vemos que clusters ha creado la red
distancesSOM <- dist(getCodes(G09SOM,1))
cluster <- hclust(distancesSOM)
plot(cluster,hang=-1,labels=F)


#ahora probamos que secciones crea para 2, 3 y 4 clusters
cluster2 <- cutree(cluster, k=2)
cluster3 <- cutree(cluster, k=3)
cluster4 <- cutree(cluster, k=4)

#representamos cada uno de ellos para estudiar si existen diferencias a la hora de hacer grupos

plot(G09SOM,type="mapping",bgcol=c("steelblue1","sienna1")[cluster2], shape = "straight")

plot(G09SOM,type="mapping",bgcol=c("steelblue1","sienna1","yellowgreen")[cluster3], shape = "straight")

plot(G09SOM,type="mapping",bgcol=c("steelblue1","sienna1","yellowgreen","red")[cluster4], shape = "straight")

#procedemos a representar los valores de los pesos por cada feature, por que si se intentan representar juntos no se entiende bien el grafismo

for (j in 1:ncol(df)){
  plot(G09SOM,type="property",property=getCodes(G09SOM,1)[,j], palette.name=purple.fade,main=colnames(df)[j],cex=0.5, shape = "straight")
}

#volvemos a juntar las variables de name y status junto a que neurona ha sido asignada dicho registro
aux <- cbind(name,G09SOM$unit.classif)
aux <- cbind(aux,status)

#le asignamos un nombre a la columna de la neurona
colnames(aux) <- c('name','neurona','status') 

#creamos los datasets con los que trabajaremos para que resulte mas sencillo


datasetaux=as.data.frame(aux)
datasetcluster2aux=as.data.frame(cluster2)
datasetcluster3aux=as.data.frame(cluster3)
datasetcluster4aux=as.data.frame(cluster4)


# y una función que opere sobre los dataset y una los grupos con los datos

unirCluster <- function(dfAUnir,gruposCluster,nClusters){
  result <- dfAUnir
  nameVar <- paste(nClusters,'Nclusters',sep='')
  result[nameVar] <- NA
  for (row in 1:nrow(dfAUnir)){
    neur <- dfAUnir[row,'neurona']
    neur <- strtoi(neur)
    group <- gruposCluster[neur,1]
    result[row,nameVar] <- group
  }
  
  return(result)
}

#ahora unimos los 3 clusters al dataset formado anteriormente

unionClusters <- unirCluster(datasetaux,datasetcluster2aux,2)
unionClusters <- unirCluster(unionClusters,datasetcluster3aux,3)
unionClusters <- unirCluster(unionClusters,datasetcluster4aux,4)

#lo exportamos al directorio correspondiente

file <- paste(dirname(getwd()),'/GeneratedGroups/G09/G09.csv',sep='')
write.csv(unionClusters, file,row.names=FALSE,)
pesosSanosEnfermos <- getCodes(G09SOM)
file <- paste(dirname(getwd()),'/GeneratedGroups/G09/G09Pesos.csv',sep='')
write.csv(pesosSanosEnfermos, file,row.names=FALSE,)