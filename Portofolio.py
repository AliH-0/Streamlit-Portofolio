import streamlit as st
import plotly.express as px
import pandas as pd

# Setting custom page config for better aesthetics
st.set_page_config(page_title="Ali Husseini Portfolio", layout="centered", page_icon="💼")

# Style updates for consistent aesthetics
st.markdown(
    """
    <style>
        .main-title {font-size: 36px; font-weight: bold; color: #004080;}
        .header {color: #004080;}
        .contact-info {font-size: 18px; color: white;}
        .section-divider {border-top: 2px solid #E5E5E5; margin-top: 20px; margin-bottom: 20px;}
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Contact Information
st.markdown("<p class='main-title'>Ali Husseini</p>", unsafe_allow_html=True)
st.subheader('Computer Scientist | Data Analyst')

st.markdown("<p class='contact-info'>Email: ali.h.husseini0@gmail.com</p>", unsafe_allow_html=True)
st.markdown("<p class='contact-info'>Phone: +961 70 280082</p>", unsafe_allow_html=True)

# Divider
st.write("<div class='section-divider'></div>", unsafe_allow_html=True)

# Education Section
st.subheader("Education")
st.write("* **B.S. in Computer Science** - Lebanese University (2020 - 2021)")
st.write("* **B.S. in Computer Science** - Lebanese International University (2021 - 2024)")

st.write("<div class='section-divider'></div>", unsafe_allow_html=True)

# Experience Section
st.subheader("Experience")
st.write("* **Developed E-Commerce websites for clients.**  (Dec 2023 – March 2024)")

st.write("<div class='section-divider'></div>", unsafe_allow_html=True)

# Projects Section
st.subheader("Projects")
proj = [
    'Streamlit + Plotly: Superstore Data Analysis and Visualization Dashboard', 
    'Tableau: Interactive and Dynamic Dashboard for British Airway Reviews',
    'Reinforcement Learning Using Deep Q-Learning', 
    'Airbnb Listings Analysis Using Tableau',
    'E-Commerce Website for Supermarket Management'
]
opt = st.selectbox('Select a Project:', options=proj)

def project_lister(proj):
    projects_info = {
        'Streamlit + Plotly: Superstore Data Analysis and Visualization Dashboard': 
            "Developed an interactive dashboard using Streamlit for exploring and analyzing the Superstore dataset. "
            "Users can visualize key metrics like sales and profits through various dynamic charts. "
            "[View Project](https://superstore-data-analysis-and-visualization-dashboard.streamlit.app)",
        
        'Tableau: Interactive and Dynamic Dashboard for British Airway Reviews':
            "Implemented a Dashboard for British Airways reviews that has a sidebar with multiple filtering options for "
            "different metrics, date, traveler type, etc. Includes an interactive map showcasing overall ratings by country. "
            "A custom parameter was added to display currently selected metrics based on filters. "
            "[View Project](https://public.tableau.com/app/profile/ali.el.husseini/viz/BritishAirways_17309565539610/Dashboard1?publish=yes)",
        
        'Reinforcement Learning Using Deep Q-Learning': 
            "Created a deep Q-learning model to simulate spacecraft landing, demonstrating advanced reinforcement learning techniques with optimized control algorithms.",
            
        'Airbnb Listings Analysis Using Tableau':
            "Developed a comprehensive Tableau dashboard analyzing the Airbnb Listings 2016 Dataset. The project includes key metrics such as average price per bedroom, distinct count of bedroom listings, and price analysis by zipcode.",
        
        'E-Commerce Website for Supermarket Management': 
            "Developed a full-stack e-commerce website for a supermarket using ASP.NET and React, featuring user registration, product browsing, shopping cart functionality, and admin management for users and orders.",
    }
    return projects_info.get(proj, "Project description not available.")

st.write(f"**Project Title:** {opt}")
st.write(f"**Description:** {project_lister(opt)}")

if opt == 'Airbnb Listings Analysis Using Tableau':
    st.image("airbnb.jpg", caption="Airbnb Listings Analysis Dashboard", use_column_width=True)
    
if opt == 'Tableau: Interactive and Dynamic Dashboard for British Airway Reviews':
    st.image("british_airway.png", caption="British Airway Reviews Dashboard", use_column_width=True)

st.write("<div class='section-divider'></div>", unsafe_allow_html=True)

# Skills Section with Pie Chart
skills = {'Tableau': 50, 'Plotly': 30, 'Matplotlib': 20}
skills_df = pd.DataFrame.from_dict(skills, orient='index', columns=['Skill Level'])

fig = px.pie(skills_df, names=skills_df.index, values='Skill Level', title='Data Visualization Skills',
             hover_data=['Skill Level'], labels={'Skill Level': 'Skill Level'}, template='plotly_dark')

fig.update_traces(textinfo='label+percent')
st.plotly_chart(fig)

st.subheader("Skills")
st.write("**Programming Languages:** Python, Java, C#, JavaScript")
st.write("**Web Development:** HTML, CSS, JavaScript, ReactJS, ASP.NET, MySQL, MicrosoftSQL")
st.write("**Data Analysis & Visualization:** Python, Tableau, Streamlit, Plotly, Matplotlib, Pandas")
st.write("**Machine Learning:** Python, NumPy, PyTorch")
