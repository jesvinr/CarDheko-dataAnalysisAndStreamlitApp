import streamlit as st

# Inject custom CSS for styling
st.markdown("""
    <style>
    /* Style the title */
    .title {
        font-family: 'Arial Black', sans-serif;
        color: #333333;
        font-size: 36px;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Style the input labels */
    label {
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        color: #444444;
    }

    /* Style the submit button */
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 18px;
        font-family: 'Arial', sans-serif;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }

    /* Hover effect for the submit button */
    .stButton button:hover {
        background-color: #45a049;
    }

    /* Style the results */
    .result {
        background-color: #f9f9f9;
        border-left: 5px solid #4CAF50;
        padding: 10px;
        margin-top: 20px;
        font-family: 'Arial', sans-serif;
    }

    /* Error message */
    .error {
        color: red;
        font-weight: bold;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.markdown('<div class="title">Car Information Submission Form</div>', unsafe_allow_html=True)

# Car brand input
car_brand = st.text_input('Car Brand')
kilometersTraveled = st.number_input('kilometersTraveled')
transmission = st.selectbox('transmission', ['automatic', 'manual'])
# (constraint: must be less than 5)
nth_owner = st.number_input('Number of Owners', min_value=1, max_value=5, step=1)
oem = st.text_input('Brand')
model = st.text_input('model')
model_year = st.number_input('Model Year', min_value=1980, max_value=2024, step=1)
registration_year = st.number_input('Registration Year', min_value=1980, max_value=2024, step=1)
insuranceValidity = st.selectbox('Insurance validity',['third party', 'comprehensive', 'zero dep', 'not available',
       'insurance validity', '2', '1'])
car_fueltype = st.selectbox('Fuel Type', ['petrol', 'diesel', 'electric', 'cng', 'lpg'])
seats = st.number_input('Seats', min_value=2, max_value=10, step=1)
engineDisplacement  = st.number_input('Engine Displacement', min_value=0, max_value=2000)
yearOfManufacture   = st.number_input("Year of manufacture",  min_value=1980, max_value=2024, step=1)
noOfCylinder        = st.number_input("No of cylinder", min_value=3, max_value=8, step=1)
valuesPerCylinder   = st.number_input("No of cylinder", min_value=2, max_value=4, step=1)
turboCharger        = st.selectbox('Turbo changer', ['yes', 'no','twin'])
superCharger        = st.selectbox('Super changer', ['yes', 'no'])
length              = st.number_input("length", min_value=2974, max_value=5453)
width               = st.number_input("width", min_value=1410, max_value=2220)
height              = st.number_input("height", min_value=1300, max_value=1995)
gearBox             = st.selectbox('Gear box', ['7', '5', '8', '6', 'c', '9', 'f', '4', 'i', 'a', 's', 'e', 'd',
                                    '1', 'm'])
driveType           = st.selectbox('Drive Type', ['fwd', 'rwd', 'awd', '4x2', '2wd', '4wd', '4x4', 'rwd with esp',
                            'all wheel drive', 'awd integrated management', 'rwd with mtt','4 wd'])
steeringType        = st.selectbox('Steering type', ['electric', 'manual', 'electronic', 'power', 'electrical', 'epas',
                            'hydraulic'])
turningRadius       = st.number_input("turningRadius", min_value=4.0, max_value=12.0, step=0.1)
tyreType            = st.selectbox("Tyre type", ['tubeless radial', 'tubeless', 'radial', 'tubeless runflat',
                            'runflat', 'radialwithtube', 'tubeless mud terrain','runflat,radial', 'tubelessallterrain'])
numOfDoors          = st.number_input("Number Of Doors", min_value=2, max_value=6, step=1)
city                = st.selectbox("City", ['chennai', 'bangalore', 'delhi', 'hyderabad', 'jaipur'])



# Submit button
if st.button('Submit'):
    # Constraint: model_year should be <= registration_year
    if model_year > registration_year:
        st.markdown('<div class="error">Error: Model year cannot be greater than registration year.</div>', unsafe_allow_html=True)
    else:

        from sklearn.preprocessing import LabelEncoder, StandardScaler
        import pandas as pd
        import pickle
        import numpy as np

        with open('D:\\python\\VsCodePythonWorkplace\\car_dheko_project\\datasets\\carDhekoModelWithEncoder.pkl', 'rb') as file:
            data = pickle.load(file)

        rf = data['model']
        label_encoders = data['label_encoders']
        scaler = data['scaler']

        # User inputs from the form
        user_inputs = [
            car_brand,              # 'brand type'
            kilometersTraveled,      # 'km'
            nth_owner,              # 'ownerno'
            oem,                    # 'oem'
            model,                  # 'model'
            model_year,             # 'modelyear'
            registration_year,       # 'registration year'
            insuranceValidity,       # 'insurance validity'
            car_fueltype,            # 'fuel type'
            seats,                  # 'seats'
            transmission,           # 'transmission'
            yearOfManufacture,       # 'year of manufacture'
            engineDisplacement,      # 'displacement'
            noOfCylinder,            # 'no of cylinder'
            valuesPerCylinder,       # 'values per cylinder'
            turboCharger,            # 'turbo charger'
            superCharger,            # 'super charger'
            length,                 # 'length'
            width,                  # 'width'
            height,                 # 'height'
            gearBox,                # 'gear box'
            driveType,              # 'drive type'
            steeringType,           # 'steering type'
            turningRadius,          # 'turning radius'
            tyreType,               # 'tyre type'
            numOfDoors,             # 'no door numbers'
            city                    # 'city'
        ]

        # Column names
        columns = [
            'brand type', 'km', 'ownerno', 'oem', 'model', 'modelyear',
            'registration year', 'insurance validity', 'fuel type', 'seats',
            'transmission', 'year of manufacture', 'displacement', 'no of cylinder',
            'values per cylinder', 'turbo charger', 'super charger', 'length',
            'width', 'height', 'gear box', 'drive type', 'steering type',
            'turning radius', 'tyre type', 'no door numbers', 'city'
        ]

        # Creating the dictionary by zipping columns and user inputs
        user_input_dict = dict(zip(columns, user_inputs))

        # Creating a DataFrame with the user inputs
        user_input_df = pd.DataFrame([user_input_dict])

        print(user_input_df)
        
        # Standardize numeric columns
        car_numeric_cols = user_input_df.select_dtypes(include=['int64', 'float64', 'int32']).columns
        user_input_df[car_numeric_cols] = scaler.transform(user_input_df[car_numeric_cols])

        car_categorical_cols = user_input_df.select_dtypes(include='object').columns
        user_input_df[car_categorical_cols] = user_input_df[car_categorical_cols].astype(str)

    
        print(user_input_df)

        # Encode categorical columns using the saved LabelEncoders
        for col in car_categorical_cols:
            le = label_encoders[col]  # Retrieve the encoder
            user_input_df[col] = le.transform(user_input_df[col])
        
        print(user_input_df)
        predicted_price = int(rf.predict(user_input_df))

        # st.write("### User Input Summary:")
        # st.write(f"**Car Brand:** {car_brand}")
        # st.write(f"**Kilometers Traveled:** {kilometersTraveled}")
        # st.write(f"**Transmission:** {transmission}")
        # st.write(f"**Number of Owners:** {nth_owner}")
        # st.write(f"**OEM:** {oem}")
        # st.write(f"**Model:** {model}")
        # st.write(f"**Model Year:** {model_year}")
        # st.write(f"**Registration Year:** {registration_year}")
        # st.write(f"**Insurance Validity:** {insuranceValidity}")
        # st.write(f"**Fuel Type:** {car_fueltype}")
        # st.write(f"**Seats:** {seats}")
        # st.write(f"**Engine Displacement:** {engineDisplacement}")
        # st.write(f"**Year of Manufacture:** {yearOfManufacture}")
        # st.write(f"**Number of Cylinders:** {noOfCylinder}")
        # st.write(f"**Values per Cylinder:** {valuesPerCylinder}")
        # st.write(f"**Turbocharger:** {turboCharger}")
        # st.write(f"**Supercharger:** {superCharger}")
        # st.write(f"**Length:** {length}")
        # st.write(f"**Width:** {width}")
        # st.write(f"**Height:** {height}")
        # st.write(f"**Gearbox:** {gearBox}")
        # st.write(f"**Drive Type:** {driveType}")
        # st.write(f"**Steering Type:** {steeringType}")
        # st.write(f"**Turning Radius:** {turningRadius}")
        # st.write(f"**Tyre Type:** {tyreType}")
        # st.write(f"**Number of Doors:** {numOfDoors}")
        # st.write(f"**City:** {city}")
        st.write(f"**Price:** {predicted_price}")

"""
Note: While inputing test-feild, write in lowercase
"""