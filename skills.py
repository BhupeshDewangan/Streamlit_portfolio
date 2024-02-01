import streamlit as st
import requests

def skills_section():
    st.title("Skills")

    col1, col2 = st.columns(2)
    # Display a list of skills
    with col1:
        st.subheader("Data Analysis 👩‍💻:")
        st.write("- Exploratory Data Analysis (EDA) 📊")
        st.write("- Data Cleaning and Preprocessing 🧹")
        st.write("- Advanced Excel (Lookups, Pivot Tables, Graphs, and Charts) 📈")

        st.subheader("Programming 💻:")
        st.write("- Python (Pandas, NumPy, Streamlit, Scikit-learn) 🐍")
        st.write("- HTML, CSS, JavaScript, C++ 🗃️")

        st.subheader("Data Visualization 📊:")
        st.write("- Matplotlib, Seaborn 📈")
        st.write("- PowerBI 📊")

    with col2:
        st.subheader("Machine Learning 🤖:")
        st.write("- Supervised Learning (Regression, Classification) 🧠")
        st.write("- Unsupervised Learning (Clustering) 🤔")
        st.write("- Feature Engineering 🛠️")

        st.subheader("Database Management 🗄️:")
        st.write("- SQL (Postgres, MySQL) 🗃️")
        st.write("- PgAdmin, SQL Workbench 🔍")

        st.subheader("Tools 🛠️:")
        st.write("- Jupyter Notebooks 📓")
        st.write("- Google Colab 🧪")
        st.write("- Git and Version Control 🐙")