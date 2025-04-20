import streamlit as st
import sqlite3
import hashlib

conn =  sqlite3.connect("db/app.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (username text, email text, password text)''')
conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def create_user(username, email, password):
    conn = sqlite3.connect("db/app.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, hash_password(password)))
    conn.commit()
    conn.close()
def check_user(email, password):
    conn = sqlite3.connect("db/app.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, hash_password(password)))
    user = c.fetchone()
    conn.close()
    if user and user[0] == email:
        return True
    return False
def signup():
    st.subheader('Sign Up')
    username = st.text_input("Username", key="signup_username")
    email = st.text_input("Email", key="signup_email")
    password = st.text_input("Password", type='password', key="signup_password")
    if st.button("Sign Up"):
        if username and email and password:
            create_user(username, email, password)
            st.success("Signup successfully!")
        else:
            st.error("Please fill in all fields.")
def login():
    pass
def home():
    st.title("Forcast Net")
    st.write("Welcome to Forcast Net! An AI  platform which is based on predicting the future of various cryptocurencies, stock prices and many more in the trading market based on historical Data.")
    st.header("Features")
    st.write("""
             * Real Time price tracking
             * Price forecasting using machine learning models,
             * Historical price data analysis
             * Customizable alerts and notifications 
             
             """)
    
def main():
    # st.title("Forcast Net")
    # tab1, tab2 =  st.tabs(['Login', 'Sign Up'])
    # with tab1:
    #     login()
    # with tab2:
    #     signup()
    pages = {
        "Home": home,
        "Login": login,
        "Sign Up": signup
    }
    st.sidebar.title("Forcast Net")
    page =  st.sidebar.selectbox("Select a page", list(pages.keys()))
    pages[page]()
if __name__ == "__main__":
    main()
    

    
