import streamlit as st

# Adding title with custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #f0f5f5;
        color: #000000;
    }
    .stApp {
        background: linear-gradient(105deg, #f0f5f5);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: black;
    }
    .stButton>button {
        background: linear-gradient(45deg, #0b5394, #351c75);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.1);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }
    .result-box {
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.3);
        padding: 25px;
        border-radius: 15px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 16px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1>Unit Converter</h1>", unsafe_allow_html=True)
st.write("Easily Convert Between Different Units Using This Streamlit App")

# Sidebar menu
conversion_type = st.sidebar.selectbox("Select Type of Conversion", ["Length", "Weight", "Temperature", "Volume"])

value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

# Define unit selection
units = {
    "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "MicroMeter", "Nanometer", "Miles", "Yard", "Foot", "Inch"],
    "Weight": ["Kilogram", "Gram", "Milligram", "Microgram", "Ton", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Volume": ["Liter", "Milliliter", "Gallon", "Quart", "Pint", "Cup", "Ounce", "Tablespoon", "Teaspoon"]
}

with col1:
    unit_from = st.selectbox("From", units[conversion_type])
with col2:
    unit_to = st.selectbox("To", units[conversion_type])

# Conversion Functions
def length_converter(value, unit_from, unit_to):
    length_units = {
        'Meter': 1, 'Kilometer': 0.001, 'Centimeter': 100, 'Millimeter': 1000,
        'MicroMeter': 1e6, 'Nanometer': 1e9, 'Miles': 0.000621371,
        'Yard': 1.09361, 'Foot': 3.28084, 'Inch': 39.3701
    }
    return (value / length_units[unit_from]) * length_units[unit_to]

def weight_converter(value, unit_from, unit_to):
    weight_units = {
        'Kilogram': 1, 'Gram': 1000, 'Milligram': 1e6, 'Microgram': 1e9,
        'Ton': 0.001, 'Pound': 2.20462, 'Ounce': 35.274
    }
    return (value / weight_units[unit_from]) * weight_units[unit_to]

def temperature_converter(value, unit_from, unit_to):
    if unit_from == "Celsius":
        return (value * 9/5 + 32) if unit_to == "Fahrenheit" else value + 273.15 if unit_to == "Kelvin" else value
    elif unit_from == "Fahrenheit":
        return (value - 32) * 5/9 if unit_to == "Celsius" else (value - 32) * 5/9 + 273.15 if unit_to == "Kelvin" else value
    elif unit_from == "Kelvin":
        return value - 273.15 if unit_to == "Celsius" else (value - 273.15) * 9/5 + 32 if unit_to == "Fahrenheit" else value

def volume_converter(value, unit_from, unit_to):
    volume_units = {
        'Liter': 1, 'Milliliter': 1000, 'Gallon': 0.264172, 'Quart': 1.05669,
        'Pint': 2.11338, 'Cup': 4.22675, 'Ounce': 33.814, 'Tablespoon': 67.268, 'Teaspoon': 202.884
    }
    return (value / volume_units[unit_from]) * volume_units[unit_to]

# Convert Button
if st.button("Convert"):
    if conversion_type == "Length":
        result = length_converter(value, unit_from, unit_to)
    elif conversion_type == "Weight":
        result = weight_converter(value, unit_from, unit_to)
    elif conversion_type == "Temperature":
        result = temperature_converter(value, unit_from, unit_to)
    elif conversion_type == "Volume":
        result = volume_converter(value, unit_from, unit_to)
    
    st.markdown(f"<div class='result-box'>{value} {unit_from} = {result:.4f} {unit_to}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Created By: Asad Jilani GIAIC (7534) Email : a.jee1975@gmail.com </div>", unsafe_allow_html=True)
