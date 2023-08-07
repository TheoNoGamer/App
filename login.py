import PySimpleGUI as sg
from subprocess import call
from properties import appname

def VerifyLogin(username, password, filepath):
    try:
        password = password + "\n"
        
        with open(filepath, 'r') as file:
            lines = file.readlines()
            
            for line in lines:
                fields = line.split(",")
                
                if fields[0] == username and fields[1] == password:
                    return True
        
    except Exception as e:
        print(e)
        
    return False

def open_py_file():
    call(["python", appname])

password_char = '*'
password_hidden = True

login_valied = False

layout = [
    [sg.Text('Username'), sg.Input(key='-username-')],
    [sg.Text('Password'), 
     sg.Input(key='-password-', password_char=password_char),  
     sg.Button('Show Password', k='-CB-', button_color=('white', 'green'))],
    [sg.Button('Login', key="-login-")]
]

window = sg.Window('Login', layout)

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    
    if event == '-login-':
        username = values['-username-']
        password = values['-password-']
        
        if VerifyLogin(username, password, "login_data.txt"):
            print("Inloggning lyckades")
            login_valied = True
            print(login_valied)
            open_py_file()
            window.close()
            
        else:
            login_valied = False 
            print(login_valied)
            print("Inloggning misslyckades")
            sg.popup('Try again!')
            
    
    elif event == '-CB-': 
        login_valied = False
        password_hidden = not password_hidden
        if password_hidden:
            window['-CB-'].update(text="Show Password")
            password_char = '*'
            window['-CB-'].update(button_color=('white', 'green'))  
        else:
            window['-CB-'].update(text="Hide Password")
            password_char = ''
            window['-CB-'].update(button_color=('white', 'red')) 
        
        window['-password-'].update(password_char=password_char)

window.close()
