import numpy as np
import pickle
import pandas as pd
import streamlit as st
from numpy import asarray
from sklearn.preprocessing import StandardScaler

 
pickle_in=open("random_forest_model.pkl","rb")
random_forest_model=pickle.load(pickle_in)
scaler=pickle.load(open("scaler.pkl","rb"))

page_bg_img = '''
<style>
body {
background-image: linear-gradient(rgba(0,0,0,0),rgba(0,0,0,0.8)),url("https://www.cube19.com/wp-content/uploads/2021/04/heartrate.jpg");
background-size: cover;
background-repeat: no-repeat;
background-attachment: fixed;

}


</style>

'''
st.markdown(
    """
<style>
.medium-font {
    border-style: inset;
    border-color: #1AEF53;
    border-width: 7px;
    font-size:20px !important;
    color:white;
    text-align:center;
    font-family: Times New Roman;

}
.big-font {
    border-style: inset;
    border-color: white;
    border-width: 7px;
    font-size:40px !important;
    color:white;
    text-align:center;
    font-family: Times New Roman;

}
.small-font {
     border-style: inset;
  border-color:#EC8484;
  border-width: 7px;
    font-size:20px !important;
    color:white;
    text-align:center;
    font-family: Times New Roman;

}
.error_class {
    font-size:25px !important;
    color:black;
    background:#ff6666;
    text-align:center;
    
}
.success_class {
    font-size:25px !important;
    color:black;
    background:#66ff66;
    text-align:center;
}
.reportview-container .markdown-text-container {
    font-family: monospace;
}
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}
.Widget>label {
    
    color:white;
    font-size:20px !important;
    font-family: Raleway Bold;
    
}
[class^="st-b"]  {
    color: black;
    font-family: monospace;
}
.slider{
    color:black
}
.st-bb {
    background-color: transparent;
}
.st-at {
    background-color: #ff5050;
}
footer {
    font-family: monospace;
}
.reportview-container .main footer, .reportview-container .main footer a {
    color: #0c0080;
}
header .decoration {
    background-image: none;
}
.val{
    font-size:10px !important;
    color:black;
    text-align:center;
}
</style>
""",
    unsafe_allow_html=True,
)




def predict_heart_failure(age,creatinine_phosphokinase,ejection_fraction,platelets,serum_creatinine,serum_sodium,time):
    
    age=scaler.transform(np.array(float(age)).reshape(1,-1))
    creatinine_phosphokinase=scaler.transform(np.array(float(creatinine_phosphokinase)).reshape(1,-1))
    ejection_fraction=scaler.transform(np.array(float(ejection_fraction)).reshape(1,-1))
    platelets=scaler.transform(np.array(float(platelets)).reshape(1,-1))
    serum_creatinine=scaler.transform(np.array(float(serum_creatinine)).reshape(1,-1))
    serum_sodium=scaler.transform(np.array(float(serum_sodium)).reshape(1,-1))
    time=scaler.transform(np.array(float(time)).reshape(1,-1))


    prediction=random_forest_model.predict([[age,creatinine_phosphokinase,ejection_fraction,platelets,serum_creatinine,serum_sodium,time]])
    if prediction==0:
     pred='Patient is safe'
    else:
     pred='Consult a Specialist'
    return pred    
      
    
   
 
def main():
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
   
    st.markdown('<p class="big-font"><b>Heart Failure Prediction</b></p>', unsafe_allow_html=True)          
    
    age=st.slider("age",min_value=1,max_value=100)
    creatinine_phosphokinase=st.text_input("creatinine_phosphokinase","0")   
    ejection_fraction=st.text_input("ejection_fraction","0")
    platelets=st.text_input("platelets","0")
    serum_creatinine=st.text_input("serum_creatinine","0")
    serum_sodium=st.text_input("serum_sodium","0")
    time=st.text_input("time","0")
    
    result=""
    
    if st.button("predict"):
         #result=predict_heart_failure(age,creatinine_phosphokinase,ejection_fraction,platelets,serum_creatinine,serum_sodium,time)
        age=scaler.transform(np.array(float(age)).reshape(-1,1))[0][0]
        creatinine_phosphokinase=scaler.transform(np.array(float(creatinine_phosphokinase)).reshape(-1,1))[0][0]
        ejection_fraction=scaler.transform(np.array(float(ejection_fraction)).reshape(-1,1))[0][0]
        platelets=scaler.transform(np.array(float(platelets)).reshape(-1,1))[0][0]
        serum_creatinine=scaler.transform(np.array(float(serum_creatinine)).reshape(-1,1))[0][0]
        serum_sodium=scaler.transform(np.array(float(serum_sodium)).reshape(-1,1))[0][0]
        time=scaler.transform(np.array(float(time)).reshape(-1,1))[0][0]
        
        test = np.array([[age,creatinine_phosphokinase,ejection_fraction,platelets,serum_creatinine,serum_sodium,time]])
        
        #st.markdown(test)

        prediction=random_forest_model.predict(test)[0]
        if prediction==0:
            st.markdown('<p class="medium-font"><b>Patient is safe</b></p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="small-font"><b>Consult a Specialist</b></p>', unsafe_allow_html=True)
              
    
            

   
        
        

    
if __name__=='__main__':
    main()
       
 



