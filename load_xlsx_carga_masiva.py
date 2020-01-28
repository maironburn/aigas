from common_config import XLXS_CARGA_MASIVA
import pandas as pd
import numpy as np
import datetime


def convert_to_yyyymmdd(date):
    pass

df = pd.read_excel(XLXS_CARGA_MASIVA)
pandas_row_mapper={0: 'TasaMolecula', 1: 'PrecioFormula', 2 : 'Calendario', 3: 'Prevision',
                 4: 'Nominacion'}

df= df.loc[:8, 'colecciones':'CLI'] # filtro columnas
# Calendario, Nominacion , PrecioFormula, Prevision, TasaMolecula, prices
df= df.rename(index=pandas_row_mapper).replace(np.nan, '', regex=True)
df= df.loc[:, 'From':'CLI']

# 2020-01-01 17:14:45
df['From'] = pd.to_datetime(df.From, format='%Y-%m-%d').apply(lambda x: x.strftime('%Y-%m-%d')).astype(str)
df['To'] = pd.to_datetime(df.To, format='%Y-%m-%d').apply(lambda x: x.strftime('%Y-%m-%d'))
df['From'] = pd.to_datetime(df.From, format='%Y-%m-%d').apply(lambda x: x.strftime('%Y-%m-%d'))
df['FromLastModified'] = pd.to_datetime(df.To, format='%Y-%m-%d').apply(lambda x: x.strftime('%Y-%m-%d'))

df = pd.to_datetime(df.To, format='%d%m%Y')

print("")
