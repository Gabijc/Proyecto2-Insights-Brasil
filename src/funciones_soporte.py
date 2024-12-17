# En este documento nos encontramos con las funciones creadas para trabajar en el 
# archivo de análisis de presupuestos de Brasil

import pandas as pd
import numpy as np

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

# Creamos una función que realiza las mismas funciones que el describe, pero con más estadísticos, solo para elementos numéricos
def estadisticos_numericas_df(dataframe):
    valores_curtosis = []
    valores_asimetria = []
    valores_moda = []
    valores_mediana = []
    #creamos un bucle for para calcular los valores de la curtosis y la asimetría
    for columna in dataframe:
        if dataframe[columna].dtype == "int" or dataframe[columna].dtype == "float":

            moda = round(dataframe[columna].mode(), 2)
            mediana = round(dataframe[columna].median(), 2)
            curtosis = round(dataframe[columna].kurtosis(), 2)
            asimetria = round(dataframe[columna].skew(),2)

            valores_moda.append(moda)
            valores_curtosis.append(curtosis)
            valores_asimetria.append(asimetria)
            valores_mediana.append(mediana)
        else: 
            ...

    estadísticos_generales = round(dataframe.describe().T, 2)
    estadísticos_generales["Mediana"] = valores_mediana
    estadísticos_generales["Moda"] = valores_moda[0]
    estadísticos_generales["Curtosis"] = valores_curtosis
    estadísticos_generales["Coef_asimetria"] = valores_asimetria

    return estadísticos_generales