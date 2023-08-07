import PySimpleGUI as sg 
from login import login_valied

layout = [
    []
    ]

window = sg.Window('App_Name', layout)

if login_valied == True:
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        
    window.close()
