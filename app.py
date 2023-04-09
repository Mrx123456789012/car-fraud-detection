import streamlit as st 
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
# Load the machine learning model
import warnings

warnings.filterwarnings("ignore", message="Trying to unpickle estimator DecisionTreeClassifier from version 1.1.1 when using version 1.2.2")
warnings.filterwarnings("ignore", message="Trying to unpickle estimator RandomForestClassifier from version 1.1.1 when using version 1.2.2")

model = joblib.load("C:/Users/Md Shadan/Downloads/data_science_website/.venv/random_forest_model3.joblib") 

st.write('Please enter the following details to check for fraud:')
st.write('- Incident Type: Multi-vehicle Collision-3, Parked Car-4, Single Vehicle Collision-5, Vehicle Theft-6')
st.write('- Incident Severity: major damage-1, minor damage-2, total loss-3, trivial damage-4')
st.write('- Authorities Contacted: ambulance-5, fire-6, none-7, other-8, police-9')
st.write('- Collision Type: front-0, rear-1, side-2, unknown-3')
st.write('- Insured Sex: male-1, female-0')

# Rest of the code goes here


st.sidebar.header('Enter Incident Data')
incident_type = st.sidebar.selectbox('Incident Type', ['1', '2', '3', '4', '5'])
police_report_available = st.sidebar.selectbox('Police Report Available', ['0', '1', '2'])
number_of_vehicles_involved = st.sidebar.number_input('Number of Vehicles Involved', min_value=0, max_value=10, step=1)
incident_severity = st.sidebar.selectbox('Incident Severity', ['1', '2', '3', '4'])
injury_claim = st.sidebar.number_input('Injury Claim', min_value=0, max_value=100000, step=100)
vehicle_claim = st.sidebar.number_input('Vehicle Claim', min_value=0, max_value=100000, step=100)
total_claim_amount = st.sidebar.number_input('Total Claim Amount', min_value=0, max_value=100000, step=100)
property_claim = st.sidebar.number_input('Property Claim', min_value=0, max_value=100000, step=100)
witnesses = st.sidebar.number_input('Witnesses', min_value=0, max_value=10, step=1)
authorities_contacted = st.sidebar.selectbox('Authorities Contacted', ['1', '2', '3', '4', '5'])
collision_type = st.sidebar.selectbox('Collision Type', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
Capital_Loss= st.sidebar.number_input('Capital Loss', min_value=-100000, max_value=0, step=100)
Capital_Gain = st.sidebar.number_input('Capital Gain', min_value=0, max_value=100000, step=100)
insured_sex = st.sidebar.selectbox('Insured Sex', ['0', '1'])

# Make predictions
if st.sidebar.button('Predict Fraud'):
    try:
        data = {'incident_type': incident_type,
                'police_report_available': police_report_available,
                'number_of_vehicles_involved': number_of_vehicles_involved,
                'incident_severity': incident_severity,
                'injury_claim': injury_claim,
                'vehicle_claim': vehicle_claim,
                'total_claim_amount': total_claim_amount,
                'property_claim': property_claim,
                'witnesses': witnesses,
                'authorities_contacted': authorities_contacted,
                'collision_type': collision_type,
                'Capital_Loss': Capital_Loss,
                'Capital_Gain': Capital_Gain,
                'insured_sex': insured_sex}
        input_data = pd.DataFrame(data, index=[0])
        prediction = model.predict(input_data)
        if prediction[0] == 1:
            st.write('Fraud detected')
        else:
            st.write('Fraud not detected')
    except Exception as e:
        st.error('An error occurred while making predictions: {}'.format(e))
