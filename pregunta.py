"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #
    df = df.iloc[:,1:]
    df = df.dropna()

    df.sexo = df.sexo.str.lower()

    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()

    df.idea_negocio = df.idea_negocio.str.lower()
    df.idea_negocio = df.idea_negocio.str.replace("-"," ")
    df.idea_negocio = df.idea_negocio.str.replace("_"," ")
    df.idea_negocio = df.idea_negocio.str.strip()

    df.barrio = df.barrio.str.lower()
    df.barrio = df.barrio.str.strip()
    df.barrio = df.barrio.str.strip()
    df.barrio = df.barrio.str.strip()
    df.barrio = df.barrio.str.replace("_"," ")
    df.barrio = df.barrio.str.replace("-"," ")
    df.barrio = df.barrio.str.replace('santo domingo savio ','santo domingo savio')

    df.monto_del_credito = df.monto_del_credito.str.strip("$")
    df.monto_del_credito = df.monto_del_credito.str.strip()
    df.monto_del_credito = df.monto_del_credito.str.replace(",","")
    df.monto_del_credito = df.monto_del_credito.astype('float64')

    df.línea_credito = df.línea_credito.str.lower()
    df.línea_credito = df.línea_credito.str.replace("-"," ")
    df.línea_credito = df.línea_credito.str.replace("_"," ")
    df.línea_credito = df.línea_credito.str.strip()

    df.fecha_de_beneficio = df.fecha_de_beneficio.map(lambda x: x[5:9]+"/"+x[2:4]+"/"+ x[0] if x[1] == "/" else x)
    df.fecha_de_beneficio = df.fecha_de_beneficio.map(lambda x: x[6:10]+"/"+x[3:5]+"/"+ x[0:2] if x[2] == "/" else x)
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio,infer_datetime_format = True, errors = "coerce")

    df = df[~df.duplicated()]

    return df
