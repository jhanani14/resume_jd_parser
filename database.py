import sqlite3

def create_database():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            password BLOB,
            resume TEXT,
            job_description TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_user_data(email, resume_text, jd_text):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET resume = ?, job_description = ?
        WHERE email = ?
    """, (resume_text, jd_text, email))

    conn.commit()
    conn.close()
