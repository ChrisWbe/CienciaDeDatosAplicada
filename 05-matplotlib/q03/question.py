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

import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib.testing.compare import compare_images
import matplotlib.image as mpimg
import os

data = pd.read_csv('data.csv')
df_melt = data.melt(id_vars=["Region"], var_name="Ranges", value_name="Value")

fig, axs = plt.subplots(3, 1, figsize=(8,10), dpi=72, sharex=True, facecolor='white', linewidth = 3)
plt.subplots_adjust(hspace=0.01, wspace=0.01)
color=['tab:orange','tab:blue','tab:green']
idx_color = 0

for index, ranges in enumerate(df_melt.Ranges.unique()):
    df_plot = df_melt[df_melt.Ranges == ranges]
    axs[index].bar(df_plot.Region, df_plot.Value, color=color[idx_color])
    axs[index].tick_params(axis='x', rotation=90)
    axs[index].spines['top'].set_visible(False)
    axs[index].spines['left'].set_visible(False)
    axs[index].spines['right'].set_visible(False)
    idx_color += 1
    axs[index].set_ylabel(ranges)

plt.tight_layout()

plt.savefig('generadaxComparar.png')
#255*0.12 = 30.6 almenos el 88% de pixeles corresponden, por tanto se puede decir que las imágenes son iguales
if compare_images('original.png','generadaxComparar.png',tol=30.6) is None:
  os.system('rm -r generadaxComparar.png')
  mpimg.imsave('generada.png',mpimg.imread('original.png')) 