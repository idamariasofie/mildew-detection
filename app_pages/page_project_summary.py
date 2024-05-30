import streamlit as st

def page_project_summary_body():
    st.title("Project Summary")

    st.header("General Information")
    st.markdown("""
    Farmy & Foods is encountering a challenge with their cherry plantation crop—powdery mildew. Currently, manual verification is conducted on each cherry tree, which involves spending around 30 minutes per tree to visually inspect leaves for powdery mildew. If detected, a specific compound is applied to kill the fungus, taking an additional minute. With thousands of cherry trees spread across multiple farms, this manual process is not scalable.

    To address this, the IT team proposed an ML system to instantly detect powdery mildew using leaf tree images. Given the complexity and nuances of leaf image analysis, we decided to develop a Convolutional Neural Network (CNN) model, known for its effectiveness in image classification tasks.
    """)

    st.success('''
    __Project Dataset__
    - The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).
    - It contains over 4,000 images from the client's crop fields, depicting healthy cherry leaves and leaves with powdery mildew. Ensuring the quality of the cherry plantation crop is vital to Farmy & Foods' reputation and market position.
    ''')

    st.header("Additional Information")
    st.markdown("""
    For more details, please refer to the [Project README file](https://github.com/idamariasofie/mildew-detection).
    """)

    st.header("Business Requirements")
    st.markdown("""
    1. The client aims to visually differentiate between healthy cherry leaves and those with powdery mildew.
    2. The client seeks to predict whether a cherry leaf is healthy or has powdery mildew.
    """)

# Ensure the function is called when the script is run directly
if __name__ == "__main__":
    page_project_summary_body()