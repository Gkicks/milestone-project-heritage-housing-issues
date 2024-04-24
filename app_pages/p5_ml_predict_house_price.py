import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_housing_data, load_pkl_file
from src.machine_learning.evaluate import performance, evaluation


def page_ml_predict_house_price_body():

    version = 'v1'
    # load needed files
    sale_price_pipe_model = load_pkl_file(
        f'outputs/ml_pipeline/predict_sale_price/{version}/pipeline.pkl')
    sale_price_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_sale_price/{version}/features_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/y_train.csv").values
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/y_test.csv").values

    st.write("### ML Pipeline: Predict Sales Price")
    # display pipeline training summary conclusions
    st.info(
        f"* The aim of the pipline was to achieve an R2 score of at 0.75 "
        f"on the train set as well as on the test set"
        f"* The pipeline performance on train and test set is 0.98 and 0.85, respectively."
    )

    # show pipelines
    st.write("---")

    st.write("* The The pipeline that was used in this project:")
    st.write(sale_price_pipe_model)

    # show feature importance plot
    st.write("---")
    st.write("* The features the model was trained and their importance.")
    st.write(X_train.columns.to_list())
    st.image(sale_price_feat_importance)


    # evaluate performance on train and test set
    st.write("---")
    st.write("### Pipeline Performance")
    performance(X_train, y_train, X_test, y_test, sale_price_pipe_model)