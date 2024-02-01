import streamlit as st
import requests

def about_me_section():
    
    st.title("About Me")

    # Create two columns
    col1, col2 = st.columns([3, 2])    

    # Column 1: Name and Description
    col1.header("Bhupesh Kumar Dewangan")
    col1.success("**Ethusias Data Analyst | Proficient in Power BI, Intermediate SQL, Advanced Excel, Advanced Python|**")
    col1.write("I am an enthusiastic professional entering the tech industry with a keen focus on transforming raw data into actionable insights. Equipped with a robust skill set and a commitment to continuous learning, I am ready to contribute to meaningful projects in data analysis and data science.")


    # Column 2: Image
    col2.image("./Assets/bhupesh_profile.jpg")

    col1.write("***Mobile No 📱 - 8319341550***")
    col1.write("***Email ✉️ - bhupesh.dew.careers@gmail.com***")

    st.write("---")

    website_url1 = "https://github.com/BhupeshDewangan"
    website_url2 = "https://www.linkedin.com/in/bhupesh-dewangan-7121851ba/"
    website_url3 = "https://github.com/BhupeshDewangan"
    website_url4 = "https://leetcode.com/Bhupesh_Dewangan/"
    website_url5 = "https://www.codingninjas.com/codestudio/profile/ca83b5ed-a8f6-4338-8f9f-bfbab2b40d74"

    s1, s2, s3, s4,s5 = st.columns([2,2,2,2,2])

    s1.markdown(f'''
    <a href={website_url1}><button style="background-color:#607d8b; border: none;
	font-family: 'Lato';
	font-size: 20px;
	color: inherit;
	background: none;
	cursor: pointer; ">Github 🔗</button></a>
    ''',
    unsafe_allow_html=True)

    s2.markdown(f'''
    <a href={website_url2}><button style="background-color:#607d8b; border: none;
	font-family: 'Lato';
	font-size: 20px;
	color: inherit;
	background: none;
	cursor: pointer; ">Linkedin 🔗</button></a>
    ''',
    unsafe_allow_html=True)

    s3.markdown(f'''
    <a href={website_url1}><button style="background-color:#607d8b; border: none;
	font-family: 'Lato';
	font-size: 20px;
	color: inherit;
	background: none;
	cursor: pointer;">GFG 🔗</button></a>
    ''',
    unsafe_allow_html=True)

    s4.markdown(f'''
    <a href={website_url1}><button style="background-color:#607d8b;border: none;
	font-family: 'Lato';
	font-size: 20px;
	color: inherit;
	background: none;
	cursor: pointer;">Leetcode 🔗</button></a>
    ''',
    unsafe_allow_html=True)

    s5.markdown(f'''
    <a href={website_url1}><button style="background-color:#607d8b;border: none;
	font-family: 'Lato';
	font-size: 20px;
	color: inherit;
	background: none;
	cursor: pointer;">Code Studio🔗</button></a>
    ''',
    unsafe_allow_html=True)
