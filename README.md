# TFGParkinson :electron:
Este TFG trata de la creación de redes de neuronas de tipo SOM (Self-organizing map) para la búsqueda de biomarcadores de la Enfermedad de Parkinson en la voz. En este repositorio se encuentra el código para la generación de esttadísticas sobre el dataset utilizado y que se puede encontrar en el subdirectorio OxfordDataset. El directorio MultipleSounds consta de un dataset que se desechó como dataset del proyecto, aunque se preserva para la trazabilidad del proyecto.
El código principal de las estadísticas se encuentra en los archivos _AnalisisyExploracion.py_, _FeatureSelection.py_ y _MutualInformationCode.py_, dentro del directorio Code. Estos archivos en Python generan los directorios _plotImages_ (sus subdirectorios y archivos) y _stadistics_. 

En _plotImages_ se encuentran las imágenes de distintos gráficos dobre las características, tanto individuales de cada característica como globales, cada una en su respectivo directorio dentro de _plotImages_.

En _stadistics_ se encuentran algunas estadísticas utilizadas para crear las gráficas encontradas en _plotImages_,y alguna estadística auxiliar más.

La representación gráfica de las redes de neuronas som y el entrenamiento de las mismas se realizará en R, con distintos grupos de características y distintos tamaños de red

\## :white_check_mark: Tecnologías utilizadas

-Python
-R

\##:construction: Issues :construction:

- [x]
- [ ]
- [ ]
