import streamlit as st


def page_summary_body():
    """ Page 1 of Streamlit Dashboard - Project Summary """

    st.write("### Project Summary")

    # Copied from README file - "Dataset Content" section
    st.info(
        f"**Project Dataset**\n"
        f"* The dataset represents housing records from Ames, Iowa "
        f"indicating house profile "
        f"(Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, "
        f"Year Built) and its respective sale price for houses "
        f"built between 1872 and 2010.")

    # Link to README file
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Gkicks/milestone-project-"
        f"heritage-housing-issues/blob/main/README.md).")

    # Copied from README file - "Business Requirements" section
    st.success(
        f"The project has two business requirements:\n"
        f"* 1 - The client is interested in discovering how the house "
        f"attributes correlate with the sale price. "
        f"Therefore, the client expects data visualisations of the correlated "
        f"variables against the sale price to show this.\n"
        f"* 2 - The client is interested in predicting the house sale price "
        f"from her four inherited houses and any other house in Ames, Iowa."
        )
