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
#Separación de variables predictoras y target
x = df_ml.drop(columns='abandono')  #Predictoras
y = df_ml['abandono']               #Target

#Separación dataframes train y test
from sklearn.model_selection import train_test_split

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size = 0.3)

##----- Entrenamiento del modelo con train -----##
from sklearn.tree import DecisionTreeClassifier

#Instanciar
ac = DecisionTreeClassifier(max_depth=4)
#Entrenar
ac.fit(train_x,train_y)

##----- Predicción y validación sobre test -----##
# Predicción
pred = ac.predict_proba(test_x)[:, 1]
pred[:20]
# Evaluación
from sklearn.metrics import roc_auc_score
roc_auc_score(test_y,pred)

###----- INTERPRETACIÓN -----###

