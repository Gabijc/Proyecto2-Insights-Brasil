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

# Creamos una función que nos permite ir accediendo a las categorías económicas con sus valores de ingresos. Será aplicable a los ministerios también
def info_cat(dataframe, categoria):

    ingresos_categoria = dataframe.groupby(categoria)[["VALOR PREVISTO ATUALIZADO", "VALOR LANÇADO","VALOR REALIZADO"]].sum().round(2)
    ingresos_categoria["porcentaje recaudado"] = round((ingresos_categoria["VALOR REALIZADO"]/ingresos_categoria["VALOR PREVISTO ATUALIZADO"])* 100, 2).replace([np.inf, -np.inf, np.nan], "Previsión de 0")
    ingresos_categoria["diferencia_recaudacion"] = round(ingresos_categoria["VALOR REALIZADO"]-ingresos_categoria["VALOR LANÇADO"], 2)

    return ingresos_categoria

# Función que nos devuelve información sobre un ministerio en concreto
def info_ministerio(dataframe, ministerio):

    info_min = dataframe[dataframe["NOME ÓRGÃO SUPERIOR"] == ministerio]

    print(f"Los órganos de los que se compone el {ministerio} son: {info_min["NOME ÓRGÃO"].unique()}")
    print(f"Las unidades gestoras que componen los órganos del {ministerio} son: {info_min["NOME UNIDADE GESTORA"].unique()}")
    print(f"Los ingresos entre 2013 y 2025 del {ministerio} se ")
    return fs.info_cat(info_min, "NOME ÓRGÃO SUPERIOR")

# Función para gráficas temporales que comparan dos variables
def evolucion_temporal(dataframe, eje_x, ejes_y):
    sns.lineplot(x = eje_x, 
             y = ejes_y[0],
             data = dataframe, 
             color = "navy")
    sns.lineplot(x = eje_x, 
             y = ejes_y[1],
             data = dataframe, 
             color = "crimson")

    plt.title(input("Qué nombre quieres ponerle al gráfico: "))
    plt.xlabel(eje_x)
    plt.ylabel(input("Qué nombre tiene el eje y: "))
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["top"].set_visible(False) 

# Función para representar los estadísticos de variables numéricas
def graficos_estadisticos(dataframe, columna):
    fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (20, 5))

    sns.boxplot(x = columna, 
            data = dataframe, 
            color ="violet", 
            ax = axes[0])

    axes[0].set_title(input("Nombre del diagrama de caja: "))
    axes[0].set_ylabel(columna)
    axes[0].spines["right"].set_visible(False)
    axes[0].spines["top"].set_visible(False) 
    axes[0].ticklabel_format(style='plain', axis='x')
    sns.violinplot(x = columna, 
             data = dataframe, 
             color = "olivedrab",
             ax = axes[1])


    axes[1].set_title(input("Nombre del diagrama de violin: "))
    axes[1].set_ylabel(columna)
    axes[1].spines["right"].set_visible(False)
    axes[1].spines["top"].set_visible(False) 
    axes[1].ticklabel_format(style='plain', axis='x')