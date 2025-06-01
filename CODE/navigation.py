import streamlit as st

import base64
import numpy as np
import matplotlib.pyplot as plt 
from tkinter.filedialog import askopenfilename

import streamlit as st

import matplotlib.image as mpimg

import streamlit as st
import base64

import pandas as pd
import sqlite3

# ================ Background image ===

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('1.jpg')


def navigation():
    try:
        path = st.experimental_get_query_params()['p'][0]
    except Exception as e:
        st.error('Please use the main app.')
        return None
    return path


if navigation() == "home":
    st.markdown(f'<h1 style="color:#000000 ;text-align: center;font-size:26px;font-family:verdana;">{"Improve the quality of digital health care services using big data analytics"}</h1>', unsafe_allow_html=True)

    # st.markdown(f'<h1 style="color:#ffffff;text-align: center;font-size:36px;">{"Ethical issues of Generative AI"}</h1>', unsafe_allow_html=True)
    
    print()
    print()

    print()

    st.text("                 ")
    st.text("                 ")
    a = "Machine learning approach that enables health condition prediction while prioritizing patient privacy. By training models across decentralized data sources—such as hospitals and clinics—without sharing sensitive health information, federated learning enhances collaboration among institutions. This method allows for the development of more accurate predictive models by leveraging diverse datasets while ensuring compliance with data protection regulations. Ultimately, it fosters improved health outcomes through tailored interventions based on aggregated insights from multiple sources."

    
    st.markdown(f'<h1 style="color:#000000;text-align: justify;font-size:20px;font-family:Caveat, sans-serif;">{a}</h1>', unsafe_allow_html=True)

    st.text("                 ")
    st.text("                 ")
    
    st.text("                 ")
    st.text("                 ")
    
    # col1,col2,col3 = st.columns(3)
    
    # with col1:
        
    #     st.image("b1.jpg")

    # with col2:
        
    #     st.image("b2.jpg")

    # with col3:
        
    #     st.image("b3.jpg")



elif navigation()=='reg':
   
    st.markdown(f'<h1 style="color:#000000 ;text-align: center;font-size:26px;font-family:verdana;">{"Improve the quality of digital health care services using big data analytics"}</h1>', unsafe_allow_html=True)

    st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:20px;">{"Register Here !!!"}</h1>', unsafe_allow_html=True)
    
    import streamlit as st
    import sqlite3
    import re
    
    # Function to create a database connection
    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except sqlite3.Error as e:
            print(e)
        return conn
    
    # Function to create a new user
    def create_user(conn, user):
        sql = ''' INSERT INTO users(name, password, email, phone)
                  VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, user)
        conn.commit()
        return cur.lastrowid
    
    # Function to check if a user already exists
    def user_exists(conn, email):
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email=?", (email,))
        if cur.fetchone():
            return True
        return False
    
    # Function to validate email
    def validate_email(email):
        pattern = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        return re.match(pattern, email)
    
    # Function to validate phone number
    def validate_phone(phone):
        pattern = r'^[6-9]\d{9}$'
        return re.match(pattern, phone)
    
    # Main function
    def main():
        # st.title("User Registration")
    
        # Create a database connection
        conn = create_connection("dbs.db")
    
        if conn is not None:
            # Create users table if it doesn't exist
            conn.execute('''CREATE TABLE IF NOT EXISTS users
                         (id INTEGER PRIMARY KEY,
                         name TEXT NOT NULL,
                         password TEXT NOT NULL,
                         email TEXT NOT NULL UNIQUE,
                         phone TEXT NOT NULL);''')
    
            # User input fields
            name = st.text_input("Enter your name")
            password = st.text_input("Enter your password", type="password")
            confirm_password = st.text_input("Confirm your password", type="password")
            email = st.text_input("Enter your email")
            phone = st.text_input("Enter your phone number")
    
            col1, col2 = st.columns(2)

            with col1:
                    
                aa = st.button("REGISTER")
                
                if aa:
                    
                    if password == confirm_password:
                        if not user_exists(conn, email):
                            if validate_email(email) and validate_phone(phone):
                                user = (name, password, email, phone)
                                create_user(conn, user)
                                st.success("User registered successfully!")
                            else:
                                st.error("Invalid email or phone number!")
                        else:
                            st.error("User with this email already exists!")
                    else:
                        st.error("Passwords do not match!")
                    
                    conn.close()
                    # st.success('Successfully Registered !!!')
                # else:
                    
                    # st.write('Registeration Failed !!!')     
            
            with col2:
                    
                aa = st.button("LOGIN")
                
                if aa:
                    import subprocess
                    subprocess.run(['python','-m','streamlit','run','login.py'])
                    # st.success('Successfully Registered !!!')
    
    
    
  
    if __name__ == '__main__':
        main()



elif navigation()=='Login':
    
    st.markdown(f'<h1 style="color:#000000 ;text-align: center;font-size:26px;font-family:verdana;">{"Improve the quality of digital health care services using big data analytics"}</h1>', unsafe_allow_html=True)


    # Function to create a database connection
    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except sqlite3.Error as e:
            print(e)
        return conn
    
    # Function to create a new user
    def create_user(conn, user):
        sql = ''' INSERT INTO users(name, password, email, phone)
                  VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, user)
        conn.commit()
        return cur.lastrowid
    
    # Function to validate user credentials
    def validate_user(conn, name, password):
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE name=? AND password=?", (name, password))
        user = cur.fetchone()
        if user:
            return True, user[1]  # Return True and user name
        return False, None
    
    # Main function
    def main():
        # st.title("User Login")
        st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:24px;">{"Login here"}</h1>', unsafe_allow_html=True)
    
    
        # Create a database connection
        conn = create_connection("dbs.db")
    
        if conn is not None:
            # Create users table if it doesn't exist
            conn.execute('''CREATE TABLE IF NOT EXISTS users
                         (id INTEGER PRIMARY KEY,
                         name TEXT NOT NULL,
                         password TEXT NOT NULL,
                         email TEXT NOT NULL UNIQUE,
                         phone TEXT NOT NULL);''')
    
            st.write("Enter your credentials to login:")
            name = st.text_input("User name")
            password = st.text_input("Password", type="password")
    
            col1, col2 = st.columns(2)
    
            with col1:
                    
                aa = st.button("Login")
                
                if aa:
    
    
            # # if st.button("Login"):
                    is_valid, user_name = validate_user(conn, name, password)
                    if is_valid:
                        st.success(f"Welcome back, {user_name}! Login successful!")
                        
                        import subprocess
                        subprocess.run(['python','-m','streamlit','run','app.py'])
                        
                        
                        
                        
                        
                    else:
                        st.error("Invalid user name or password!")
                        
           
                      # st.success('Successfully Registered !!!')          
                        
                        
            # if st.button("Change Password"):
            #     import subprocess
            #     subprocess.run(['streamlit','run','CP.py'])
    
    
            # Close the database connection
            conn.close()
        else:
            st.error("Error! cannot create the database connection.")
    
    if __name__ == '__main__':
        main()


elif navigation()=='chat':
    
    import streamlit as st
    import google.generativeai as genai

    # --- Config API ---
    genai.configure(api_key="AIzaSyClwCo8aIpV8gieeDQ5HsjiASODhGkxt-0")  # Replace with your actual API key

    # --- Generation configuration ---
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    # --- Initialize the model ---
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction=(
            "Want to create a Medical chatbot. User can ask questions related to their disease "
            "like suggest medicines, precautions and so on. If I speak in Tulu, the reply must be in Tulu."
        ),
    )

    # --- Set up Streamlit ---
    # st.set_page_config(page_title="💊 Medical Chatbot", layout="wide")
    st.title("💊 Medical Chatbot")
    st.markdown("Ask any health-related questions. If you speak in Tulu, the bot will reply in Tulu.")

    # --- Session state for chat history ---
    if "chat" not in st.session_state:
        st.session_state.chat = model.start_chat(history=[
            {
                "role": "user",
                "parts": ["Hi, I have a cold, give suggestions."]
            },
            {
                "role": "model",
                "parts": ["""I am an AI and cannot give medical advice. A cold is usually caused by a virus and will typically clear up on its own within 7–10 days. However, to alleviate symptoms, try the following:

    - 💧 **Hydration:** Drink fluids like water or tea  
    - 😴 **Rest:** Help your body recover  
    - 💊 **OTC Meds:** Try paracetamol or ibuprofen for fever  
    - 🌬️ **Humidifier:** Helps with nasal congestion  
    - 🧂 **Salt gargle:** For sore throat  
    - 🚫 **Avoid irritants:** Like smoke and dust

    > ⚠️ **Consult a doctor if symptoms persist or worsen.**
    """]
            }
        ])
        st.session_state.messages = []

    # --- Chat form ---
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("You", placeholder="Describe your symptoms or ask a health question...", label_visibility="collapsed")
        submitted = st.form_submit_button("Send")

    # --- Handle input and display ---
    if submitted and user_input:
        st.session_state.messages.append(("user", user_input))
        response = st.session_state.chat.send_message(user_input)
        st.session_state.messages.append(("bot", response.text))

    # --- Display chat messages ---
    # for role, msg in st.session_state.messages:
    #     col1, col2 = st.columns([1, 1]) if role == "user" else st.columns([1, 1])
    #     with col1 if role == "user" else col2:
    #         if role == "user":
    #             st.markdown(f"🧑‍💬 **You:**\n\n{msg}", unsafe_allow_html=True)
    #         else:
    #             st.markdown(f"🤖 **Bot:**\n\n{msg}", unsafe_allow_html=True)

    # --- Display chat messages with styles ---
    for role, msg in st.session_state.messages:
        if role == "user":
            st.markdown(
                f"""
                <div style='
                    background-color: #DCF8C6;
                    border-radius: 10px;
                    padding: 10px 15px;
                    margin: 5px 50px 5px 5px;
                    text-align: left;
                    color: black;
                    font-family: Arial;
                    '>
                    🧑‍💬 <strong>You:</strong><br>{msg}
                </div>
                """, unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style='
                    background-color: #E6E6FA;
                    border-radius: 10px;
                    padding: 10px 15px;
                    margin: 5px 5px 5px 50px;
                    text-align: left;
                    color: black;
                    font-family: Arial;
                    '>
                    🤖 <strong>Bot:</strong><br>{msg}
                </div>
                """, unsafe_allow_html=True
            )

