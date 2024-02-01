import streamlit as st

def certificates():
    st.title("Certificates")
    col1, col2 = st.columns([2,2])
    
    # col1
    col1.write("**Certificate 1**")
    col1.image('./Certificates/accenture.jpg')

    col2.write("**Certificate 3**")
    col2.image('./Certificates/cognizant.jpg')

    col1.write("**Certificate 2**")
    col1.image('./Certificates/excel.png')

    # col2
    col2.write("**Certificate 2**")
    col2.image('./Certificates/tata.jpg')

    col1.write("**Certificate 4**")
    col1.image('./Certificates/TCSiON.jpg')

    # col2.write("Certificate 1")
    # col2.image('./Certificates/cognizant.jpg')
