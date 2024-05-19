## Cherry leaves - mildew detection using CNN

An image classifier machine learning project for mildew detection on cherry leaves, utilizing convolutional neural networks (CNN).

## Table of Contents

1. [Project Dataset](#project-dataset)
2. [Business Requirements](#business-requirements)
3. [Hypothesis and Validation](#hypothesis-and-validation)
4. [The rationale to map the business requirements to the Data Visualizations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)
   - [Epics](#epics)
   - [User Stories](#user-stories)
      1. [Information Gathering and Data Collection](#information-gathering-and-data-collection)
      2. [Data Visualization, Cleaning, and Preparation](#data-visualization-cleaning-and-preparation)
      3. [Model Training, Optimization, and Validation](#model-training-optimization-and-validation)
      4. [Dashboard Planning, Designing, and Development](#dashboard-planning-designing-and-development)
      5. [Dashboard Deployment and Release](#dashboard-development-and-release)
5. [ML Business Case](#ml-business-case)
6. [Dashboard Design (Streamlit App User Interface)](#dashboard-design-streamlit-app-user-interface)
   - [Page 1: Home/ Project Summary](#page-1-home-project-summary)
   - [Page 2: Findings](#page-2-findings)
   - [Page 3: Prediction Interface](#page-3-prediction-interface)
   - [Page 4: Project Hypothesis and Validation](#page-4-project-hypothesis-and-validation)
   - [Page 5: Model Performance ](#page-5-model-performance)
   - [Page 6: ML Metrics](#page-6-ml-metrics)
7. [Unfixed Bugs](#unfixed-bugs)
8. [Deployment](#deployment)
9. [Main Data Analysis & Machine Learning Libraries](#main-data-analysis--machine-learning-libraries)
10. [Run locally](#run-locally)
11. [Credits](#credits)
12. [Acknowledgements](#acknowledgements)

## Project Dataset

Dataset used provided by Code Institute.

I have not included the actual data in this repo, if you would like to inspect the dataset, please follow the steps in [Run locally](#run-locally) to download the dataset to your local machine.

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and validation

Hypothesis: Using a machine learning approach and image processing techniques, I hypothesize that it is feasible to develop a predictive model capable of accurately detecting powdery mildew in cherry leaves, based on features extracted from images.

How to validate: Conducting an average image study of cherry leaves, with and without mildew. 

## The rationale to map the business requirements to the Data Visualisations and ML tasks

### Epics:

1. Information Gathering and Data Collection: Focuses on gathering relevant information and collecting the cherry leaf image dataset required for the project.
2. Data Visualization, Cleaning, and Preparation: Involves visualizing, cleaning, and preparing the dataset for model training, ensuring data quality and integrity.
3. Model Training, Optimization, and Validation: Covers the design, training, optimization, and validation of a neural network model to predict cherry leaf health status.
4. Dashboard Planning, Designing, and Development: Encompasses the planning, designing, and development of an interactive dashboard interface for users to explore project findings and make live predictions.
5. Dashboard Deployment and Release: Focuses on deploying the dashboard to a web hosting platform and releasing it for user access, ensuring accessibility and usability.


### User Stories:

Information Gathering and Data Collection
1. User Story: As a developer, I can gather relevant information and collect the cherry leaf image dataset for the project.
- Task: Obtain cherry leaf images from the provided Kaggle repository and ensure compliance with the non-disclosure agreement (NDA) for data sharing and save the images in a new relevant folder structure.

Data Visualization, Cleaning, and Preparation
1. User Story: As a developer, I can visualize and explore the dataset to understand its characteristics and identify patterns relevant to powdery mildew detection.
- Task: Generate average images, variability images, and image montages for healthy and powdery mildew cherry leaves to fulfill Business Requirement 1. 
2. User Story: As a developer, I can clean and prepare the dataset for model training, addressing any missing values or outliers.
- Task: Implement data cleaning techniques and resize images to a smaller shape to reduce model size and enable smoother GitHub pushes.

Model Training, Optimization, and Validation

1. User Story: As a developer, I can design and train a neural network model to predict whether a cherry leaf is healthy or contains powdery mildew.
- Task: Define the neural network architecture, train the model on the prepared dataset, and optimize hyperparameters to achieve a minimum accuracy of 97%.
2. User Story: As a developer, I can validate the model's performance using appropriate metrics to ensure it meets the client's performance goal.
- Task: Evaluate the trained model's performance using metrics such as accuracy, precision, recall, and F1-score, ensuring it meets the minimum accuracy requirement.

Dashboard Planning, Designing, and Development:

1. User Story: As a developer, I can plan and design an intuitive dashboard interface for users to explore project findings and make live predictions.
- Task: Design the dashboard layout and navigation, including features like project summary, study findings, live prediction, and technical performance pages.
2. User Story: As a developer, I can develop the dashboard to ensure accessibility and usability.
- Task: Develop the dashboard using Streamlit, focusing on creating an intuitive user interface and incorporating all required features.

Dashboard Deployment and Release

1. User Story: As a developer, I can deploy the dashboard to a web hosting platform, ensuring accessibility and usability for users.
- Task: Deploy the developed dashboard to a web hosting service (e.g., Heroku) for user access.


## ML Business Case

Farmy & Foods, a leading agriculture company, is facing challenges in detecting powdery mildew in cherry leaves across their cherry plantations. Currently, the process involves manual verification by employees, which is time-consuming and not scalable due to the large number of cherry trees spread across multiple farms. The company seeks an efficient solution to automate the detection process, ensuring the quality of their cherry products while optimizing resource utilization.

Business Objectives:
1. Efficiency Improvement: Reduce the time and effort required for detecting powdery mildew in cherry leaves, enabling faster decision-making and response to infections.
2. Scalability: Develop a scalable solution that can handle the inspection of thousands of cherry trees spread across multiple farms, ensuring consistent and reliable detection of powdery mildew.
3. Quality Assurance: Ensure the quality of cherry products by accurately identifying and treating trees infected with powdery mildew, thereby minimizing crop loss and maintaining customer satisfaction.

Proposed Solution:
Implement a machine learning (ML) system based on convolutional neural networks (CNNs) to automate the detection of powdery mildew in cherry leaves. By leveraging image processing techniques and deep learning algorithms, the proposed solution aims to analyze cherry leaf images and classify them as healthy or infected with powdery mildew with high accuracy and efficiency.

Business Benefits:
1. Time Savings: By automating the detection process, Farmy & Foods can significantly reduce the time spent on manual inspections, enabling employees to focus on other critical tasks and increasing overall operational efficiency.
2. Cost Reduction: The implementation of an ML-based solution eliminates the need for manual labor-intensive inspections, leading to cost savings associated with labor, resources, and potential crop loss due to undetected infections.
3. Scalability: The proposed solution can scale to handle the inspection of large-scale cherry plantations, allowing Farmy & Foods to maintain consistent quality standards across all farms and effectively manage their agricultural operations.
4. Quality Assurance: By accurately detecting powdery mildew in cherry leaves, the ML system ensures the timely identification and treatment of infected trees, preserving the quality and integrity of cherry products and enhancing customer trust and satisfaction.

Success Criteria:
1. Accuracy: Achieve a minimum accuracy rate of 97% in classifying cherry leaves as healthy or infected with powdery mildew, ensuring reliable detection performance across different farm environments and conditions.
2. Efficiency: Reduce the inspection time per cherry tree from 30 minutes to near-instantaneous detection using the ML system, allowing Farmy & Foods to streamline their agricultural operations and respond promptly to infections.
3. Scalability: Deploy a scalable solution capable of handling the inspection of thousands of cherry trees across multiple farms, accommodating the company's growth and expansion plans without compromising detection accuracy or performance.

Risk Mitigation:
1. Data Privacy: Adhere to non-disclosure agreements (NDAs) and ethical guidelines when handling and processing sensitive data, ensuring the confidentiality and security of cherry leaf images and related information.
2. Model Robustness: Conduct rigorous testing and validation of the ML model to ensure its robustness and reliability in detecting powdery mildew under various environmental conditions and image quality constraints.
3. Deployment Challenges: Collaborate closely with IT and operational teams to address any technical challenges or infrastructure requirements during the deployment of the ML system, ensuring seamless integration with existing workflows and systems.

Conclusion:
By leveraging machine learning technology to automate the detection of powdery mildew in cherry leaves, Farmy & Foods can achieve significant improvements in operational efficiency, cost savings, and product quality assurance. The proposed ML solution not only addresses the immediate challenge of powdery mildew detection but also lays the foundation for future innovations and applications in agricultural pest and disease management, positioning Farmy & Foods as a leader in sustainable and technology-driven agriculture.

## Dashboard design (Streamlit App User Interface)

### Page 1: Home/ Project Summary
This page provides an overview of the project, including a summary of the dataset used and the client's requirements.
Key components:
-	Project title and description.
-   Dataset summary statistics, such as the number of images, classes (healthy vs. powdery mildew), and data distribution.
-   Client's requirements and project objectives.
-	Link to GitHub profile
-	Link to GitHub repo

### Page 2: Findings
This page presents the findings related to the study on visually differentiating healthy cherry leaves from those containing powdery mildew.
Key components:
- Visualizations comparing healthy and infected cherry leaves, such as histograms or scatter plots highlighting key features.
Insights drawn from the visual analysis, such as distinguishing characteristics between healthy and infected leaves.

### Page 3: Prediction Interface
This page allows users to upload cherry leaf images for live prediction of their health status.
Key components:
- A file uploader widget enabling users to upload multiple images.
- For each uploaded image, display:
- The uploaded image.
- Prediction statement indicating whether the leaf is healthy or infected with powdery mildew, along with the probability score.
- A table displaying the image name, prediction results, and probability scores.
- Download button to download the prediction results table.

- Provide a download link for images of faces for live prediction
- Provide a file uploader and predict button to interact with the model
- Provide a download button for a report of the predictions

### Page 4: Project Hypothesis and Validation
This page outlines the project hypothesis and how it was validated throughout the project lifecycle.
Key components:
- Project hypothesis statement.
- Description of the validation approach, including data collection, model training, and evaluation methods.
- Summary of validation results and their alignment with the project hypothesis.

### Page 5: Model Performance 
This page provides technical details on the performance of the ML model developed for cherry leaf health prediction.
Key components:
- Model architecture overview, including the types of layers and parameters used.
- Performance metrics such as accuracy, precision, recall, and F1-score.
- Visualizations of model performance, such as confusion matrices or ROC curves.

### Page 6: ML Metrics
- Provide metrics from model training presented visually
- Provide metrics from model evaluation presented visually
- Provide True Positives(TP), True Negatives(TN), False Positives(FN) and False Negatives(FN) from model evaluation presented visually
- Provide scikit-learns classification report from model evalutation

## Unfixed Bugs

### Collect data set from Kaggle

- Initially, I attempted to collect the data set from Kaggle using a path specified in my code, following the structure outlined in Walkthrough 1 project. However, during the download process, I consistently encountered a 403 - forbidden error. In an effort to resolve this issue, I undertook the following steps:

Path Verification: I double-checked to ensure that the path to the Kaggle data set was accurately specified within my code.

Token Regeneration: Suspecting that the issue might be related to authentication, I invalidated my existing Kaggle token and generated a new one, which I then integrated into my IDE.

Despite these troubleshooting efforts, the problem persisted, and the 403 error persisted. Faced with this obstacle, I made the decision to download the data set directly and import it into my IDE. While this course of action necessitated alterations to the code and structure of my DataCollection workbook, I remained steadfast in my determination to progress with the project.


## Deployment

This project was deployed to [Heroku](https://heroku.com/) using the following steps:
1.  Log in to Heroku and create an App
2.  At the Deploy tab, select GitHub as the deployment method.
3.  Select your repository name and click Search. Once it is found, click Connect.
4.  Select the branch you want to deploy, then click Deploy Branch.
5.  The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6.  If the slug size is too large then specify dependencies unnecessary for deployment by specifying your 'requirements.txt' and specify unnecessary files in a '.slugignore' in the root directory.


### Heroku

- The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

__Main Data analysis libraries used__:

- Numpy
	- For performing calculations on large amounts of data efficiently, mainly pixel data in this case
	- Normalizing pixel data
	- Calculating means and standard deviations
	- Base for other data analysis and ML libraries
- Pandas
	- Mainly for pandas DataFrame's for easy management of large data (sampling, shuffling, concatenation etc.)
- Matplotlib & Seaborn
	- For plotting and visualization of data
	- Showing images from pixel data
	- Metric plots & Histograms

__Main Machine Learning libraries used:__

- TensorFlow & Keras
	- Image augmentation
	- Model loading
	- Defining model architecture
	- Training model
	- One-hot encoding
	- tensorflow.data.Datset API
- Scikit Learn
	- Hyperparameter optimization using GridSearchCV
	- Generating confusion matrixes & classification reports
- OpenCV
	- Reading images pixel data as NumPy arrays
	- Resizing images
- Scikeras
	- For performing GridSearchCV on Keras models which is not compatible by default with scikit-learn. (KerasClassifier)

## Run locally

This repo covers the entire process of creating a ML model. From collecting and processing the data, to conducting hyperparameter optimization, data augmentation, defining and training the model on the data.

__To use this repo, follow these steps:__

1. Fork or clone this repository
2. Install dependencies by running:
	```bash
	pip install -r "requirements-dev.txt"
	```
3. Register an account with [Kaggle](https://www.kaggle.com/) and create a new API token, download the kaggle.json and place it in the projects root directory.
4. Run the notebooks in the jupyter_notebooks folder in the specified order.
	- __DataCollection.ipynb:__ Downloads the dataset and extracts specified number of images.
	- __DataVisualization.ipynb:__ Conducts studies on the data and saves insightful plots.
	- __Model.ipynb:__ Prepares data, performs data augmentation and hyperparameter optimization, defines model architecture, trains, evaluates and saves a ML model.
5. Start the web app by running:
	```bash
	streamlit run Home.py
	```
___If you encounter an error while importing opencv-python(cv2), run the following commands:___
```bash
sudo apt-get update
sudo apt-get install -y libgl1-mesa-dev
```

## Credits


### Content

- [Churnometer repo by Code Institute](https://github.com/Code-Institute-Solutions/churnometer#readme): For the Readme template/structure.

- [Gender predictor](https://github.com/linx02/genderpredictor/tree/main): For the Readme template/structure.

- [Streamlit documentation](https://docs.streamlit.io/): For getting the web app up and running.

- [Solve error with using OpenCV](https://stackoverflow.com/questions/55313610/importerror-libgl-so-1-cannot-open-shared-object-file-no-such-file-or-directo)


### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements

- 
