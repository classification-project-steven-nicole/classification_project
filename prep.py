import pandas as pd
import numpy as np
from pydataset import data
from sklearn.preprocessing import LabelEncoder

def null_values(df):
    df.replace(' ', np.nan, inplace=True)
    df.fillna(0, inplace=True)
    df["total_charges"] = df.total_charges.astype(float)
    return df

def transform_churn(df):
    df['churn'] = df['churn'].replace({'Yes': 1, 'No': 0})
    return df

def tenure_year(df):
    tenure_year = (df.tenure / 12)
    df['tenure_year']= tenure_year.round(2)
    return df

def household_type_id(df):
    df["household_type_id"] = df["partner"].map(str) + df["dependents"]
    df['household_type_id'] = df['household_type_id'].replace({'YesYes': 3, 'NoNo': 0, 'YesNo': 2, 'NoYes': 1})
    return df

def streaming_services(df):
    df["streaming_services"] = df["streaming_tv"].map(str) + df["streaming_movies"]
    df['streaming_services'] = df['streaming_services'].replace({'YesYes': 3, 'NoNo': 0, 'YesNo': 2, 'NoYes': 1, 'No internet serviceNo internet service': 0})
    return df

def phone_info(df):
    df["phone_id"] = df["phone_service"].map(str) + df["multiple_lines"]
    df['phone_id'] = df['phone_id'].replace({'YesYes': 2, 'NoNo phone service': 0, 'YesNo': 1})
    return df

def online_security_backup(df):
    df["online_security_backup"] = df["online_security"].map(str) + df["online_backup"]
    df['online_security_backup'] = df['online_security_backup'].replace({'No internet serviceNo internet service': 0,'NoNo': 1, 'NoYes': 2,'YesNo': 3,'YesYes': 4})
    return df

def telco_encoded(df):
    encoded = df[['gender', 'device_protection', 'tech_support', 'paperless_billing']].apply(LabelEncoder().fit_transform)
    df.drop(columns= ['gender', 'device_protection', 'tech_support', 'paperless_billing'], axis=1, inplace=True)
    df = df.join(encoded)
    return df

def drop_columns(df):
    df = df.drop(['partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'streaming_tv', 'streaming_movies'], axis=1)
    return df

def prep_telco(df):
    return df.pipe(null_values)\
        .pipe(transform_churn)\
        .pipe(tenure_year)\
        .pipe(household_type_id)\
        .pipe(streaming_services)\
        .pipe(phone_info)\
        .pipe(online_security_backup)\
        .pipe(telco_encoded)\
        .pipe(drop_columns)
