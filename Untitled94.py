#!/usr/bin/env python
# coding: utf-8

# 1. What are the key tasks that machine learning entails? What does data pre-processing imply?
# 

# Data collection: Gathering relevant data from various sources.
# Data preprocessing: Cleaning and transforming the data to make it suitable for analysis.
# Feature selection and engineering: Identifying the most informative variables and creating new ones if needed.
# Model selection: Choosing the appropriate machine learning algorithm or model.
# Training: Fitting the model to the training data to learn patterns and relationships.
# Evaluation: Assessing the performance of the trained model using evaluation metrics.
# Hyperparameter tuning: Optimizing the model's settings to improve performance.
# Prediction or inference: Applying the trained model to new data to make predictions or draw conclusions.
# 
# 
# Data preprocessing refers to the steps taken to prepare the data for machine learning. It involves cleaning the data by handling missing values, outliers, and noise. It also includes transforming the data by scaling, normalizing, or encoding categorical variables. Data preprocessing is essential to ensure that the data is in a suitable format and quality for accurate and effective machine learning analysis.

# 2. Describe quantitative and qualitative data in depth. Make a distinction between the two.
# 

# Quantitative data is numerical and analyzed mathematically, while qualitative data is descriptive and focuses on qualities. Quantitative data is objective and collected through surveys or experiments, while qualitative data is subjective and collected through interviews or observations.
# 
# 
# Quantitative data is numerical and measurable, while qualitative data is descriptive and non-numerical.
# 
# 
# 

# 3. Create a basic data collection that includes some sample records. Have at least one attribute from each of the machine learning data types.
# 

# In[1]:


data = [
    {"Name": "Johny", "Age": 35, "Gender": "Male", "Income": 50000, "Purchased": True},
    {"Name": "Eally", "Age": 28, "Gender": "Female", "Income": 45000, "Purchased": False},
    {"Name": "Davide", "Age": 42, "Gender": "Male", "Income": 60000, "Purchased": True}
]


# In[2]:


print(data)


# 4. What are the various causes of machine learning data issues? What are the ramifications?
# 

# Data issues in machine learning can arise from missing data, outliers, imbalanced data, inconsistent formats, duplicate data, and biased data. These issues can lead to inaccurate models, decreased performance, biased outcomes, increased costs, and ineffective decision-making. Addressing data issues is essential to ensure reliable and trustworthy machine learning results.

# 5. Demonstrate various approaches to categorical data exploration with appropriate examples.
# 

# 
# Approaches to exploring categorical data include frequency distribution (counting occurrences), bar charts (visualizing frequencies), pie charts (displaying proportions), cross tabulation (examining relationships), stacked bar charts (comparing distributions), and heatmaps (showing associations). These methods help analyze patterns and relationships within categorical variables.

# 6. How would the learning activity be affected if certain variables have missing values? Having said that, what can be done about it?
# 

# Missing values in variables can impact the learning activity by introducing bias, reducing the sample size, and distorting relationships. To address missing values, they can be deleted (if few and random), imputed (replaced with estimated values), or handled using indicator variables or model-based imputation. The choice depends on the amount and pattern of missingness, data nature, and analysis goals. Handling missing values carefully is important to minimize bias and ensure accurate analysis.

# 7. Describe the various methods for dealing with missing data values in depth.
# 

# Deletion Methods: Remove cases or variables with missing data, but it may lead to loss of information.
# 
# Imputation Methods: Replace missing values with estimated values.
# 
# Mean/Mode/Median Imputation: Replace missing values with the mean/mode/median of the variable.
# Hot Deck Imputation: Fill missing values with values from similar cases.
# Regression Imputation: Predict missing values using a regression model.
# Multiple Imputation: Generate multiple imputed datasets and combine results.
# Maximum Likelihood Estimation: Estimate missing values using statistical likelihood.
# Machine Learning-Based Methods: Use machine learning algorithms to predict missing values.
# 

# 8. What are the various data pre-processing techniques? Explain dimensionality reduction and function selection in a few words.
# 

# Dimensionality Reduction:
# 
# Reduces the number of variables while preserving important information.
# Helps with high-dimensional datasets, improving efficiency and model performance.
# Techniques include PCA, LDA, and t-SNE.
# Feature Selection:
# 
# Selects relevant features to improve model performance and interpretability.
# Eliminates irrelevant, redundant, or noisy features.
# Methods use statistical techniques or machine learning algorithms.
# Enhances accuracy, efficiency, and model generalization.

# i. What is the IQR? What criteria are used to assess it?
# 
# ii. Describe the various components of a box plot in detail? When will the lower whisker    surpass the upper whisker in length? How can box plots be used to identify outliers?
# 

#  The IQR (Interquartile Range) is a measure of statistical dispersion that represents the spread of the middle 50% of data values. It is calculated as the difference between the third quartile (Q3) and the first quartile (Q1) of a dataset. The IQR is robust to outliers and provides insights into the variability of the data.
# To assess the IQR, we consider the following criteria:
# 
# Range: The IQR indicates the range of values within which the middle 50% of the data points lie.
# Outliers: Values that fall below Q1 - 1.5 * IQR or above Q3 + 1.5 * IQR are considered potential outliers. These thresholds are often used as a criterion to identify extreme values.
#     
#     
#     
#     
#     
# Median: The line within the box represents the median, which divides the dataset into two equal halves.
# Box: The box represents the IQR, with the lower edge at Q1 and the upper edge at Q3. It contains the middle 50% of the data.
# Whiskers: The whiskers extend from the box to the minimum and maximum values that are not considered outliers. The length of the whiskers can vary.
# Outliers: Individual data points that fall outside the whiskers are considered outliers and are represented as individual points.
#     

# 1. Data collected at regular intervals
# 
# 2. The gap between the quartiles

# 1. Data collected at regular intervals refers to a dataset where observations or measurements are recorded consistently at equal time intervals. This regularity in data collection helps in analyzing patterns and trends over time, facilitating time series analysis and modeling.
# 
# 
# 
# 
# 2.The gap between the quartiles, or the interquartile range (IQR), is a measure of the spread or variability of data. It is calculated by subtracting the lower quartile (Q1) from the upper quartile (Q3). The IQR provides insights into the range of values where the middle 50% of the data points lie. A larger IQR indicates greater variability, while a smaller IQR suggests a more compact distribution.
# 
# 
# 
# 
# 

# In[ ]:




