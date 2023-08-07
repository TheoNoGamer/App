import PySimpleGUI as sg
import hashlib
import sqlite3
import os

def create_database():
    conn = sqlite3.connect("user_db.sqlite")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            salt TEXT
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password, salt):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000).hex()

def insert_user(username, password):
    salt = os.urandom(16).hex()
    hashed_password = hash_password(password, salt)
    
    conn = sqlite3.connect("user_db.sqlite")
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO users (username, password, salt) VALUES (?, ?, ?)', (username, hashed_password, salt))
    conn.commit()
    conn.close()

def validate_login(username, password):
    conn = sqlite3.connect("user_db.sqlite")
    cursor = conn.cursor()
    
    cursor.execute('SELECT password, salt FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    
    conn.close()

    if result:
        stored_password, salt = result
        hashed_password = hash_password(password, salt)
        return stored_password == hashed_password
    return False

def main():
    create_database()

    layout = [
        [sg.Text('Username:'), sg.InputText(key='username')],
        [sg.Text('Password:'), sg.InputText(key='password', password_char='*')],
        [sg.Button('Login'), sg.Button('Exit')]
    ]

    window = sg.Window('Secure Login System', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Login':
            username = values['username']
            password = values['password']

            if validate_login(username, password):
                sg.popup_ok('Login successful!')
            else:
                sg.popup_error('Invalid username or password.')

    window.close()

if __name__ == '__main__':
    main()
