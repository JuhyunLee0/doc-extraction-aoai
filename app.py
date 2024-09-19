import base64
import streamlit as st
import os
import json
import pandas as pd
from dotenv import load_dotenv
from streamlit_pdf_viewer import pdf_viewer

load_dotenv(override=True)

from functions.get_data import get_data, get_test_data
from functions.create_highlight import highlight_pdf

# this is static file path, you can change this to a dynamic file path
file_name = "Zurich-Quote-Teachers page 1-2.pdf"
file_path = os.path.join(os.getcwd(), "local", file_name)


# Set the page configuration
st.set_page_config(page_title="AOAI DocIntel Validator", layout="wide")

# loading data from various azure doc intel resources and azure openai
def load_data(file_path):
    # init_data = get_test_data(file_path) # for testing
    init_data = get_data(file_path)
    return init_data
 
# store the data in the session state
if 'data' not in st.session_state:
    st.session_state['data'] = load_data(file_path)

data = st.session_state['data']

if 'selected_field' not in st.session_state:
    st.session_state['selected_field'] = None

if 'highlighted_file_path' not in st.session_state:
    st.session_state['highlighted_file_path'] = file_path

# Streamlit app
st.title("AOAI Document Intelligence")

# Create two columns
col1, col2 = st.columns([1, 1])

# Display list of fields on the left side
with col1:
    pdf_viewer(input=st.session_state['highlighted_file_path'], width=700)

# Display PDF on the right side
with col2:
    st.header("Fields")
    field_names = ["Select a field"] + list(data.keys())
    selected_field_name = st.radio("Select a field to highlight", field_names, index=0)
    
    if selected_field_name != "Select a field":
        selected_field = data[selected_field_name]
    else:
        selected_field = None

    # if selected field changes, update the highlighted file
    if selected_field_name != st.session_state['selected_field']:
        st.session_state['selected_field'] = selected_field_name
        if selected_field:
            if file_name.endswith(".pdf"):
                highlighted_file_path = highlight_pdf(file_path, selected_field["extraction_from"])
            else:
                highlighted_file_path = file_path
            st.session_state['highlighted_file_path'] = highlighted_file_path
            st.rerun()

st.markdown("---")

# # Add button to export data as JSON
# if st.button("Export Data as JSON"):
#     json_data = json.dumps(data, indent=4)
#     st.download_button(label="Download JSON", data=json_data, file_name="data.json", mime="application/json")