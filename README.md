# Heart-Failure-Prediction

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




