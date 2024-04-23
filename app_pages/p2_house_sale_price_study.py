import plotly.express as px
import numpy as np
import streamlit as st
from src.data_management import load_housing_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page_sale_price_study_body():

    # load data
    df = load_housing_data()

    st.write("### House Price Study")
    st.info(
        # taken from the business requirements
        f"* The client is interested in discovering how the house attributes "
        f"correlate with the sales prices. "
        f"Therefore, the client expects data visualizations "
        f"of the correlated variables against the sale price.")
    
    # inspect data
    if st.checkbox("Inspect Housing Data"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns. \n"
            f"These are the first 10 rows.")

        st.write(df.head(10))

    st.write("---")

    # the most correlated variables - from Jupyter notebook 2_data_exploration
    vars_to_study = ['GarageArea', 'GrLivArea', 'KitchenQual', 'OverallQual', 'YearBuilt']

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to the house's sale price. \n"
        f"The most correlated variable are: **{vars_to_study}**"
    )

    # Text from Juypter notebook 2_data_exploration, Conclusions section
    st.info(
        f"Overall quality has the higest impact on SalePrice. "
        f"It is indicated that: \n"
        f"* Kitchen quality also impacts SalePrice with higher quality getting "
        f"a higher price \n"
        f"* Newer homes have a higher SalePrice. \n"
        f"* Larger garage and living areas have higher SalePrice - "
        f"a larger living area having the most impact. \n"
    )

    df_eda = df.filter(vars_to_study + ['SalePrice'])

    # Individual plots per variable
    if st.checkbox("Sale Price Levels per Variable"):
        sales_to_variable_scatter(df_eda)


def sales_to_variable_scatter(df_eda):
    # target_var = 'SalePrice'
    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        ax = sns.regplot(data=df, x=col, y="SalePrice", scatter_kws={"color": "blue"}, line_kws={"color": "red"})
        plt.ylabel('SalePrice')
        plt.xlabel(col)
        plt.title(f"{col}", fontsize=20, y=1.1)
        plt.show()


# code copied from "02 - Churned Customer Study" notebook - "Variables Distribution by Churn" section
# def plot_categorical(df, col, target_var):
    # fig, axes = plt.subplots(figsize=(12, 5))
    # sns.countplot(data=df, x=col, hue=target_var,
                #   order=df[col].value_counts().index)
    # plt.xticks(rotation=90)
    # plt.title(f"{col}", fontsize=20, y=1.05)
    # st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()


# code copied from "02 - Churned Customer Study" notebook - "Variables Distribution by Churn" section
# def plot_numerical(df, col, target_var):
    # fig, axes = plt.subplots(figsize=(8, 5))
    # sns.histplot(data=df, x=col, hue=target_var, kde=True, element="step")
    # plt.title(f"{col}", fontsize=20, y=1.05)
    # st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()


# function created using "02 - Churned Customer Study" notebook code - Parallel Plot section
# def parallel_plot_churn(df_eda):

    # hard coded from "disc.binner_dict_['tenure']"" result,
    # tenure_map = [-np.Inf, 6, 12, 18, 24, np.Inf]
    # found at "02 - Churned Customer Study" notebook
    # under "Parallel Plot" section
    # disc = ArbitraryDiscretiser(binning_dict={'tenure': tenure_map})
    # df_parallel = disc.fit_transform(df_eda)

    # n_classes = len(tenure_map) - 1
    # classes_ranges = disc.binner_dict_['tenure'][1:-1]
    # LabelsMap = {}
    # for n in range(0, n_classes):
        # if n == 0:
            # LabelsMap[n] = f"<{classes_ranges[0]}"
        # elif n == n_classes-1:
            # LabelsMap[n] = f"+{classes_ranges[-1]}"
        # else:
            # LabelsMap[n] = f"{classes_ranges[n-1]} to {classes_ranges[n]}"

    # df_parallel['tenure'] = df_parallel['tenure'].replace(LabelsMap)
    # fig = px.parallel_categories(
        # df_parallel, color="Churn", width=750, height=500)
    # we use st.plotly_chart() to render, in notebook is fig.show()
    # st.plotly_chart(fig)
