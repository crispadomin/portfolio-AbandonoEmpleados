### CONFIGURACIÓN DEL ENTORNO ###

    ## Carga de librerías
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

    ## Carga de datos
ruta_csv = r'../data/AbandonoEmpleados.csv'
df = pd.read_csv(ruta_csv, sep = ';', index_col= 'id', na_values='#N/D')
print(df)