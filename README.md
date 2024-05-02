## Cherry leaves - mildew detection using CNN

An image classifier machine learning project for mildew detection on cherry leaves, utilizing convolutional neural networks (CNN).

## Table of Contents

Project Dataset
Business Requirements
Hypothesis and Validation
The rationale to map the business requirements to the Data Visualizations and ML tasks
Epics
User Stories
Data Collection and Preparation
Data Visualization
Model Training, Optimization, and Evaluation
Dashboard Planning, Designing, and Development and Deployment
API Development and Deployment
ML Business Case
Dashboard Design (Streamlit App User Interface)
Page 1: Home
Page 2: Project Summary
Page 3: Data Visualization
Page 4: Predict Gender
Page 5: Hypothesis and Validation
Page 6: ML Metrics
Page 7: API
Deployment
Main Data Analysis & Machine Learning Libraries
Run locally
Credits

## Project Dataset

Dataset used provided by Code Institute.

I have not included the actual data in this repo, if you would like to inspect the dataset, please follow the steps in Run locally to download the dataset to your local machine.

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and validation

Hypothesis: Powdery mildew can be detected using an average image study. 

How to validate: Conducting an average image study of cherry leaves, with and without mildew. 

## The rationale to map the business requirements to the Data Visualisations and ML tasks

Epics:
Data collection and preparation
Data visualization
Model training, optimization and evaluation
Dashboard planning, designing, and development and deployment
API Development and deployment
User stories:
Data Collection and Preparation
User Story: As a developer, I can source and acquire the data to create a reliable and well-prepared dataset for the project.
Task: Download the dataset and extract the relevant data, save it in a new relevant folder structure.
Data Visualization
User Story: As a developer, I can generate informative visualizations to understand the data, providing valuable insights.

Task: Choose appropriate visualization techniques, generate visualizations and save them.
User Story: As a developer, I can integrate data visualizations into the dashboard for user-friendly data exploration.

Task: Design the layout and implement interactive features.
Model Training, Optimization, and Evaluation
User Story: As a developer, I can find the optimal hyperparamaters for my model in a set range of parameters.

Task: Find the optimal parameters using techniques such as Grid Search or Randomized Search.
User Story: As a developer, I can train and fine-tune the machine learning model based on the optimal hyperparameters found.

Task: Define model architecture and implement a function to build the model based on the found optimal hyperparameters.
User Story: As a developer, I can evaluate my models performance using a variety of metrics.

Task: Perform model evaluation using a Machine Learning library, visually represent the results and save the visualizations.
User Story: As a user, I can access model evaluation results, helping me understand the model's performance.

Task: Provide a user interface for accessing model evaluation reports.
Dashboard Planning, Designing, and Development and Deployment
User Story: As a developer, I can implement Streamlit features, making it interactive and user-friendly.

Task: Develop and integrate interactive Streamlit features and functionalities into the dashboard.
User Story: As a developer, I can deploy the Streamlit dashboard, ensuring it is accessible to users.

Task: Deploy the streamlit app to Heroku and ensure the dashboard is accessible online.
User Story: As a user, I can access and interact with the deployed Streamlit app, enabling me to navigate through the project, explore data visualizations, and make live predictions on the model.

Task: Provide navigation options, interactive data exploration features and a page for making live predictions with a way to download sample images for making predictions.
API Development and Deployment
User Story: As a user, I can access the API in order to integrate the machine learning solution into my applications.

Task: Develop an API and provide an endpoint for users to interact with the model.
User Story: As a user, I can access information for usage of the API in order to learn how to use it.

Task: Provide usage instructions along with example code on how to use the API inside the dashboard.

## ML Business Case

We want an ML model to predict if the cheery leaf has powdery mildew based on the image dataset provided. The target variable is categorical and contains 2-classes. We consider a classification model. It is a supervised model, a 2-class, single-label, classification model which produces output: 0 (no powdery mildew) or 1 (powdery mildew)
Our aim is to have an accuracy of at least 90%
Our ideal outcome is to provide the company with a dependable solution to provide their algorithm with reliable data.
An API will be required for the company to integrate the solution into their platform in an automated way. The images will be gathered from profile pictures and posts made by users.


## Dashboard Design

- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
- Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).

## Unfixed Bugs

- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

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

- Here, you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits

- In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements (optional)

- Thank the people who provided support throughout this project.
