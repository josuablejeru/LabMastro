"""Web Application main entry point."""

import streamlit as st

st.title("LabMastro")

st.area_chart([1, 2, 3, 4, 5])


voltage_input = st.number_input(
    label="Voltage",
    min_value=0.0,
    max_value=60.0,
    step=0.01,
)

ampere_input = st.number_input(
    label="Amps",
    min_value=0.0,
    max_value=5.0,
    step=0.001,
)
voltage, ampere = st.columns(2)
voltage.metric("Voltage", voltage_input)
ampere.metric("Ampere", ampere_input)
