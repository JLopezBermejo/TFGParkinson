#ESTE ENTRENAMIENTO ES IGUAL AL DEL EXPERIMENTO 10 RESPECTO TANTO A LOS PARAMETROS COMO AL GRUPO
#DE CARACTERISTICAS PERO CON UNA RED 10X10



#cargamos los packetes
library(kohonen)
library(dplyr)
library(aweSOM)


#primeramente ir al directorio con los datos
directory <- paste(dirname(getwd()),'/GeneratedGroups',sep='')

directory <- paste(directory,'/G11/G11_SF_14_8x8.csv',sep='') 
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

G11SOM <- som(dfScaled, grid = somgrid(8,8,"hexagonal"), rlen = 1000, init = redInit)

#representamos la red

purple.fade <- function(n){
  return(rgb(0,0,0.2,alpha=seq(0,1,1/n)))}
plot(G11SOM, type="count", shape = "straight", palette.name = purple.fade)

plot(G11SOM, type="dist.neighbours", shape = "straight")

plot(G11SOM, shape = "straight")

#Vemos que clusters ha creado la red
distancesSOM <- dist(getCodes(G11SOM,1))
cluster <- hclust(distancesSOM)
plot(cluster,hang=-1,labels=F)


#ahora probamos que secciones crea para 2, 3 y 4 clusters
cluster2 <- cutree(cluster, k=2)
cluster3 <- cutree(cluster, k=3)
cluster4 <- cutree(cluster, k=4)

#representamos cada uno de ellos para estudiar si existen diferencias a la hora de hacer grupos

plot(G11SOM,type="mapping",bgcol=c("steelblue1","sienna1")[cluster2], shape = "straight")

plot(G11SOM,type="mapping",bgcol=c("steelblue1","sienna1","yellowgreen")[cluster3], shape = "straight")

plot(G11SOM,type="mapping",bgcol=c("steelblue1","sienna1","yellowgreen","red")[cluster4], shape = "straight")

#procedemos a representar los valores de los pesos por cada feature, por que si se intentan representar juntos no se entiende bien el grafismo

for (j in 1:ncol(df)){
  plot(G11SOM,type="property",property=getCodes(G11SOM,1)[,j], palette.name=purple.fade,main=colnames(df)[j],cex=0.5, shape = "straight")
}

#volvemos a juntar las variables de name y status junto a que neurona ha sido asignada dicho registro
aux <- cbind(name,G11SOM$unit.classif)
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

file <- paste(dirname(getwd()),'/GeneratedGroups/G11/G11.csv',sep='')
write.csv(unionClusters, file,row.names=FALSE,)
pesosSanosEnfermos <- getCodes(G11SOM)
file <- paste(dirname(getwd()),'/GeneratedGroups/G11/G11Pesos.csv',sep='')
write.csv(pesosSanosEnfermos, file,row.names=FALSE,)