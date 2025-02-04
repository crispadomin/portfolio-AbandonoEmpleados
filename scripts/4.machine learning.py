### MODELO DE MACHINE LEARNING ###

df_ml = df.copy()
df_ml.info()

##----- Preparación de los datos para la modelización -----##
#--- Transformar todas las variables categóricas a númericas ---#

from sklearn.preprocessing import OneHotEncoder
#Categóricas
cat = df_ml.select_dtypes('O')
#Instanciamos
ohe = OneHotEncoder(sparse = False)
#Entrenamos
ohe.fit(cat)
#Aplicamos
cat_ohe = ohe.transform(cat)
#Ponemos los nombres
cat_ohe = pd.DataFrame(cat_ohe, columns = ohe.get_feature_names_out(input_features = cat.columns)).reset_index(drop = True)

print(cat_ohe)

#--- Dataframe final ---#
#Seleccionamos las variables numéricas para poder juntarlas a las cat_hoe
num = df.select_dtypes('number').reset_index(drop = True)
#Las juntamos todas en el dataframe final
df_ml = pd.concat([cat_ohe,num], axis = 1)
print(df_ml)


##----- Diseño de la modelización -----##
