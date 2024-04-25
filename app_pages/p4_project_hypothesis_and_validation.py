import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect that quality will have an impact on house price, "
        f"with houses that have higher quality features fetching a higher "
        f"sale price:\n"
        f"  * Correct. The correlation study shows that overall quality "
        f"and kitchen quality are two of the main indicators of sale price, "
        f"with the higher quality finishes having higher sale price\n\n\n"
        f"* We suspect that larger houses fetch a higher sale price:\n"
        f"  * Correct. The correlation study shows that garage area and above "
        f"ground living area are two more of the main indicators of sale "
        f"price, with larger square footage having higher sale price. "
        f"The feature engineering also showed that basement square footage "
        f"was one of the five most important features to sale price\n\n\n"
        f"* We suspect that the age of a property will have an impact on "
        f"sale price, with newer properties fetching a higher sale price:\n"
        f"  * Correct. The correlation study show that both the year built "
        f"and the year the garage was built have a high correlation with sale "
        f"price however, during feature engineering, they were not found to "
        f"be the features that were most important"
    )
