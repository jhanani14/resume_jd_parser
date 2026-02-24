import streamlit as st
import sqlite3
import hashlib



def connect_db():
    return sqlite3.connect("users.db")



def create_table():
    conn = connect_db()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users(
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()



def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()



def register_user(username, password):
    conn = connect_db()
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users(username, password) VALUES (?, ?)",
                  (username, hash_password(password)))
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        return False



def check_user(username, password):
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?",
              (username, hash_password(password)))
    data = c.fetchone()
    conn.close()
    return data



def login():
    create_table()

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    st.sidebar.title("Authentication")

    if st.session_state.logged_in:
        st.sidebar.success("Logged in")
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()
        return True

    menu = ["Login", "Register"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")

        if st.sidebar.button("Login"):
            if check_user(username, password):
                st.session_state.logged_in = True
                st.sidebar.success("Login Successful")
                st.rerun()
            else:
                st.sidebar.error("Invalid Credentials")

    elif choice == "Register":
        new_user = st.sidebar.text_input("New Username")
        new_pass = st.sidebar.text_input("New Password", type="password")

        if st.sidebar.button("Register"):
            if register_user(new_user, new_pass):
                st.sidebar.success("Account Created! Now Login.")
            else:
                st.sidebar.error("Username already exists")

    return False
