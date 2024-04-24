import streamlit as st


def predict_sale_price(X_live, house_features, sale_price_pipeline):

    # from live data, subset features related to this pipeline
    X_live_sale_price = X_live.filter(house_features)
    # sale_price = X_live_sale_price.iloc[0]
    # st.write("Sale price is:")
    # st.write(sale_price)
    # X_live_sale_price['SalePrice'] = X_live_sale_price['SalePrice'].astype(int)

    # predict
    sale_price_prediction = sale_price_pipeline.predict(X_live_sale_price)

    statement = (
        f"### The predicted price for this property is:"
    )

    st.text("")
    st.write(statement)
    st.text("")
    
    sale_price = int(sale_price_prediction)
    st.write(f"### ${sale_price:,}")
    # st.write(sale_price_prediction)
    
    return sale_price_prediction