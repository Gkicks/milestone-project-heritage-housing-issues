import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_housing_data():
    df = pd.read_csv("outputs/datasets/collection/HousePricesRecords.csv")
    df['KitchenQual'] = df['KitchenQual'].replace({'Po':0, 'Fa':1, 'TA':2, 'Gd':3, 'Ex':4})
    return df


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_inherited_housing_data():
    df = pd.read_csv("inputs/datasets/raw/house-prices/house-price/inherited_houses.csv")
    df['KitchenQual'] = df['KitchenQual'].replace({'Po':0, 'Fa':1, 'TA':2, 'Gd':3, 'Ex':4})
    return df


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)