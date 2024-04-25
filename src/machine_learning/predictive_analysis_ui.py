import streamlit as st


def predict_sale_price_single(X_live, house_features, sale_price_pipeline):

    # from live data, subset features related to this pipeline
    X_live_sale_price = X_live.filter(house_features)

    # prediction
    sale_price_prediction = sale_price_pipeline.predict(X_live_sale_price)

    st.write(f"### The predicted sale price for this property is:")
    st.text("")
    sale_price = int(sale_price_prediction)
    st.write(f"### ${sale_price:,}")

    return sale_price_prediction


def predict_sale_price_inherited(X_live, house_features, sale_price_pipeline):

    # from live data, subset features related to this pipeline
    X_live_sale_price = X_live.filter(house_features)

    p_1 = X_live_sale_price.iloc[[0]]
    p_2 = X_live_sale_price.iloc[[1]]
    p_3 = X_live_sale_price.iloc[[2]]
    p_4 = X_live_sale_price.iloc[[3]]

    # prediction for each property
    sale_price_prediction = sale_price_pipeline.predict(X_live_sale_price)
    sale_price_prediction_p1 = sale_price_pipeline.predict(p_1)
    sale_price_prediction_p2 = sale_price_pipeline.predict(p_2)
    sale_price_prediction_p3 = sale_price_pipeline.predict(p_3)
    sale_price_prediction_p4 = sale_price_pipeline.predict(p_4)

    sale_price_p1 = int(sale_price_prediction_p1)
    sale_price_p2 = int(sale_price_prediction_p2)
    sale_price_p3 = int(sale_price_prediction_p3)
    sale_price_p4 = int(sale_price_prediction_p4)

    st.write(
        f"* The predicted sale price of property 1 is ${sale_price_p1:,}\n"
        f"* The predicted sale price of property 2 is ${sale_price_p2:,}\n"
        f"* The predicted sale price of property 3 is ${sale_price_p3:,}\n"
        f"* The predicted sale price of property 4 is ${sale_price_p4:,}\n"
        f"* **The predicted sale price of all properties combined is "
        f"${sale_price_p1+sale_price_p2+sale_price_p3+sale_price_p4:,}**"
        )

    return sale_price_prediction
