###     BUSINESS ANALYTICS    ###

df.info()

    ##----- Análisis de nulos -----##
df.isna().sum().sort_values(ascending = False)

''' Conclusiones:
    * anos_en_puesto y conciliacion tienen demasiados nulos --> eliminar Variables
    * sexo, educacion, satisfaccion_trabajo e implicacion --> imputarlos tras EDA'''

df.drop(columns = ['anos_en_puesto','conciliacion'], inplace = True)
print(df)