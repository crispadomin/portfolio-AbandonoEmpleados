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

'''     Conclusiones:
        * mayor_edad solo tiene un valor --> eliminarla
        * Sobre las imputaciones pendientes de variables categóricas:
            * educacion: imputar por 'Universitaria'
            * satisfaccion_trabajo: imputar por 'Alta'
            * implicacion: imputar por 'Alta'   '''

df.drop(columns = 'mayor_edad', inplace = True)
df['educacion'] = df['educacion'].fillna('Universitaria')
df['satisfaccion_trabajo'] = df['satisfaccion_trabajo'].fillna('Alta')
df['implicacion'] = df['implicacion'].fillna('Alta')

df.head(10)

    ##----- EDA Variables numéricas -----##
def estadisticos_cont(num):
    #Calculamos describe
    estadisticos = num.describe().T
    #Añadimos la mediana
    estadisticos['median'] = num.median()
    #Reordenamos para que la mediana esté al lado de la media
    estadisticos = estadisticos.iloc[:,[0,1,8,2,3,4,5,6,7]]
    #Lo devolvemos
    return(estadisticos)

print(estadisticos_cont(df.select_dtypes('number')))

'''     Conclusiones:
        * Empleados solo tiene un valor --> Eliminarla
        * Sexo tiene 4 valores --> Eliminarla
        * Horas quincena solo tiene una valor --> Eliminarla
        * De los nulos pendientes de imputación que sean numéricas
        solo está el sexo, pero como la vamos a eliminar ya no hay que imputar nada'''

df.drop(columns = ['empleados','sexo','horas_quincena'], inplace = True)
df.info()