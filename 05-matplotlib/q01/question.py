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

data = pd.read_csv('data.csv', sep=',', index_col='Region')

fig, axs = plt.subplots(nrows=1, ncols=6,  figsize=(13,6), dpi =72, sharey=True)
fig.subplots_adjust(hspace=0.1, wspace=0.05)

for x, y  in list(enumerate(data.index)):
  axs[x].scatter(range(3), data.loc[y], color=['tab:orange', 'tab:blue', 'tab:green'], facecolors='none', linewidth = 3, s=200)
  axs[x].set_title(y)
  axs[x].set_xticks(range(3))
  axs[x].set_xticklabels(data.columns, rotation='vertical')
  axs[x].margins(x=0.15, y=0.05) 

axs[0].set_ylabel('Poblacion')
fig.tight_layout()

plt.savefig('generada.png', dpi=72)