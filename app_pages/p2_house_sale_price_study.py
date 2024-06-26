import plotly.express as px
import numpy as np
import streamlit as st
from src.data_management import load_housing_data
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page_sale_price_study_body():
    """ Page 2 of Streamlit Dashboard - House Sale Price Study """

    # Load data
    df = load_housing_data()

    # Change the object type data to numerical data
    df['BsmtExposure'] = df['BsmtExposure'].replace(
        {'None': 0, 'No': 1, 'Mn': 2, 'Av': 3, 'Gd': 4})
    df['BsmtFinType1'] = df['BsmtFinType1'].replace(
        {'None': 0, 'Unf': 1, 'LwQ': 2, 'BLQ': 3, 'Rec': 4,
            'ALQ': 5, 'GLQ': 6})
    df['GarageFinish'] = df['GarageFinish'].replace(
        {'None': 0, 'Unf': 1, 'RFn': 2, 'Fin': 3})
    df['KitchenQual'] = df['KitchenQual'].replace(
        {'Po': 0, 'Fa': 1, 'TA': 2, 'Gd': 3, 'Ex': 4})

    st.write("### House Price Study")
    st.text("")
    st.info(
        # Copied from README file - "Business Requirements" section
        f"* Business requirement 1 - The client is interested in discovering "
        f" how the house attributes correlate with the sales prices. "
        f"Therefore, the client expects data visualizations "
        f"of the correlated variables against the sale price.")

    # Inspect data
    if st.checkbox("Inspect Housing Data"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns. "
            f"\nThese are the first 10 rows:")

        st.write(df.head(10))

    st.write("---")

    # The most correlated variables - from Jupyter notebook 2_data_exploration
    vars_to_study = [
        'GarageArea', 'GrLivArea', 'KitchenQual', 'OverallQual', 'YearBuilt'
        ]

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better "
        f"understand how the variables are correlated to the house's sale "
        f"price.\n"
        f"The most correlated variable are: **{vars_to_study}**"
    )

    # Text from Juypter notebook 2_data_exploration, Conclusions section
    st.success(
        f"Overall quality has the higest impact on SalePrice. "
        f"It is indicated that: \n"
        f"* Kitchen quality also impacts SalePrice with higher quality "
        f"getting a higher price \n"
        f"* Newer homes have a higher SalePrice. \n"
        f"* Larger garage and living areas have higher SalePrice - "
        f"a larger living area having the most impact. \n"
    )

    df_eda = df.filter(vars_to_study + ['SalePrice'])

    # Individual scatter plots per variable
    if st.checkbox("Sale Price Levels per Variable"):
        plot_scatter(df_eda, vars_to_study, 'SalePrice')

    # Spearman Correlation
    if st.checkbox("Spearman Correlation"):
        df_spearman_heat = df.corr(method='spearman')
        heatmap_corr(
            df=df_spearman_heat, threshold=0.6, figsize=(15, 5), font_annot=8)

    # Pearson Correlation
    if st.checkbox("Pearson Correlation"):
        df_pearson_heat = df.corr(method='pearson')
        heatmap_corr(
            df=df_pearson_heat, threshold=0.6, figsize=(15, 5), font_annot=8)


def plot_scatter(df, col, target_var):
    """ Plots each variable in a scatter chart, against the target variable """
    for col in df.drop([target_var], axis=1).columns.to_list():
        fig, axes = plt.subplots(figsize=(8, 5))
        sns.regplot(data=df, x=col, y=target_var, scatter_kws={
            "color": "purple"}, line_kws={"color": "red"})
        plt.title(f"{col}", fontsize=20, y=1.1)
        st.pyplot(fig)


def heatmap_corr(df, threshold, figsize, font_annot):
    """ display heatmat for Spearman Correlation """
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=bool)
        mask[np.triu_indices_from(mask)] = True
        mask[abs(df) < threshold] = True
        fig, axes = plt.subplots(figsize=figsize)
        sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                    mask=mask, cmap='plasma', annot_kws={
                        "size": font_annot}, ax=axes,
                    linewidth=0.5
                    )
        axes.set_yticklabels(df.columns, rotation=0)
        plt.ylim(len(df.columns), 0)
        st.pyplot(fig)
