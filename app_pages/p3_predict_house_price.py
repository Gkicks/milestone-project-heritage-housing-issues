import streamlit as st
import pandas as pd
from src.data_management import load_housing_data, load_inherited_housing_data, load_pkl_file
from src.machine_learning.predictive_analysis_ui import predict_sale_price_single, predict_sale_price_inherited 


def page_predict_house_price_body():

    # load predict sale price files
    version = 'v1'
    sale_price_pipeline = load_pkl_file(
        f"outputs/ml_pipeline/predict_sale_price/{version}/pipeline.pkl")
    house_features = (pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
                      .columns
                      .to_list()
                      )

    st.text("")
    st.info(
        f"* Business requirement 2 - "
        f"The client is interested in predicting the house sale prices from "
        f"her 4 inherited houses, and any other house in Ames, Iowa."
    )
    st.write("---")
    st.write("## Sale Price Prediction Interface - Single Property")
    st.text("")
    st.warning(
        f"* Above Ground Area, Total Basement Area and Garage Area are all "
        f"measured in square feet\n"
        f"* Overall Quality is measured from 1-10, with 1 being 'very poor' "
        f"to 10 being 'very excellent\n"
        f"* Kitchen Quality is measured from 1-5, with 1 being 'poor' "
        f"to 5 being 'excellent'\n"
        f"* Use the + and - buttons to increase / decrease the numbers or "
        f"type over the number shown\n"
        f"* Press 'Run Predictive Analysis' to shown the predicted house price "
        f"based on the variables entered"
    )
    st.text("")

    # Generate Live Data
    X_live = DrawInputsWidgets()

    # predict on live data
    st.text("")
    if st.button("Run Predictive Analysis"):
        sale_price_prediction = predict_sale_price_single(
            X_live, house_features, sale_price_pipeline)

    st.write("---")

    # section for showing the inherited houses price prediction
    st.write("## Sale Price Prediction Interface - Inherited Houses")
    st.text("")

    inherited_df = load_inherited_housing_data()

    # display inherited houses data
    if st.checkbox("Inspect Inherited Housing Data"):
        st.write(
            f"* The dataset has {inherited_df.shape[0]} rows and {inherited_df.shape[1]} columns. \n")

        st.write(inherited_df)

    st.text("")

    # predict inherited houses data
    if st.button("Run Predictive Analysis on Inherited Houses"):
        st.write(
            sale_price_prediction = predict_sale_price_inherited(
            inherited_df, house_features, sale_price_pipeline)
        )

def DrawInputsWidgets():

    # load dataset
    df = load_housing_data()

    # we create input widgets only for 5 features
    col1, col2, col3 = st.beta_columns(3)
    col4, col5, col6 = st.beta_columns(3)

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget and set initial values
    with col1:
        feature = "GrLivArea"
        st_widget = st.number_input(
            label="Above Ground Living Area",
            min_value=0,
            max_value=11284,
            value=int(df[feature].median())
        )
    X_live[feature] = st_widget

    with col2:
        feature = "OverallQual"
        st_widget = st.number_input(
            label="Overall Quality",
            min_value=1,
            max_value=10,
            value=int(df[feature].median())
        )
    X_live[feature] = st_widget

    with col3:
        feature = "KitchenQual"
        st_widget = st.number_input(
            label="Kitchen Quality",
            min_value=1,
            max_value=5,
            value=int(df[feature].median())
        )
    X_live[feature] = st_widget
    
    with col4:
        feature = "TotalBsmtSF"
        st_widget = st.number_input(
            label="Total Basement Area",
            min_value=0,
            max_value=12220,
            value=int(df[feature].median())
        )
    X_live[feature] = st_widget

    with col5:
        feature = "GarageArea"
        st_widget = st.number_input(
            label="Garage Area",
            min_value=0,
            max_value=2836,
            value=int(df[feature].median())
        )
    X_live[feature] = st_widget

    return X_live
