import streamlit as st
import requests

def ml_projects_section():
    st.title("Machine Learning and Data Science Projects")

    st.write("---")

    col1, col2 = st.columns([2,2])
    col1.write("**Project 1: Software Salary Prediction Webpage**")
    col1.write("- Build a Regression based machine learning project, which allow user to predicts the salary of software developers according to country , education and experience.")
    col1.write("- Implemented a 2 page Web Interface, Predict and Explore.")
    col2.image('./ML_Projects/1S.png')
    # col2.video('./ML_Projects/Soft_Salary_Pred.mp4')
    col2.write('- **Tech Used - Python, Streamlit, Google Colab**')
    
    st.write("---")
    
    col3, col4 = st.columns([2,2])
    col4.write("**Project 2: Movie Recommendation App**")
    col4.write("- Build a Recommendation app leveraging basic of Machine Learning and Data Analysis. Used Scikit-Learn to find similarities between movies and Streamlit library to foster seamless connections between ML Model and Webpage.")
    col4.write("- Implemented Recommend function for Movies and Director based, 2 page navigation and A responsive user friendly UI.")
    col3.image('./ML_Projects/movie.png')
    col3.write('- **Tech Used - Python, Streamlit, Jupyter Notebook, Scikit-learn.**')
    
    st.write("---")

    col5, col6 = st.columns([2,2])
    col5.write("**Project 3: Laptop Price Prediction Webpage**")
    col5.write("- Build a single page Regression based Machine Learning Project, allow user to Predict the prices of laptop by their specifications. Specs include Company, RAM, Storage, Display Size, Processor etc.")
    col5.write("- Excelled in data processing and visualization, creating impactful charts and graphs. , such as peak sales months, dominant customer demographics, and top-selling channels, informing strategic business decisions for Vrinda Store.")
    col6.image('./ML_Projects/laptop.png')
    col6.write('- **Tech Used - Python, Streamlit, Google Colab.**')
    
    st.write("---")

    # col7, col8 = st.columns([2,2])
    # col8.write("**Project 2: Walmart Sales Analysis**")
    # col8.write("- Executed comprehensive Walmart Sales Analysis project using PostgreSQL, demonstrating expertise in data wrangling, feature engineering, and insightful exploratory data analysis for strategic decision-making.")
    # col8.write("- Unveiled key insights into branch-wise sales trends, employing robust data wrangling and feature engineering techniques. Translated findings into actionable strategies for enhanced sales performance at Walmart.")
    # col7.image('./DA_Projects/p1.png')
    # col7.write('- **Tools Used - PostgreSQL, MS Excel**')