import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# -------------------------------
# Simulated training data
# -------------------------------
X = np.array([
    [200, 25, 7],
    [150, 22, 6],
    [300, 28, 8],
    [100, 20, 5],
    [250, 26, 7]
])

y = np.array([2.5, 1.8, 3.2, 1.2, 2.8])

# Train model
model = LinearRegression()
model.fit(X, y)

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🌾 Crop Yield Prediction App")

st.write("Enter the agricultural parameters below to estimate crop yield:")

rainfall = st.number_input(
    "Rainfall (mm)",
    min_value=50,
    max_value=500,
    value=200
)

temperature = st.number_input(
    "Temperature (°C)",
    min_value=10,
    max_value=40,
    value=25
)

soil_quality = st.slider(
    "Soil Quality Index (1-10)",
    1,
    10,
    7
)

# Prediction
if st.button("Predict Yield"):
    input_data = np.array([[rainfall, temperature, soil_quality]])
    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Crop Yield: {prediction:.2f} tons/hectare"
    )
