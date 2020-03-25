import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime 
from datetime import date
import re # regular expression per splittare la data (str) 
from collections import defaultdict


def prepare_dataset(df, class_name):
    df = remove_missing_values(df)
    
    
    numeric_columns = get_numeric_columns(df)
    rdf = df.copy(deep=True)
    df, feature_names, class_values = one_hot_encoding(df, class_name)
    real_feature_names = get_real_feature_names(rdf, numeric_columns, class_name)
    rdf = rdf[real_feature_names + (class_values if isinstance(class_name, list) else [class_name])]
    features_map = get_features_map(feature_names, real_feature_names)
    df['Week_day'] = df.date.apply(convert_date) #inseriamo nuova linea di codice per creare Week_day
    df.drop(['date'], inplace=True, axis=1)


    return df, feature_names, class_values, numeric_columns, rdf, real_feature_names, features_map

def remove_missing_values(df):
    for column_name, nbr_missing in df.isna().sum().to_dict().items():
        if nbr_missing > 0:
            if column_name in df._get_numeric_data().columns:
                mean = df[column_name].mean()
                df[column_name].fillna(mean, inplace=True)
            else:
                mode = df[column_name].mode().values[0]
                df[column_name].fillna(mode, inplace=True)
    return df

def get_numeric_columns(df):
    numeric_columns = list(df._get_numeric_data().columns)
    return numeric_columns

def get_real_feature_names(rdf, numeric_columns, class_name):
    real_feature_names = [c for c in rdf.columns if c in numeric_columns and c != class_name]
    real_feature_names += [c for c in rdf.columns if c not in numeric_columns and c != class_name]
    return real_feature_names

def one_hot_encoding(df, class_name):
    
    dfX = pd.get_dummies(df[[c for c in df.columns if c != class_name]], prefix_sep='=')
    class_name_map = {v: k for k, v in enumerate(sorted(df[class_name].unique()))}
    dfY = df[class_name].map(class_name_map)
    # df = pd.concat([dfX, dfY], axis=1, join_axes=[dfX.index])
    feature_names = list(dfX.columns)
    class_values = sorted(class_name_map)
    feature_names = list(df.columns)
    class_values = 0

    return df, feature_names, class_values

def get_features_map(feature_names, real_feature_names):
    features_map = defaultdict(dict)
    i = 0
    j = 0

    while i < len(feature_names) and j < len(real_feature_names):
        if feature_names[i] == real_feature_names[j]:
            features_map[j][feature_names[i]] = j
            i += 1
            j += 1
        elif feature_names[i].startswith(real_feature_names[j]):
            features_map[j][feature_names[i]] = j
            i += 1
        else:
            j += 1
    return features_map

#----------------------------------------------------------------------
#creiamo una nuova variabile che assegna valore 1 ai giorni da Lun a Ven
#0 per Sab e Dom

def convert_date(date_in_str):
    
    date_list = re.findall(r"\w+", date_in_str)
    month = date_list[0]
    dat = date_list[1]
    year = '20' + date_list[2]
    num_day = date(int(year),int(month),int(dat)).weekday()    


    # 0 è lunedi', 2 è mercoledi 
    #dobbiamo convertire 5 e 6 in 0 per definirle come weekend days (sabato e domenica )

    if num_day >= 5:
        return 0 
    else:
        return 1

