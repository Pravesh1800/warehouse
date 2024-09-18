import os

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import time

st.set_page_config(layout="wide")



logo = r"E:\Barrel Detection\Dashboard\short_logo.png"
sidebar_logo = r"E:\Barrel Detection\Dashboard\logo-removebg-preview.png"


st.logo(sidebar_logo, icon_image=logo)

st.markdown(
    """
    <style>
    img[data-testid="stLogo"] {
        height: 3.5rem;  /* Adjust this value as needed */
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    selected = option_menu('Apta Warehouse',

                           ['Dashboard',
                            'Inventory Info',"","","","","","","","","","","",""],
                           menu_icon='🧑‍💻',
                           icons=['🧔🏽‍♂️', '🧔🏽‍♂️','🧔🏽‍♂️',"🧔🏽‍♂️","🔔","🔔","🔔","🔔","🔔","🔔","🔔","🔔","🔔","🔔"],
                           default_index=0)






if selected == "Dashboard" :
     
    cctv = "store_room1-cctv"
    location = "Dubai"

    st.subheader("Welcome John")
    st.write("This is the dashboard of chemical warehouse")


    vid_col,space,info_col =  st.columns([5.5,0.5,5.5])

    with vid_col:
        city_col,blank,loc_col = st.columns(3)
        with city_col:
            city = st.selectbox("Select the camera.",("store_room1-cctv",'store_room2-cctv','common area-cctv','front door-cctv'))
        with loc_col:
            location = st.selectbox("Select the location.",("Dubai",'Sharjah','Ajman','Abu Dhabi'))
        
        
        video_file = open("E:/Barrel Detection/Dashboard/video.mp4", "rb")
        video_bytes = video_file.read()

        st.video(video_bytes,loop=True,autoplay=True,)

    with info_col:
        st.markdown("""
            <style>
                    
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
            .card {
                background-color: #5689F1;
                border-radius: 15px;
                padding: 20px;
                text-align: left;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
                margin-top: 10px;
            }
            .title {
                font-family: 'Roboto', sans-serif;
                color: #FFFFFF;
                font-size: 18px;
                font-weight: light;
                margin-bottom: 10px;
            }
            .count {
                font-family: 'Roboto', sans-serif;
                color: #FFFFFF;
                font-size: 34px;
                font-weight: thin;
            }
            .card1 {
            background-color: #623DA2;
            }
            .card2 {
                background-color: #4C6CF9;
            }
            .card3 {
                background-color: #3D50A2;
            }
            .card_haz_1 {
                background-color: #B0A1FB;
            }
            .card_haz_2 {
                background-color: #FBA1AD;
            }
                </style>
                """, unsafe_allow_html=True)

        # Wrapping everything inside a container div for a cohesive look
        st.markdown('<div class="container">', unsafe_allow_html=True)

        # Subheader with its own style
        inv_head,inv_spave,inv_date = st.columns([2,1,1])
        with inv_date:
            invdate = st.date_input("Select date")
        with inv_head:
            st.write("")
            st.write("")
            st.markdown('<p class="big-font"><b>Inventory Records</b></p>', unsafe_allow_html=True)
        

        # Use columns for layout
        total, inside, outside = st.columns(3)

        # Total chemicals with styling
        with total:
            st.markdown('''
                <div class="card card1">
                    <div class="title">Total Chemicals</div>
                    <div class="count">28</div>
                </div>
                ''', unsafe_allow_html=True)

        # Inside Chemicals card with different background color
        with inside:
            st.markdown('''
                <div class="card card2">
                    <div class="title">Hazardous</div>
                    <div class="count">12</div>
                </div>
                ''', unsafe_allow_html=True)

        # Outside Chemicals card with different background color
        with outside:
            st.markdown('''
                <div class="card card3">
                    <div class="title">Non-Hazardous</div>
                    <div class="count">16</div>
                </div>
                ''', unsafe_allow_html=True)

        # Closing Main Container
        st.markdown('</div>', unsafe_allow_html=True)

        
        st.write("")
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<p class="big-font"><b>Hazardous Chemicals Transports</b></p>', unsafe_allow_html=True)
       

        haz_in,haz_out = st.columns(2)
        with haz_in:
            st.markdown('''
                <div class="card card_haz_1">
                    <div class="title">Hazardous Chemicals In</div>
                    <div class="count">05</div>
                </div>
                ''', unsafe_allow_html=True)
        with haz_out:
            st.markdown('''
                <div class="card card_haz_2">
                    <div class="title">Hazardous Chemicals Out</div>
                    <div class="count">07</div>
                </div>
                ''', unsafe_allow_html=True)
            



    # Sample DataFrame with element names, info, and danger level
    data = {
        "Element Name": ["BoxA", "BoxB", "BoxC", "Barrel"],
        "Info": [
            "Contains Pestcide used to prevent, destroy, or control pests commonly used in agriculture",
            "Contains Asbestos used in construction materials for insulation, severe health risk if inhailed for long time",
            "Contains Ammonia, used in cleaning products and fertilizers. Exposure to high concentrations can cause severe irritation to the eyes, lungs, and skin",
            "Contains Benzene used in industrial chemical, it is a known carcinogen ",
        ],
        "Danger Level": [3, 5, 3, 5],  # Danger level from 1 to 5
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # List of elements to display
    elements_to_display = ["BoxA", "BoxB", "BoxC", "Barrel"]

    # Filter DataFrame for only the elements in the list
    filtered_df = df[df["Element Name"].isin(elements_to_display)]

    # Function to generate star ratings
    def generate_stars(danger_level):
        return "★" * danger_level + "☆" * (5 - danger_level)

    # Custom CSS for Flexbox
    st.markdown("""
        <style>
            .flex-container {
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 10px;
                background-color: white;
                margin-bottom: 10px;  
                border-radius: 8px;
            }
            .element-name {
                font-size: 18px; 
                font-weight: bold; 
                flex: 1 1 20%; 
                min-width: 150px;
            }
            .element-info {
                font-size: 14px; 
                color: #555; 
                flex: 1 1 60%; 
                text-align: left;
                padding-left: 15px;
            }
            .danger-level {
                font-size: 16px; 
                color: #e74c3c;
                flex: 1 1 20%; 
                text-align: right;
            }
        </style>
    """, unsafe_allow_html=True)

    # Streamlit app title
    st.subheader("Hazardous Chemicals Detected")

    # Loop through the filtered DataFrame and display each element on a single line using Flexbox
    for index, row in filtered_df.iterrows():
        element_name = row["Element Name"]
        element_info = row["Info"]
        danger_level = row["Danger Level"]
        if danger_level > 3:
            st.toast("Highly hazardous chemical detected",icon="☣")
            time.sleep(1)
        
        # Render each element's details inside a flexbox container
        st.markdown(f"""
            <div class="flex-container">
                <div class="element-name">{element_name}</div>
                <div class="element-info">{element_info}</div>
                <div class="danger-level">Danger Level: {generate_stars(danger_level)}</div>
            </div>
        """, unsafe_allow_html=True)


if selected == "Inventory Info":
    store = "store1"
    location = "Dubai"

    st.subheader("Inventory Details")
    st.write("This page contains all the inventory details for all the stores")


    store,blank,location = st.columns([1,2,1])
    with location:
        location = st.selectbox("Select the location.",("Dubai",'Abu Dhabi','Sharjah','Ajman'))
        if location == "Dubai":
            stores = ("store1","store2")
        elif location == "Abu Dhabi":
            stores = ("storeA","storeB")
        else:
            stores = ("storeX","storeY","storeZ")
    with store:
        store_name = st.selectbox("Select the store",stores)


    if location == "Dubai":
        if store_name == "store1":
            data = pd.read_excel("store1_dubai_warehouse.xlsx")
            st.dataframe(data=data,use_container_width=True,height=600)
        elif store_name == "store2":
            data = pd.read_excel("store2_dubai_warehouse.xlsx")
            st.dataframe(data=data,use_container_width=True,height=600)
    elif location == "Abu Dhabi":
        if store_name == "storeA":
            data = pd.read_excel("storeA_abu_dhabi_warehouse.xlsx")
            st.dataframe(data=data,use_container_width=True,height=600)
        elif store_name == "storeB":
            data = pd.read_excel("storeB_abu_dhabi_warehouse.xlsx")
            st.dataframe(data=data,use_container_width=True,height=600)
    else:
        data = pd.read_excel("storeA_abu_dhabi_warehouse.xlsx")
        st.dataframe(data=data,use_container_width=True,height=600)
















































