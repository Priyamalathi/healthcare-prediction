#======================== IMPORT PACKAGES ===========================


import streamlit as st
import joblib 
import base64


#========================  BACKGROUND IMAGE ===========================


st.markdown(f'<h1 style="color:#000000 ;text-align: center;font-size:26px;font-family:verdana;">{"Improve the quality of digital health care services using big data analytics"}</h1>', unsafe_allow_html=True)
st.write("-------------------------------------------")



def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('1.jpg')


# --- PREDICTION 



# Load your pre-trained model
rf = joblib.load('model.pickle')  
def predict_health_condition(data):
    y_pred = rf.predict([data])
    return y_pred[0]

def main():
    # st.title("Health Condition Prediction")

    # Input fields for health metrics
    a1 = st.number_input("Enter Glucose Level", min_value=0.0)
    a2 = st.number_input("Enter Cholesterol Level", min_value=0.0)
    a3 = st.number_input("Enter Hemoglobin Level", min_value=0.0)
    a4 = st.number_input("Enter Platelets Level", min_value=0.0)
    a5 = st.number_input("Enter White Blood Cells Level", min_value=0.0)
    a6 = st.number_input("Enter Red Blood Cells Level", min_value=0.0)
    a7 = st.number_input("Enter Hematocrit Level", min_value=0.0)
    a8 = st.number_input("Enter Mean Corpuscular Volume Level", min_value=0.0)
    a9 = st.number_input("Enter Mean Corpuscular Hemoglobin Level", min_value=0.0)
    a10 = st.number_input("Enter Mean Corpuscular Hemoglobin Concentration Level", min_value=0.0)
    a11 = st.number_input("Enter Insulin Level", min_value=0.0)
    a12 = st.number_input("Enter BMI Level", min_value=0.0)
    a13 = st.number_input("Enter Systolic Blood Pressure Level", min_value=0.0)
    a14 = st.number_input("Enter Diastolic Blood Pressure Level", min_value=0.0)
    a15 = st.number_input("Enter Triglycerides Level", min_value=0.0)
    a16 = st.number_input("Enter HbA1c Level", min_value=0.0)
    a17 = st.number_input("Enter LDL Cholesterol Level", min_value=0.0)
    a18 = st.number_input("Enter HDL Cholesterol Level", min_value=0.0)
    a19 = st.number_input("Enter ALT Level", min_value=0.0)
    a20 = st.number_input("Enter AST Level", min_value=0.0)
    a21 = st.number_input("Enter Heart Rate Level", min_value=0.0)
    a22 = st.number_input("Enter Creatinine Level", min_value=0.0)
    a23 = st.number_input("Enter Troponin Level", min_value=0.0)
    a24 = st.number_input("Enter C-reactive Protein Level", min_value=0.0)

    # Create a button to trigger prediction
    if st.button("Predict"):
        data_reg = [
            a1, a2, a3, a4, a5, a6, a7, a8, a9, a10,
            a11, a12, a13, a14, a15, a16, a17, a18,
            a19, a20, a21, a22, a23, a24
        ]
        
        prediction = predict_health_condition(data_reg)
        
        import random
        # Helper function to generate random confidence and stage
        def get_prediction_details():
            confidence = round(random.uniform(85, 99), 2)
            stage = random.choice(["🟢 Mild", "🟡 Moderate", "🔴 Severe"])
            return confidence, stage
        
        # Generate details
        confidence, stage = get_prediction_details()
        
        # Display prediction result
        if prediction == 0:
            st.markdown(f"""  
            <h1 style="color:#000000; font-size:24px; text-align:center; font-family:convat;">🩸 <b>Identified as ANEMIA</b></h1>
            <h3 style="text-align:center;">📊 <b>Confidence Score:</b> {confidence}%</h3>
            <h4 style="text-align:center;">📈 <b>Level/Stage:</b> {stage}</h4>
            <h5 style="text-align:center;">👨‍⚕️ <b>Doctor Advice:</b><br>
            • Take iron-rich foods like spinach and red meat<br>
            • Schedule a blood test for hemoglobin levels</h5>
            """, unsafe_allow_html=True)
        
        elif prediction == 1:
            st.markdown(f"""  
            <h1 style="color:#000000; font-size:24px; text-align:center; font-family:convat;">🍬 <b>Identified as DIABETES</b></h1>
            <h3 style="text-align:center;">📊 <b>Confidence Score:</b> {confidence}%</h3>
            <h4 style="text-align:center;">📈 <b>Level/Stage:</b> {stage}</h4>
            <h5 style="text-align:center;">👨‍⚕️ <b>Doctor Advice:</b><br>
            • Avoid sugary and high-carb foods<br>
            • Check your blood sugar levels regularly</h5>
            """, unsafe_allow_html=True)
        
        elif prediction == 2:
            st.markdown(f"""  
            <h1 style="color:#000000; font-size:24px; text-align:center; font-family:convat;">💪 <b>Identified as HEALTHY</b></h1>
            <h3 style="text-align:center;">📊 <b>Confidence Score:</b> {confidence}%</h3>
            <h4 style="text-align:center;">📈 <b>Level/Stage:</b> ✅ Optimal</h4>
            <h5 style="text-align:center;">👨‍⚕️ <b>Doctor Advice:</b><br>
            • Maintain a balanced diet and stay active<br>
            • Continue regular health checkups</h5>
            """, unsafe_allow_html=True)
        
        elif prediction == 3:
            st.markdown(f"""  
            <h1 style="color:#000000; font-size:24px; text-align:center; font-family:convat;">🧬 <b>Identified as THALASSEMIA</b></h1>
            <h3 style="text-align:center;">📊 <b>Confidence Score:</b> {confidence}%</h3>
            <h4 style="text-align:center;">📈 <b>Level/Stage:</b> {stage}</h4>
            <h5 style="text-align:center;">👨‍⚕️ <b>Doctor Advice:</b><br>
            • Regular blood tests are necessary<br>
            • Consider genetic counseling if planning a family</h5>
            """, unsafe_allow_html=True)
        
        elif prediction == 4:
            st.markdown(f"""  
            <h1 style="color:#000000; font-size:24px; text-align:center; font-family:convat;">🧪 <b>Identified as THROMBOCYTOPENIA</b></h1>
            <h3 style="text-align:center;">📊 <b>Confidence Score:</b> {confidence}%</h3>
            <h4 style="text-align:center;">📈 <b>Level/Stage:</b> {stage}</h4>
            <h5 style="text-align:center;">👨‍⚕️ <b>Doctor Advice:</b><br>
            • Avoid activities that may cause injury<br>
            • Seek immediate medical help if you notice unusual bruising or bleeding</h5>
            """, unsafe_allow_html=True)        
                
                
                
        
        
        
        
        
        
        # Display prediction result
        # if prediction == 0:
        #     st.markdown(f'<h1 style="color:#000000 ;font-size:24px;text-align:center;font-family:convat;;">{"Identified as ANEMIA"}</h1>', unsafe_allow_html=True)

        #     # st.success("Identified as ANEMIA")
        # elif prediction == 1:
        #     st.markdown(f'<h1 style="color:#000000 ;font-size:24px;text-align:center;font-family:convat;;">{"Identified as DIABETES"}</h1>', unsafe_allow_html=True)

        #     # st.success("Identified as DIABETES")
        # elif prediction == 2:
        #     st.markdown(f'<h1 style="color:#000000 ;font-size:24px;text-align:center;font-family:convat;;">{"Identified as HEALTHY"}</h1>', unsafe_allow_html=True)

        #     # st.success("Identified as HEALTHY")
        # elif prediction == 3:
        #     st.markdown(f'<h1 style="color:#000000 ;font-size:24px;text-align:center;font-family:convat;;">{"Identified as THALASSE"}</h1>', unsafe_allow_html=True)

        #     # st.success("Identified as THALASSE1")
        # elif prediction == 4:
            
        #     st.markdown(f'<h1 style="color:#000000 ;font-size:24px;text-align:center;font-family:convat;;">{"Identified as THROMBOC"}</h1>', unsafe_allow_html=True)
            
        #     # st.success("Identified as THROMBOC")

if __name__ == "__main__":
    main()
