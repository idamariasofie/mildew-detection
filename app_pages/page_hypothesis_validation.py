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
    - **Image Montage**: Typically, a parasitized cell has purplish marks across it.
    - **Average Image Study**: Did not reveal any clear pattern to differentiate one from another.
    """)

# Ensure the function is called when the script is run directly
if __name__ == "__main__":
    page_hypothesis_validation_body()
