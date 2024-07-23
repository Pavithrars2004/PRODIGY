import streamlit as st

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def convert_temperature(value, unit):
    if unit.lower() == 'c':
        return {
            "Fahrenheit": celsius_to_fahrenheit(value),
            "Kelvin": celsius_to_kelvin(value)
        }
    elif unit.lower() == 'f':
        return {
            "Celsius": fahrenheit_to_celsius(value),
            "Kelvin": fahrenheit_to_kelvin(value)
        }
    elif unit.lower() == 'k':
        return {
            "Celsius": kelvin_to_celsius(value),
            "Fahrenheit": kelvin_to_fahrenheit(value)
        }
    else:
        return None

st.title("Temperature Converter")

value = st.number_input("Enter the temperature value:")
unit = st.selectbox("Select the unit of temperature:", ["Celsius (C)", "Fahrenheit (F)", "Kelvin (K)"])

unit_short = unit[0].lower()

if st.button("Convert"):
    results = convert_temperature(value, unit_short)
    if results:
        st.write(f"Converted Temperatures:")
        for scale, temp in results.items():
            st.write(f"{scale}: {temp:.2f}")
    else:
        st.write("Invalid unit. Please select a valid unit.")
