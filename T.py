import streamlit as st
import pandas as pd

# Excel
E= "C:/Users/Hind/Desktop/IT Program Tracking Sheet.xlsx"

# لحفظ البيانات في ملف Excel 
def save_data(data):  
    df_existing = pd.read_excel(E) if pd.io.common.file_exists(E) else pd.DataFrame()  
    df_combined = pd.concat([df_existing, pd.DataFrame([data])], ignore_index=True)
    
    df_combined.to_excel(E, index=False) 
    print("Data saved successfully.")

# التحقق من Session State
if "page" not in st.session_state:
    st.session_state.page = "Data Entry"
if "submitted" not in st.session_state:
    st.session_state.submitted = False


st.title("IT Programs")

# لتنقل
if st.sidebar.button("Data Entry"):
    st.session_state.page = "Data Entry"
    st.session_state.submitted = False

if st.sidebar.button("Dashboard"):
    st.session_state.page = "Dashboard"

# إدخال البيانات
if st.session_state.page == "Data Entry":
    st.header("Program Data Entry Form")

    if st.session_state.submitted:
        st.success("Data has already been submitted.")
    else:
        # جمع البيانات  
        program_name = st.text_input("Program Name")
        responsible_dept = st.text_input("Responsible Department")
        beneficiary_group = st.multiselect("Beneficiary Group", ["Students", "Faculty", "Staff"])
        colleges = [
            "College of Arts", "College of Science", "College of Engineering",
            "College of Medicine", "College of Pharmacy", "College of Business",
            "College of Computer Science", "College of Law",
            "College of Humanities", "College of Dentistry", "College of Health Sciences"
        ]
        
        beneficiary_colleges = st.multiselect("Beneficiary Colleges", colleges)
        program_purpose = st.text_input("Program Purpose")
        license_type = st.selectbox("License Type", ["Open-source", "Paid", "In-house Developed"])
        annual_license_cost = st.number_input("Annual License Cost", min_value=0.0)
        cost_per_user = st.number_input("Cost per User", min_value=0.0)
        initial_usage_date = st.date_input("Initial Usage Date")
        available_subscriptions = st.number_input("Available Subscriptions", min_value=0)
        current_user_count = st.number_input("Current User Count", min_value=0)
        required_user_count = st.number_input("Required User Count", min_value=0)
        monthly_usage_rate = st.number_input("Monthly Usage Rate", min_value=0)
        program_performance = st.slider("Program Performance", 1, 10)
        monthly_incident_count = st.number_input("Monthly Incident Count", min_value=0)
        technical_support_level = st.selectbox("Technical Support Level", ["High", "Medium", "Low"])
        number_of_improvements = st.number_input("Number of Required Improvements per Year", min_value=0)
        current_program_state = st.selectbox("Current Program State", ["In use", "Outdated", "Needs Replacement"])
        future_viability = st.selectbox("Future Viability", ["Expand", "Phase Out"])
        total_cost_to_date = st.number_input("Total Cost to Date", min_value=0.0)
#"Submit" 
        if st.button("Submit"):
            data = {
                "Program Name": program_name,
                "Responsible Department": responsible_dept,
                "Beneficiary Group": ", ".join(beneficiary_group),
                "Beneficiary Colleges": ", ".join(beneficiary_colleges),
                "Program Purpose": program_purpose,
                "License Type": license_type,
                "Annual License Cost": annual_license_cost,
                "Cost per User": cost_per_user,
                "Initial Usage Date": initial_usage_date,
                "Available Subscriptions": available_subscriptions,
                "Current User Count": current_user_count,
                "Required User Count": required_user_count,
                "Monthly Usage Rate": monthly_usage_rate,
                "Program Performance": program_performance,
                "Monthly Incident Count": monthly_incident_count,
                "Technical Support Level": technical_support_level,
                "Number of Required Improvements per Year": number_of_improvements,
                "Current Program State": current_program_state,
                "Future Viability": future_viability,
                "Total Cost to Date": total_cost_to_date
            }

            if all(data.values()):
                print("Data to be saved:", data)
                save_data(data)
                st.session_state.submitted = True
                st.success("Data submitted successfully")
            else:
                st.error("Please fill in all fields before submitting")

# Dashboard
elif st.session_state.page == "Dashboard":
    st.header("Dashboard")