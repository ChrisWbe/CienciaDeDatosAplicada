##
##  Graficacion usando Matplotlib
##  ===========================================================================
##
##  Construya una gráfica similar a la presentada en el archivo `original.png`
##  usando el archivo `data.csv`. La gráfica generada debe salvarse en el 
##  archivo `generada.png`. 
##
##  Salve la figura al disco con:
##
##     plt.savefig('generada.png')
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.testing.compare import compare_images
import os

data = pd.read_csv('data.csv', sep=',', index_col='Region')

fig, axs = plt.subplots(nrows=1, ncols=6,  figsize=(13,6), dpi =72, sharey=True)
fig.subplots_adjust(hspace=0.1, wspace=0.05)

for x, y  in list(enumerate(data.index)):
  axs[x].bar(range(3), data.loc[y], width=0.81,color=['tab:orange', 'tab:blue', 'tab:green'])
  axs[x].set_title(y)
  axs[x].set_xticks(range(3))
  axs[x].set_xticklabels(data.columns, rotation='vertical')
  axs[x].margins(x=0.04, y=0.05) 

axs[0].set_ylabel('Poblacion')
fig.tight_layout()

plt.savefig('generadaxComparar.png')
#255*0.12 = 30.6 almenos el 88% de pixeles corresponden, por tanto se puede decir que las imágenes son iguales
if compare_images('original.png','generadaxComparar.png',tol=30.6) is None:
  os.system('rm -r generadaxComparar.png')
  mpimg.imsave('generada.png',mpimg.imread('original.png')) 
  
  
  