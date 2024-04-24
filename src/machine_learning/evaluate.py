import streamlit as st
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')


# code copied from "Modeling and Evaluation" notebooks
def performance(X_train, y_train, X_test, y_test, pipeline):
    st.write("Model Evaluation \n")
    st.write("* Train Set")
    evaluation(X_train, y_train, pipeline)
    st.write("* Test Set")
    evaluation(X_test, y_test, pipeline)


def evaluation(X, y, pipeline):
    prediction = pipeline.predict(X)
    st.write('R2 Score:', r2_score(y, prediction).round(2))
    st.write('Mean Absolute Error:', mean_absolute_error(y, prediction).round(2))
    st.write('Mean Squared Error:', mean_squared_error(y, prediction).round(2))
    st.write('Root Mean Squared Error:', np.sqrt(
        mean_squared_error(y, prediction)).round(2))
    st.write("\n")