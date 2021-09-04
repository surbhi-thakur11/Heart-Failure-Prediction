# Heart-Failure-Prediction

![Frequent-drinking-is-greater-risk-factor-fR-heart-rhythM](https://user-images.githubusercontent.com/77155721/132086338-b3288aab-bca5-49ed-89dc-6c56422886a0.jpg)


## Objective: 
There are some factors that affects Death Event. This dataset contains person's information like age ,sex , blood pressure, smoke, diabetes,ejection fraction, creatinine phosphokinase, serum_creatinine, serum_sodium, time and we have to predict their DEATH EVENT.

## Dataset Link: 
https://www.kaggle.com/andrewmvd/heart-failure-clinical-data

## Columns: 

 Age: Age of the patient in years
Anaemia: Decrease of red blood cells or hemoglobin (0:Reduced or 1:Normal)
creatinine_phosphokinase: Level of the CPK enzyme in the blood (mcg/L)
Diabetes: If the patient has diabetes (0:No or 1:Yes)
ejection_fraction: Percentage of blood leaving the heart at each contraction (percentage)
high_blood_pressure: If the patient has hypertension (0:No or 1:Yes)
platelets: Platelets in the blood (kiloplatelets/mL)
serum_creatinine: Level of serum creatinine in the blood (mg/dL)
serum_sodium: Level of serum sodium in the blood (mEq/L)
sex: Biological sex of the patient (0:Female or 1:Male)
smoking: If the patient is a smoker (0:No or 1: Yes)
time: Follow-up period in days
death_event: If the patient survived till the end of follow-up period (0:No or 1:Yes )

## Steps Followed:

![Screenshot 2021-09-04 123652](https://user-images.githubusercontent.com/77155721/132086024-88bc0c93-6b77-481c-b465-aa19d5d200e3.png)

Column’s anaemia, diabetes, high blood pressure and smoking are Boolean type
Rest of the columns except sex are numeric.
sex is a categorical column with only 2 values (Male: 0 and Female: 1). Since there are only 2
categories, we need not do any hot encoding and we can leave them as they are.
DEATH_EVENT is our label column

After EDA and Data Preprocessing 

## Feature Selection
Lets find out what features are relevant for predicting heart failure.
We can do this in two ways:
1.Plotting a correlation wrt death event and visualizing each feature wrt Death Event and see if there
is any correlation
2.Using feature importance in ensemble techniques

Correlation only works in case of non-categorical data. So it needs additional effort for checking
relation between categorical data and label.
![image](https://user-images.githubusercontent.com/77155721/132086121-11876f4a-0f7c-4458-b4a8-e9e8f7dd94df.png)

'time' is the most influential variable.
'serum creatinine', 'ejection fraction', 'age', 'creatinine phosphokinase', 'platelets', 'serum sodium' are

looking important in the specified order. All these numerical features and as we saw from the chi-
square tests earlier, the categorical features are not so important.

![image](https://user-images.githubusercontent.com/77155721/132086154-7a77200e-7bb6-4a32-bea7-56ee22484448.png)

After Feature Selection, we applied Feature Scaling and then made the model with the best possible algorithm.
Random Forest gave the best results.

And then I dumped the model into pickle file for deployment and to prepare the .py file. 

## Final Model after Deployment
![Screenshot 2021-09-04 124402](https://user-images.githubusercontent.com/77155721/132086251-947c4635-f297-40c8-baa2-52e73ca5bec8.png)

## Links
Deployed Model: https://share.streamlit.io/surbhi-thakur11/heart-failure-prediction/main/temp.py

Dataset Link: https://www.kaggle.com/andrewmvd/heart-failure-clinical-data


LinkedIn video: https://www.linkedin.com/posts/surbhi-thakur11_datascience-python-internship-activity-6804667185840099328-ImcU



