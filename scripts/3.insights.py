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

### Estrategias asociadas a los insights de abandono:
'''Habíamos visto que los representantes de ventas son el puesto que más se van.
¿Tendría sentido hacer un plan específico para ellos? ¿Cual sería el coste ahorrado si disminuimos la fuga un 30%?
Primero vamos a calcular el % de representantes de ventas que se han ido el año pasado'''

total_repre_pasado = len(df.loc[df.puesto == 'Sales Representative'])
abandonos_repre_pasado = len(df.loc[(df.puesto == 'Sales Representative') & (df.abandono == 1)])
porc_pasado = abandonos_repre_pasado / total_repre_pasado

porc_pasado

### Ahora vamos a estimar cuántos se nos irán este año
total_repre_actual = len(df.loc[(df.puesto == 'Sales Representative') & (df.abandono == 0)])
se_iran = int(total_repre_actual * porc_pasado)

se_iran

### Sobre ellos, cuantos podemos retener (hipótesis 30%) y cuanto dinero puede suponer
retenemos = int(se_iran * 0.3)
ahorramos = df.loc[(df.puesto == 'Sales Representative') & (df.abandono == 0),'impacto_abandono'].sum() * porc_pasado * 0.3

print(f'Podemos retener {retenemos} representantes de ventas y ello supondría ahorrar {ahorramos}$.')

'''Este dato también es muy interesante porque nos permite determinar el presupuesto para acciones
de retención por departamento o perfil.
Ya que sabemos que podemos gastarnos hasta 37.000$ sólo en acciones específicas para retener
a representantes de ventas y se estarían pagando sólas con la pérdida evitada'''