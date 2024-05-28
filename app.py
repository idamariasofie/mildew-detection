import streamlit as st
from app_pages.multipage import MultiPage
from src.machine_learning.evaluate_clf import load_test_evaluation

# Load page scripts
from app_pages.page_project_summary import page_project_summary_body
from app_pages.page_findings import page_findings_body
from app_pages.page_prediction_interface import page_prediction_interface_body
from app_pages.page_hypothesis_validation import page_hypothesis_validation_body
from app_pages.page_ml_metrics import page_ml_metrics_body

app = MultiPage(app_name="Mildew Detection") 

app.add_page("Project Summary", page_project_summary_body)
app.add_page("Findings", page_findings_body)
app.add_page("Prediction Interface", page_prediction_interface_body)
app.add_page("Hypothesis and Validation", page_hypothesis_validation_body)
app.add_page("ML Metrics", page_ml_metrics_body)

app.run() 