# import streamlit as st
# import time as t
# import pandas as pd
# import numpy as np

# st.sidebar.title("WELCOME TO MY WEBSITE")
# st.sidebar.markdown("# Login")
# log = st.sidebar.text_input("email")
# if log :
#     if log.isalnum():
#         st.sidebar.error("Enter valid email")

    

# pas = st.sidebar.text_input("password")
# if(pas):
#     if len(pas) < 8 :
#         st.sidebar.error("Enter valid password")

# st.sidebar.write("password must be 8 letter")
# sub = st.sidebar.button("click")
# if sub :
#     if sub :
#         st.sidebar.success("Submited successfuly")
#         st.image("pgmcoe.webp")
#         st.title(" BASIC INFORMATION FORM")

#         st.file_uploader("upload ur identicard")
#         st.text_input("Enter Your Surname Name : ")
#         st.text_input("Enter Your Name : ")
#         st.text_input("Enter Your Father Name : ")
#         mobile_number = st.text_input("Enter your mobile number:")
#         if mobile_number:
#             if len(mobile_number) == 10 and mobile_number.isdigit():
#                 st.success(f"Valid mobile number: {mobile_number}")
#             else:
#                 st.error("Enter a valid 10-digit mobile number.")


#         st.radio("select your gender ",["male","female","other"])
#         st.date_input("Enter your bith date")
#         st.selectbox("select your branch",["cs","IT","AIDS","ENTC","MACH","CIVIL"])

#         st.select_slider("currenty studing in which year :",["1st","2nd","3rd","4th"])

#         st.button("submit")







# # st.image("pgmcoe.webp")
# # st.title(" BASIC INFORMATION FORM")

# # st.file_uploader("upload ur identicard")
# # st.text_input("Enter Your Surname Name : ")
# # st.text_input("Enter Your Name : ")
# # st.text_input("Enter Your Father Name : ")
# # mobile_number = st.text_input("Enter your mobile number:")
# # if mobile_number:
# #     if len(mobile_number) == 10 and mobile_number.isdigit():
# #         st.success(f"Valid mobile number: {mobile_number}")
# #     else:
# #         st.error("Enter a valid 10-digit mobile number.")


# # st.radio("select your gender ",["male","female","other"])
# # st.date_input("Enter your bith date")
# # st.selectbox("select your branch",["cs","IT","AIDS","ENTC","MACH","CIVIL"])

# # st.select_slider("currenty studing in which year :",["1st","2nd","3rd","4th"])

# # st.button("submit")

import streamlit as st
import wikipediaapi

# Initialize Wikipedia API with a user-agent
wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent="YourAppName/1.0 (https://yourwebsite.com/; your-email@example.com)"
)

# Sidebar title and login
st.sidebar.title("WELCOME TO MY WEBSITE")
st.sidebar.markdown("# Login")

# Email input with validation
log = st.sidebar.text_input("Email")
if log:
    if not ("@" in log and "." in log):
        st.sidebar.error("Enter a valid email")

# Password input with validation
pas = st.sidebar.text_input("Password", type="password")
if pas:
    if len(pas) < 8:
        st.sidebar.error("Enter a valid password")
st.sidebar.write("Password must be at least 8 characters.")

# Submit button
sub = st.sidebar.button("Submit")
if sub:
    if log and pas and ("@" in log and "." in log) and len(pas) >= 8:
        st.sidebar.success("Login successful!")
    else:
        st.sidebar.error("Please provide valid login details.")

# Main Section: Patient Details
st.title("Patient Details Form")

# Patient details input
name = st.text_input("Name")
age = st.number_input("Age", min_value=0, max_value=120, step=1)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
address = st.text_area("Address")
mobile = st.text_input("Mobile Number")
if mobile:
    if not mobile.isdigit() or len(mobile) != 10:
        st.error("Enter a valid 10-digit mobile number.")

# Symptoms dropdown
symptoms = st.multiselect(
    "Symptoms",
    options=["Cough", "Sneezing", "Fever", "Headache", "Stomach Pain", "Other"]
)

# Description of symptoms
description = st.text_area("Description of Symptoms", placeholder="Describe the symptoms in detail...")

# Dummy doctor list based on symptoms
doctor_mapping = {
    "Cough": "Dr. Smith (Pulmonologist)",
    "Sneezing": "Dr. Allen (Allergist)",
    "Fever": "Dr. Brown (General Physician)",
    "Headache": "Dr. Taylor (Neurologist)",
    "Stomach Pain": "Dr. Davis (Gastroenterologist)",
    "Other": "Dr. Wilson (General Practitioner)"
}

# Assign doctors based on symptoms
assigned_doctors = set()
for symptom in symptoms:
    assigned_doctors.add(doctor_mapping.get(symptom, "Dr. Wilson (General Practitioner)"))

# Function to fetch precautions from Wikipedia
def fetch_precautions(query):
    page = wiki_wiki.page(query)
    if page.exists():
        return page.summary[:500]  # Limit summary to 500 characters
    else:
        return "No precautions found for this description."

# Submit button for patient details
submit_details = st.button("Submit Details")
if submit_details:
    if name and age and gender and address and mobile and symptoms and description:
        st.success("Patient details submitted successfully!")
        st.write("### Patient Summary")
        st.write(f"**Name:** {name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Address:** {address}")
        st.write(f"**Mobile Number:** {mobile}")
        st.write(f"**Symptoms:** {', '.join(symptoms)}")
        st.write(f"**Description of Symptoms:** {description}")

        # Display assigned doctors
        st.write("### Assigned Doctor(s):")
        for doctor in assigned_doctors:
            st.write(f"- {doctor}")

        # Fetch and display precautions
        st.write("### Precautions Based on Description:")
        precautions = fetch_precautions(description)
        st.write(precautions)
    else:
        st.error("Please fill out all fields before submitting.")
