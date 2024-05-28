import streamlit as st

def page_project_summary_body():
    st.title("Project Summary")

    st.header("General Information")
    st.markdown("""
    - **Challenge**: The cherry plantation crop from Farmy & Foods is facing a challenge with powdery mildew.
    - **Current Process**: Manual verification of cherry trees for powdery mildew, which is not scalable.
    - **Proposed Solution**: Implementing an ML system to detect powdery mildew using leaf tree images.
    - **Dataset**: A collection of cherry leaf images provided by Farmy & Foods.
    """)

    st.header("Additional Information")
    st.markdown("""
    - For additional information, please visit and **read** the [Project README file](https://github.com/idamariasofie/mildew-detection).
    """)

    st.header("Business Requirements")
    st.markdown("""
    1. **Study**: Conduct a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
    2. **Prediction**: Predict if a cherry leaf is healthy or contains powdery mildew.
    """)

# Ensure the function is called when the script is run directly
if __name__ == "__main__":
    page_project_summary_body()
