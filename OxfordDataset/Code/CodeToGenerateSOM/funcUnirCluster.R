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