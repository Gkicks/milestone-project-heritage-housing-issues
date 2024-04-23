import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.p1_project_summary import page_summary_body
# from app_pages.page_churned_customer_study import page_churned_customer_study_body

app = MultiPage(app_name= "Predicting Housing Prices in Ames, Iowa") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Project Summary", page_summary_body)
# app.add_page("Customer Base Churn Study", page_churned_customer_study_body)

app.run() # Run the  app