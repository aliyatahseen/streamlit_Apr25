import streamlit as st
import pandas as pd
import os
import pickle
# Get the full path to the current script and build path to CSV
base_path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_path, "car_price.csv")

# Show the computed file path in the Streamlit app
st.write("Full path to CSV:", csv_path)

# Try to read the CSV
try:
    cars_df = pd.read_csv(csv_path)
    st.success("CSV loaded successfully!")
except FileNotFoundError as e:
    st.error(f"File not found: {e}")
except Exception as e:
    st.error(f"Unexpected error: {e}")

st.title("Car Resale Price Prediction")
st.dataframe(cars_df.head())

model_path = os.path.join(os.path.dirname(__file__), "car_pred")
with open(model_path, "rb") as f:
    model = pickle.load(f)



# sklearn model which is trained on cars24 data.



col1, col2 = st.columns(2)

# dropdown
fuel_type = col1.selectbox("Select the fuel type",
                           ["Diesel", "Petrol", "CNG", "LPG", "Electric"])

engine = col1.slider("Set the Engine Power",
                     500, 5000, step=100)

transmission_type = col2.selectbox("Select the transmission type",
                                   ["Manual", "Automatic"])

seats = col2.selectbox("Enter the number of seats",
                       [4,5,7,9,11])


## Encoding Categorical features
## Use the same encoding as used during the training. 
encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "seller_type": {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
}


if st.button("Get Price"):
    # predict here

    encoded_fuel_type = encode_dict['fuel_type'][fuel_type]
    encoded_transmission_type = encode_dict['transmission_type'][transmission_type]

    input_car = [2012.0,2,120000,encoded_fuel_type,encoded_transmission_type,19.7,engine,46.3,seats]
    price = model.predict([input_car])[0]

    st.header(round(price,2))
