###     BUSINESS ANALYTICS    ###

df.info()

    ##----- Análisis de nulos -----##
df.isna().sum().sort_values(ascending = False)

''' Conclusiones:
    * anos_en_puesto y conciliacion tienen demasiados nulos --> eliminar Variables
    * sexo, educacion, satisfaccion_trabajo e implicacion --> imputarlos tras EDA'''

df.drop(columns = ['anos_en_puesto','conciliacion'], inplace = True)
print(df)

    ##----- EDA Variables categóricas -----##
def graficos_eda_categoricos(cat):
    
        # Calculamos el número de filas que necesitamos para la representación
    from math import ceil
    filas = ceil(cat.shape[1] / 2)

        # Definimos el gráfico
    f, ax = plt.subplots(nrows = filas, ncols = 2, figsize = (16, filas * 6))

        # Aplanamos para iterar por el gráfico como si fuera de 1 dimensión en lugar de 2
    ax = ax.flat 

        # Creamos el bucle que va añadiendo gráficos
    for cada, variable in enumerate(cat):
        cat[variable].value_counts().plot.barh(ax = ax[cada])
        ax[cada].set_title(variable, fontsize = 12, fontweight = "bold")
        ax[cada].tick_params(labelsize = 12)

graficos_eda_categoricos(df.select_dtypes('O'))