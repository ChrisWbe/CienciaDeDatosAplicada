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

fig.savefig("generada.png", dpi=72)