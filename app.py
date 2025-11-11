import streamlit as st
import numpy as np

# Set page config
st.set_page_config(page_title="Prediction Model 💰🔥", layout="wide")

# --- Sidebar ---
with st.sidebar:
    st.title("Prediction Apps")
    st.markdown("### Navigation")
    st.button("🏠 Home")
    st.button("📈 Relations & Correlations")
    st.button("🧮 Prediction")

    st.markdown("---")
    st.markdown("**Upload Your Dataset 📂**")
    uploaded_file = st.file_uploader("Drag and drop file here", type=['csv'])

# --- Main Title ---
st.markdown("<h1 style='text-align:center; color:#b5179e;'>Prediction Model 💰🔥</h1>", unsafe_allow_html=True)

# --- Tabs ---
tab1, tab2 = st.tabs(["One Value", "From File"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Employee Age", min_value=18, max_value=65, value=25)
    with col2:
        exp = st.number_input("Experience Years", min_value=0, max_value=40, value=4)

    edu = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])

    # Predict button
    if st.button("Predict", use_container_width=True):
        # Simple fake prediction logic (replace with model later)
        base_salary = 40000
        salary = base_salary + (exp * 2500) + (age * 500)
        if edu == "Master's":
            salary += 10000
        elif edu == "PhD":
            salary += 20000
        accuracy = np.random.uniform(90, 95)

        col3, col4 = st.columns(2)
        with col3:
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135706.png", width=80)
            st.metric("Expected Salary", f"${salary:,.0f}")
        with col4:
            st.image("https://cdn-icons-png.flaticon.com/512/992/992700.png", width=80)
            st.metric("Model Accuracy", f"{accuracy:.2f}%")

with tab2:
    st.info("📂 Upload a CSV file to predict multiple values (feature not implemented in this demo).")

