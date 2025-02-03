###     GENERACIÓN DE INSIGHTS    ###

## Cuantificación del problema: ¿Cual es la tasa de abandono? ##
print(df.abandono.value_counts(normalize = True) * 100)

## ¿Hay un perfil tipo de empleado que deja la empresa? ##
    # Transformar abandono a numérica
df['abandono'] = df.abandono.map({'No':0, 'Yes':1})

    # Analisis por educación
temp = df.groupby('educacion').abandono.mean().sort_values(ascending = False) * 100
temp.plot.bar();

    # Analisis por estado civil
temp = df.groupby('estado_civil').abandono.mean().sort_values(ascending = False) * 100
temp.plot.bar();

    # Analisis por horas extras
temp = df.groupby('horas_extra').abandono.mean().sort_values(ascending = False) * 100
temp.plot.bar();

    # Analisis por puesto
temp = df.groupby('puesto').abandono.mean().sort_values(ascending = False) * 100
temp.plot.bar();

    # Análisis por salario medio
temp = df.groupby('abandono').salario_mes.mean()
temp.plot.bar();

'''     Conclusiones:
        El perfil medio del empleado que deja la empresa es:
            * Bajo nivel educativo
            * Soltero
            * Trabaja en ventas
            * Bajo salario
            * Alta carga de horas extras'''

### ¿Cual es el impacto económico de este problema?

'''Según el estudio "Cost of Turnover" del Center for American Progress:
* El coste de la fuga de los empleados que ganan menos de 30000 es del 16,1% de su salario
* El coste de la fuga de los empleados que ganan entre 30000-50000 es del 19,7% de su salario
* El coste de la fuga de los empleados que ganan entre 50000-75000 es del 20,4% de su salario
* El coste de la fuga de los empleados que ganan más de 75000 es del 21% de su salario'''

# Creamos una nueva variable salario_ano del empleado
df['salario_ano'] = df.salario_mes.transform(lambda x: x*12)
df[['salario_mes','salario_ano']]

# Calculamos el impacto económico de cada empleado si deja la empresa
# Lista de condiciones
condiciones = [(df['salario_ano'] <= 30000),
               (df['salario_ano'] > 30000) & (df['salario_ano'] <= 50000),
               (df['salario_ano'] > 50000) & (df['salario_ano'] <= 75000),
               (df['salario_ano'] > 75000)]

# Lista de resultados
resultados = [df.salario_ano * 0.161, df.salario_ano * 0.197, df.salario_ano * 0.204, df.salario_ano * 0.21]
                
# Aplicamos select
df['impacto_abandono'] = np.select(condiciones,resultados, default = -999)

print(df)

### ¿Cúanto nos ha costado este problema en el último año?
coste_total =  df.loc[df.abandono == 1].impacto_abandono.sum()
print('Coste abandono último año: ', coste_total, '$', sep='')

### ¿Cuanto nos cuesta que los empleados no estén motivados? (pérdidas en implicación == Baja)
print('Coste falta motivación: ',df.loc[(df.abandono == 1) & (df.implicacion == 'Baja')].impacto_abandono.sum(),'$', sep='')

### ¿Cuanto dinero podríamos ahorrar fidelizando mejor a nuestros empleados?
print(f"Reducir un 10% la fuga de empleados nos ahorraría {int(coste_total * 0.1)}$ cada año.")
print(f"Reducir un 20% la fuga de empleados nos ahorraría {int(coste_total * 0.2)}$ cada año.")
print(f"Reducir un 30% la fuga de empleados nos ahorraría {int(coste_total * 0.3)}$ cada año.")