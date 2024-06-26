import streamlit as st
import pickle

# Load your trained machine learning model
model = pickle.load(open('DecisionTree_classification.sav', 'rb'))

def predict_fault(phase_a_current, phase_b_current, phase_c_current):
  """
  Predicts the fault type based on the input current data.

  Args:
      phase_a_current: Phase A current value (Amperes).
      phase_b_current: Phase B current value (Amperes).
      phase_c_current: Phase C current value (Amperes).

  Returns:
      The predicted fault type as a string.
  """

  # Prepare the input data based on your model's expectations
  # Assuming your model expects a 2D array with each row being a sample
  # (modify if necessary according to your model's requirements)
  data = [[phase_a_current, phase_b_current, phase_c_current]]

  prediction = model.predict(data)[0]

  # Map the prediction to the corresponding fault type using your provided mapping
  fault_type_mapping = {
      '14': 'NO Fault',
      '13': 'Line A Fault',
      '12': 'Line B Fault',
      '11': 'Line C Fault',
      '10': 'Line A to Ground Fault',
      '9': 'Line B to Ground Fault',
      '8': 'Line C to Ground Fault',
      '7': 'Line A Line B to Ground Fault',
      '6': 'Line A Line C to Ground Fault',
      '5': 'Line B Line C to Ground Fault',
      '4': 'Line A to Line B fault',
      '3': 'Line A to Line C Fault',
      '2': 'Line B to Line C Fault',
      '1': 'Line A Line B Line C',
      '0': 'Line A Line B Line C to Ground Fault',
  }

  return fault_type_mapping.get(prediction, 'Unknown Fault')

st.title("Three-Phase Fault Classifier")

# Get user input for three-phase current values
phase_a_current = st.number_input("Phase A Current (A)", min_value=0.0)
phase_b_current = st.number_input("Phase B Current (A)", min_value=0.0)
phase_c_current = st.number_input("Phase C Current (A)", min_value=0.0)

# Make prediction when the button is clicked
if st.button("Classify Fault"):
  predicted_fault = predict_fault(phase_a_current, phase_b_current, phase_c_current)
  st.write(f"Predicted Fault Type: {predicted_fault}")
