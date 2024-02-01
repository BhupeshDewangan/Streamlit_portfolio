import streamlit as st
import requests

def da_projects_section():
    st.title(" Data Analysis Projects")

    sbox = st.selectbox("Choose", ("ALL","MS Excel", "Power BI"))

    if sbox == 'ALL':
        col1, col2 = st.columns([2,2])
        col1.write("**Project 1: HR Analysis Dashboard**")
        col1.write("- Developed a comprehensive HR analysis dashboard, offering valuable insights into employee demographics, performance metrics, attrition rates, and training effectiveness.")
        col1.write("- Enhancing HR decision-making by visualizing key HR data in an interactive and user-friendly manner.")
        col2.image('./DA_Projects/HR.png')
        col2.write('- **Tools Used - Power BI, MS Excel**')
        
        st.write("---")
        
        col3, col4 = st.columns([2,2])
        col4.write("**Project 2: Coffee Sales Dashboard**")
        col4.write("- Designed and implemented a dynamic coffee sales dashboard, showcasing expertise in line and bar charts, VLOOKUP, and INDEX MATCH for dynamic data fetching.")
        col4.write("- Excelled in pivot tables, slicers, and timelines, creating visually stunning coffee sales dashboards. Prioritized accessibility with scroll bars for optimal user experience.")
        col3.image('./DA_Projects/Coffee.jpeg')
        col3.write('- **Tools Used - MS Excel, Dashboard, Pivot Table, Lookups**')
        
        st.write("---")

        col5, col6 = st.columns([2,2])
        col5.write("**Project 3: Vrinda Store Analysis**")
        col5.write("- Led a comprehensive Excel project, extracting, cleaning, and analyzing data to unveil key insights. Identified growth opportunities by targeting women customers (30-49 yrs) in top-performing states on major e-commerce platforms")
        col5.write("- Excelled in data processing and visualization, creating impactful charts and graphs. , such as peak sales months, dominant customer demographics, and top-selling channels, informing strategic business decisions for Vrinda Store.")
        col6.image('./DA_Projects/vrinda.jpeg')
        col6.write('- **Tools Used - MS Excel, Dashboard, Pivot Table**')
        
        st.write("---")

        col7, col8 = st.columns([2,2])
        col8.write("**Project 4: Walmart Sales Analysis**")
        col8.write("- Executed comprehensive Walmart Sales Analysis project using PostgreSQL, demonstrating expertise in data wrangling, feature engineering, and insightful exploratory data analysis for strategic decision-making.")
        col8.write("- Unveiled key insights into branch-wise sales trends, employing robust data wrangling and feature engineering techniques. Translated findings into actionable strategies for enhanced sales performance at Walmart.")
        col7.image('./DA_Projects/walmart.jpg')
        col7.write('- **Tools Used - PostgreSQL, MS Excel**')
        



    if sbox == 'MS Excel':
        col3, col4 = st.columns([2,2])
        col4.write("**Project 1: Coffee Sales Dashboard**")
        col4.write("- Designed and implemented a dynamic coffee sales dashboard, showcasing expertise in line and bar charts, VLOOKUP, and INDEX MATCH for dynamic data fetching.")
        col4.write("- Excelled in pivot tables, slicers, and timelines, creating visually stunning coffee sales dashboards. Prioritized accessibility with scroll bars for optimal user experience.")
        col3.image('./DA_Projects/Coffee.jpeg')
        col3.write('- **Tools Used - MS Excel, Dashboard, Pivot Table, Lookups**')

        st.write("----")

        col5, col6 = st.columns([2,2])
        col5.write("**Project 2: Vrinda Store Analysis**")
        col5.write("- Led a comprehensive Excel project, extracting, cleaning, and analyzing data to unveil key insights. Identified growth opportunities by targeting women customers (30-49 yrs) in top-performing states on major e-commerce platforms")
        col5.write("- Excelled in data processing and visualization, creating impactful charts and graphs. , such as peak sales months, dominant customer demographics, and top-selling channels, informing strategic business decisions for Vrinda Store.")
        col6.image('./DA_Projects/vrinda.jpeg')
        col6.write('- **Tools Used - MS Excel, Dashboard, Pivot Table**')


    if sbox == 'Power BI':

        col1, col2 = st.columns([2,2])
        col1.write("**Project 1: HR Analysis Dashboard**")
        col1.write("- Developed a comprehensive HR analysis dashboard, offering valuable insights into employee demographics, performance metrics, attrition rates, and training effectiveness.")
        col1.write("- Enhancing HR decision-making by visualizing key HR data in an interactive and user-friendly manner.")
        col2.image('./DA_Projects/HR.png')
        col2.write('- **Tools Used - Power BI, MS Excel**')
        
        st.write("---")

        col5, col6 = st.columns([2,2])
        col6.write("**Project 2: Vrinda Store Analysis**")
        col6.write("- Led a comprehensive Excel project, extracting, cleaning, and analyzing data to unveil key insights. Identified growth opportunities by targeting women customers (30-49 yrs) in top-performing states on major e-commerce platforms")
        col6.write("- Excelled in data processing and visualization, creating impactful charts and graphs. , such as peak sales months, dominant customer demographics, and top-selling channels, informing strategic business decisions for Vrinda Store.")
        col5.image('./DA_Projects/vrinda.jpeg')
        col5.write('- **Tools Used - MS Excel, Dashboard, Pivot Table**')

    