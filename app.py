import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.p1_project_summary import page_summary_body
from app_pages.p2_house_sale_price_study import page_sale_price_study_body

# Create an instance of the app
app = MultiPage(app_name= "Predicting Housing Prices in Ames, Iowa")  

# Adding pages to the app
app.add_page("Project Summary", page_summary_body)
app.add_page("House Sale Price Study", page_sale_price_study_body)
# app.add_page("Predict House Price", )
# app.add_page("Project Hypothesis and Validation", )
# app.add_page("ML - Predict House Price", )

app.run() # Run the  app