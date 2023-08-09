import PySimpleGUI as sg
import time
from subprocess import call

error = False

userdata = [#putt usrname and password here
    #username, password
    "SapphireUser, Diamond$123",
    "QuantumCoder, Entanglement#",
    "NebulaExplorer, Cosmic*Wander",
    "CyberPhoenix, Firewall@987",
    "EnchantedElf, MagicForest$",
    "SolarSailor, Starship2023",
    "GalacticGourmet, TasteTheStars",
    "ChronoTraveler, TimeWarp*55",
    "AquaAdventurer, DeepSea$Dive",
    "CelestialDreamer, DreamBig#2023",
    ", "#remove for safety
]

def the_login_error():
    global error
    
    if error == True:
        print("Error is True")
        error = False
        popup_result = sg.popup_ok_cancel("An error occurred while verifying userdata", keep_on_top=True)
        
        if popup_result == 'OK':
            run_login_system()

def VerifyLogin(username, password, userdata):
    global error
    global login_check
    
    if login_check == True:
        error = False
        try:
            for user_info in userdata:
                fields = user_info.split(', ')
                if len(fields) >= 2 and fields[0] == username and fields[1] == password:
                    return True
            
        except Exception as e:
            print(e)
            
        return False
    else:
        error = True
        the_login_error()



def run_application():
    global login_valied
    global error
    
    if login_valied == True:
        error = False
        login_valied = False
        
        layout = [
                [sg.Text('test text')]
                ]

        window = sg.Window('App_Name', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
                
        window.close()
        
    else:
        error = True
        login_valied = False
        the_login_error()

def run_login_system():
    global login_valied
    global error
    global login_check
    
    password_char = '*'
    password_hidden = True
    login_valied = False
    login_check = False

    layout = [
        [sg.Text('Username'), 
         sg.Input(key='-username-')],
        
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
            
            login_check = True
            if VerifyLogin(username, password, userdata):
                print("Login succeeded")
                login_valied = True
                print(login_valied, login_check)
                login_check = False
                print(login_check)
                window.close()
                time.sleep(0.9)
                run_application()
                login_valied = False
                print(login_valied)
                
            else:
                login_check = False
                login_valied = False 
                print(login_valied, login_check)
                print("Login failed")
                sg.popup('Try again!')
        
        elif event == '-CB-': 
            login_valied = False
            password_hidden = not password_hidden
            if password_hidden:
                password_char = '*'
                window['-CB-'].update(text="Show Password")
                window['-CB-'].update(button_color=('white', 'green'))  
            else:
                password_char = ''
                window['-CB-'].update(text="Hide Password")
                window['-CB-'].update(button_color=('white', 'red')) 
            
            window['-password-'].update(password_char=password_char)

    window.close()

#The start
run_login_system()
