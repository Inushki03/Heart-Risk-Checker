import streamlit as st

st.set_page_config(layout="wide")
st.markdown("""
    <style>
    .title-bar {
        text-align: center;
        margin-bottom: 18px;
    }

    .title-bar h1 {
        font-size: 28px;
        margin: 0;
    }

    .title-bar p {
        color: gray;
        margin: 4px 0 0 0;
        font-size: 14px;
    }       
    </style>
    """,
    unsafe_allow_html=True
)
from app import get_result

def main():

    st.markdown(
        """
        <div class="title-bar">
            <h1>❤️ Heart Risk Checker</h1>
            <p>Enter patient details to estimate the risk of heart disease</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.form("heart_form"):
    
        col1,col2 = st.columns(2)
        with col1:
            age=st.number_input("Age",min_value=28,max_value=100,step=1,value=40)
            Sex= st.selectbox('Sex',['M','F'])
            RestingBP=st.number_input("RestingBP",min_value=50,max_value=260,step=1,value=60)
            Cholesterol=st.number_input("Cholesterol",min_value=60,max_value=600,step=1,value=70)
            ChestPainType= st.selectbox('ChestPainType',['ATA', 'NAP', 'ASY', 'TA'])
            FastingBS=st.number_input("FastingBS",min_value=0,max_value=1,step=1,value=0,help='1:if Fasting BS > 120 mg/dl or 0:BS<=120 mg/dl')
        with col2:
            MaxHR=st.number_input("MaxHR",min_value=60,max_value=202,step=1,value=70)
            Oldpeak=st.number_input("Oldpeak",min_value=0.0,max_value=4.9,step=1.1,value=0.5)
            RestingECG= st.selectbox('RestingECG',['Normal','ST','LVH'])
            ExerciseAngina= st.selectbox('ExerciseAngina',['Y','N'])
            ST_Slope= st.selectbox('ST_Slope',['Up','Flat','Down'])

        st.markdown("""
            <style>
            div.stButton > button:first-child {
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 16px;
                
            }
            div.stButton > button:hover {
                background-color: #45a049;
            }
            </style>
            """, unsafe_allow_html=True)
        submit=st.form_submit_button("Predict Risk")
        
    if submit:
        result=get_result(age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope)
        if result == 1:
            st.markdown("### 🔴 High Chance of Heart Disease")
            st.write(
                "The model predicts a **high risk** of heart disease based on the given values. "
                "Please consult a healthcare professional for a detailed medical evaluation."
            )
        else:
            st.markdown("### 🟢 Low Chance of Heart Disease")
            st.write(
                "The model predicts a **low risk** of heart disease based on the current inputs. "
                "Maintain a healthy lifestyle and regular check-ups for long-term heart health."
            )
if __name__ =="__main__":
    main()
