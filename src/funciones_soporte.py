# En este documento nos encontramos con las funciones creadas para trabajar en el 
# archivo de análisis de presupuestos de Brasil

import pandas as pd
import numpy as np
from pandas.api.types import is_datetime64_any_dtype as is_datetime
import seaborn as sns
import matplotlib.pyplot as plt

def info_df(dataframe):
    """
    Función que devuelve información general sobre el DatFrame que le pasemos.

    Args:
        df (DataFrame): DataFrame con información que queramos revisar

    Returns:
        DataFrame: DataFrame con información general sobre las columnas del DataFrame que se le ha pasado a la función: tipo de datos, número de
        registros, número de valores nulos, porcentaje de los valores nulos sobre el total
    """
    info_df = pd.DataFrame()
    info_df["Tipo_dato"] = dataframe.dtypes
    info_df["numero_registros"] = [dataframe[elemento].value_counts().sum() for elemento in dataframe]
    info_df["Numero_nulos"] = round(dataframe.isnull().sum())
    info_df["%_nulos"] = round((dataframe.isnull().sum()/dataframe.shape[0])*100, 2)

    return info_df

# Para poder realizar el cambio de estas columnas del tipo de dato, anteriormente necesitaremos cambiar las comas por puntos, ya que python
# no reconoce las comas en los números, solo los puntos. Para ello aplicaremos un replace sobre cada uno de los elementos de las columnas, 
# y pediremos que nos modifique las comas por puntos.
def buscar_reemplazar(dataframe, columnas):

    """
    Función que cambia los datos numéricos de una columna de un dataframe, que están en tipo string, y contienen comas. 

    Args:
        dataframe (DataFrame): Dataframe que contiene las columnas a modificar
        columnas (lista de columnas del DataFrame): lista de columnas del DataFrame, de las cuales se quiere realizar el cambio de datos.

    Returns:
        DataFrame: dataframe con las columnas indicadas con los datos numéricos cambiados a tipo float.
    """
    for columna in columnas:
    
        dataframe[columna] = dataframe[columna].str.replace(",", ".").astype(float)

    return dataframe

# Creamos una función que realiza las mismas funciones que el describe, pero con más estadísticos, solo para elementos numéricos
def estadisticos_numericas_df(dataframe, lista_columnas):
    valores_curtosis = []
    valores_asimetria = []
    valores_moda = []
    #creamos un bucle for para calcular los valores de la curtosis y la asimetría
    for columna in lista_columnas:
        if dataframe[columna].dtype == int or dataframe[columna].dtype == float:

            curtosis = round(dataframe[columna].kurtosis(), 2)
            asimetria = round(dataframe[columna].skew(),2)
            moda = dataframe[columna].mode()

            valores_curtosis.append(curtosis)
            valores_asimetria.append(asimetria)
            valores_moda.append(float(moda.iloc[0]))
            
        elif is_datetime(dataframe[columna]):
            valores_curtosis.append(np.nan)
            valores_asimetria.append(np.nan)
            valores_moda.append(float(moda.iloc[0]))
            
    estadísticos_generales = round(dataframe.describe().T, 2)
    estadísticos_generales["Curtosis"] = valores_curtosis
    estadísticos_generales["Coef_asimetria"] = valores_asimetria
    estadísticos_generales["Moda"] = valores_moda

    return estadísticos_generales

