import streamlit as st

def page_hypothesis_validation_body():
    st.title("Hypothesis and Validation")

    st.header("Hypothesis")
    st.markdown("""
    - **Hypothesis**: Using a machine learning approach and image processing techniques, it is hypothesized that it is feasible to develop a predictive model capable of accurately detecting powdery mildew in cherry leaves, based on features extracted from images.
    """)

    st.header("Validation Process")
    st.markdown("""
    - **Study Design**: Conducting an average image study of cherry leaves, with and without mildew.
    - **Image Analysis**: Analyzing average images, variability images, and differences between averages to identify patterns.
    """)

    st.header("Findings")
    st.markdown("""
    - **Image Montage**: Notably, leaves with powdery mildew often exhibit characteristic features such as discoloration or irregularities.
    - **Average Image Study**: Despite comprehensive efforts, no discernible patterns were identified to effectively differentiate between healthy leaves and those infected with powdery mildew.
    """)

# Ensure the function is called when the script is run directly
if __name__ == "__main__":
    page_hypothesis_validation_body()
