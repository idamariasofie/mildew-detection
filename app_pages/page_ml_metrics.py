import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from src.machine_learning.evaluate_clf import load_test_evaluation

# Define or import the load_test_evaluation function if necessary
# from utils import load_test_evaluation

def page_ml_metrics_body():
    st.title("ML Metrics")
    st.write("This page displays the ML metrics.")

    st.write("### Train, Validation, and Test Set: Labels Frequencies")

    labels_distribution = plt.imread("outputs/v5/datasets_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation, and Test Sets')
    st.write("---")

    st.write("### Model History")
    col1, col2 = st.beta_columns(2)
    with col1: 
        model_acc = plt.imread("outputs/v5/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread("outputs/v5/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    test_loss, test_accuracy = load_test_evaluation()
    st.write("Test Loss:", test_loss)
    st.write("Test Accuracy:", test_accuracy)

# Ensure the function is called when the script is run directly
if __name__ == "__main__":
    page_ml_metrics_body()