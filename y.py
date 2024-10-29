import streamlit as st
import pandas as pd

# وظيفة لحفظ البيانات في ملف Excel محلي
def save_data(data):
    try:
        # تحميل البيانات الحالية إذا كان الملف موجودًا
        df_existing = pd.read_excel("C:/Users/Hind/Desktop/IT Program Tracking Sheet.xlsx")  # تأكد من تعديل المسار
    except FileNotFoundError:
        # إذا كان الملف غير موجود، إنشاء DataFrame فارغ
        df_existing = pd.DataFrame()
    
    # إضافة البيانات الجديدة
    df = pd.DataFrame([data])
    df_combined = pd.concat([df_existing, df], ignore_index=True)

    # حفظ البيانات إلى ملف Excel محلي
    try:
        df_combined.to_excel("C:/Users/Hind/Desktop/IT Program Tracking Sheet.xlsx", index=False)  # تأكد من تعديل المسار
        print("Data saved successfully.")
    except Exception as e:
        print("Error saving data:", e)

# تأكد من أن Session State يحتوي على مفتاح الصفحة
if "page" not in st.session_state:
    st.session_state.page = "Data Entry"

# متغير لتتبع حالة الإرسال
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# عنوان التطبيق
st.title("IT Program Tracking")

# أزرار التنقل لتحديد الصفحة
if st.sidebar.button("Data Entry"):
    st.session_state.page = "Data Entry"
    st.session_state.submitted = False  # إعادة تعيين حالة الإرسال عند العودة إلى الصفحة

if st.sidebar.button("Dashboard"):
    st.session_state.page = "Dashboard"

# صفحة إدخال البيانات
if st.session_state.page == "Data Entry":
    st.header("Program Data Entry Form")

    # إذا كانت البيانات قد تم تقديمها بالفعل، اعرض رسالة
    if st.session_state.submitted:
        st.success("Data has already been submitted.")
    else:
        # تجميع البيانات من المستخدم لكل عمود مع عدم إظهار القيم السابقة
        program_name = st.text_input("Program Name", value="", key="program_name")
        responsible_dept = st.text_input("Responsible Department", value="", key="responsible_dept")
        
        # قائمة الكليات في جامعة الملك عبدالعزيز
        colleges = [
            "College of Arts",
            "College of Science",
            "College of Engineering",
            "College of Medicine",
            "College of Pharmacy",
            "College of Business",
            "College of Computer Science",
            "College of Law",
            "College of Environmental Design",
            "College of Humanities",
            "College of Dentistry",
            "College of Health Sciences"
        ]
        
        beneficiary_group = st.multiselect("Beneficiary Group", ["Students", "Faculty", "Staff"], key="beneficiary_group")
        beneficiary_colleges = st.multiselect("Beneficiary Colleges", colleges, key="beneficiary_colleges")
        program_purpose = st.text_area("Program Purpose", value="", key="program_purpose")
        license_type = st.selectbox("License Type", ["Open-source", "Paid", "In-house Developed"], key="license_type")
        annual_license_cost = st.number_input("Annual License Cost", min_value=0.0, key="annual_license_cost")
        cost_per_user = st.number_input("Cost per User", min_value=0.0, key="cost_per_user")
        initial_usage_date = st.date_input("Initial Usage Date", key="initial_usage_date")
        available_subscriptions = st.number_input("Available Subscriptions", min_value=0, key="available_subscriptions")
        current_user_count = st.number_input("Current User Count", min_value=0, key="current_user_count")
        required_user_count = st.number_input("Required User Count", min_value=0, key="required_user_count")
        monthly_usage_rate = st.number_input("Monthly Usage Rate", min_value=0, key="monthly_usage_rate")
        program_performance = st.slider("Program Performance", 1, 10, key="program_performance")
        monthly_incident_count = st.number_input("Monthly Incident Count", min_value=0, key="monthly_incident_count")
        technical_support_level = st.selectbox("Technical Support Level", ["High", "Medium", "Low"], key="technical_support_level")
        number_of_improvements = st.number_input("Number of Required Improvements", min_value=0, key="number_of_improvements")
        current_program_state = st.selectbox("Current Program State", ["In use", "Outdated", "Needs Replacement"], key="current_program_state")
        future_viability = st.selectbox("Future Viability", ["Expand", "Phase Out"], key="future_viability")
        total_cost_to_date = st.number_input("Total Cost to Date", min_value=0.0, key="total_cost_to_date")

        # زر "Submit" لحفظ البيانات
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
                "Number of Required Improvements": number_of_improvements,
                "Current Program State": current_program_state,
                "Future Viability": future_viability,
                "Total Cost to Date": total_cost_to_date
            }

            # التحقق من عدم وجود بيانات فارغة قبل الحفظ
            if all(data.values()):
                print("Data to be saved:", data)  # عرض البيانات قبل الحفظ
                save_data(data)
                st.session_state.submitted = True  # تعيين حالة الإرسال إلى True
                st.success("Data submitted successfully")
            else:
                st.error("Please fill in all fields before submitting.")

# صفحة Dashboard فارغة
elif st.session_state.page == "Dashboard":
    st.header("Dashboard")
    st.write("This is the Dashboard page. Content will be added later.")
