import streamlit as st
import streamlit.components.v1 as components

# Page settings
st.set_page_config(
    page_title="OLA Ride Analytics",
    page_icon="🚖",
    layout="wide"
)

# Custom CSS styling
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
h1, h2, h3 {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🚖 OLA Ride Analytics")

page = st.sidebar.radio(
    "Navigation",
    ["Project Overview", "Dashboard"]
)

# -----------------------------
# Project Overview Page
# -----------------------------
if page == "Project Overview":

    st.title("🚖 OLA Ride Data Analysis Project")

    st.markdown("""
This project analyzes **OLA ride data** to uncover insights about:

- Ride volume trends  
- Booking success and cancellation rates  
- Revenue by payment method  
- Customer and driver ratings  
- Vehicle performance  

The project demonstrates a **complete data analytics workflow**.
""")

    st.markdown("## 🛠 Tools Used")

    col1, col2, col3, col4 = st.columns(4)

    col1.info("Python")
    col2.info("SQL")
    col3.info("Tableau")
    col4.info("Streamlit")

    st.markdown("## 📊 Project Workflow")

    st.markdown("""
1️⃣ Data Cleaning (Python / Excel)  
2️⃣ SQL Data Analysis  
3️⃣ Tableau Dashboard Creation  
4️⃣ Streamlit App Development  
5️⃣ Cloud Deployment
""")

# -----------------------------
# Dashboard Page
# -----------------------------
elif page == "Dashboard":

    st.title("📊 OLA Ride Data Analysis Dashboard")

    st.markdown("Interactive business intelligence dashboard built using **Tableau Public**.")

    # KPI metrics
    st.markdown("### Key Metrics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Rides", "103,024")
    col2.metric("Total Revenue", "₹3.38M")
    col3.metric("Avg Customer Rating", "4.2 ⭐")
    col4.metric("Success Rate", "63%")

    st.markdown("---")

    st.subheader("📈 Interactive Tableau Dashboard")

    components.html("""
    <div class='tableauPlaceholder' style='width:100%;height:900px;'>
    <object class='tableauViz' width='100%' height='900'>
    <param name='host_url' value='https://public.tableau.com/' />
    <param name='embed_code_version' value='3' />
    <param name='name' value='Book1_17733640226230/Dashboard1' />
    <param name='tabs' value='no' />
    <param name='toolbar' value='yes' />
    </object>
    </div>
    <script src='https://public.tableau.com/javascripts/api/viz_v1.js'></script>
    """, height=900)

# Footer
st.markdown("---")
st.markdown("Created by **Saeesh Vele | Data Analytics Project**")