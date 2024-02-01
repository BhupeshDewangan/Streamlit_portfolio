import streamlit as st
import requests

from streamlit_option_menu import option_menu

from about import about_me_section
from skills import skills_section
from certificate import certificates
from da_projects import da_projects_section
from ml_projects import ml_projects_section





def sidebar():
    with st.sidebar:
        selected = option_menu("Main Menu", ["Home", 'Skills', 'Data Analysis Projects', 'ML and DS Projects', 'Certificates'], 
            icons=['house-check', 'braces-asterisk', 'clipboard2-data-fill', 'gear', 'patch-check-fill'], menu_icon="list", default_index=0)
        
    if selected == "Home":
        about_me_section()

    elif selected == "Skills":
        skills_section()

    elif selected == "Data Analysis Projects":
        da_projects_section()

    elif selected == "ML and DS Projects":
        ml_projects_section()

    elif selected == "Certificates":
        certificates()
    
    # ---------------------------------------------


    # RESUME -----------------------------------------------------
    website_url = "https://docs.google.com/document/d/1OFtW2NZ7BC39LUXwy6xrxJWKbhiMvV2tEnQ7AdKAoXA/edit"

    st.sidebar.markdown(f'''
        <a href={website_url}>
        <button style="background-color:#4181e4; 
        cursor: pointer; 
        border-radius: 8px;
        border: 1px solid black;
        padding: 10px 20px;
        text-decoration: none;
        display: inline-block;
        ">
        Download Button 🔗
        </button>
        </a>
        ''',
        unsafe_allow_html=True)




def main():
    # Set page title and icon
    st.set_page_config(
        page_title=" 👋🏻 My Personal Portfolio ✨",
        page_icon="✨",
        layout="wide"
    )

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    sidebar()


if __name__ == "__main__":
    main()
