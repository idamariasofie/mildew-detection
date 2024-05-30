import streamlit as st
import os
import matplotlib.pyplot as plt
import random
import itertools
from matplotlib.image import imread

def page_findings_body():
    st.title("Insights & Discoveries")
    st.write("Explore the insightful findings from our project.")

    st.info("Exploring the Complexities of Cherry Leaf Structures")

    # Checkbox for Difference between average and variability image
    if st.checkbox("Leaf Patterns: Average vs Variability"):
        avg_healthy = plt.imread("outputs/v1/avg_var_healthy.png")
        avg_powdery = plt.imread("outputs/v1/avg_var_powdery_mildew.png")
        st.warning("Our exploration of average and variability images revealed intriguing insights. While no distinct patterns emerged, we observed subtle differences in color pigment.")
        st.image(avg_healthy, caption='Healthy Leaf - Average and Variability')
        st.image(avg_powdery, caption='Powdery Mildew Leaf - Average and Variability')
        st.write("---")

    # Checkbox for Differences between average powdery mildew and average healthy leaf
    if st.checkbox("Analyzing Leaf Traits: Average Powdery Mildew vs Average Healthy Leaf"):
        avg_difference = plt.imread("outputs/avg_diff.png")
        st.warning("Our analysis of average images highlighted subtle differences, yet identifying a clear differentiation proved to be challenging.")
        st.image(avg_difference, caption='Difference between Average Images')
        st.write("---")

    # Checkbox for Image Montage
    if st.checkbox("Exploring Cherry Leaf Diversity"):
        st.write("* To refresh the montage, click on the 'Create Montage' button")
        data_dir = 'inputs/datasets/cherry-leaves'
        labels = os.listdir(data_dir + '/validation')
        label_to_display = st.selectbox(label="Select label", options=labels, index=0)
        
        if st.button("Create Montage"):
            try:
                image_montage(dir_path=data_dir + '/validation',
                              label_to_display=label_to_display,
                              nrows=8, ncols=3, figsize=(10, 25))
            except Exception as e:
                st.error(f"Error: {e}")

def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
    labels = os.listdir(dir_path)
    
    if label_to_display in labels:
        images_list = os.listdir(os.path.join(dir_path, label_to_display))
        
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            st.warning(f"Please decrease the number of rows or columns to create your montage. There are {len(images_list)} images in your selected subset.")

        plot_idx = list(itertools.product(range(nrows), range(ncols)))
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        
        for x in range(nrows * ncols):
            img = imread(os.path.join(dir_path, label_to_display, img_idx[x]))
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        
        plt.tight_layout()
        st.pyplot(fig=fig)
    else:
        st.error("The selected label does not exist.")

# Ensure the function is called when the script is run directly
if __name__ == "__main__":
    page_findings_body()
