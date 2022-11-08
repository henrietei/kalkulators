'''import PySimpleGUI as sg

sg.theme('DarkBrown5')


class Logs:

    def cik(x,y):
        return x*y

    layout=[[sg.T('rekinasana')],
        [sg.T('pirmais skaitlis'), sg.I(key='x')],
        [sg.T('otrais skaitlis'), sg.I(key='y')],
        #[sg.I(key='-IN-')],
        [sg.T(key='-OUT-')],
        [sg.B('+'), sg.B('*'), sg.B('/'), sg.B('-'), sg.Exit()]]

    window=sg.Window('kalkulators', layout)

    while True:
        event, values=window.read()
        if event==sg.WIN_CLOSED or event == 'Exit':
            break
        elif event=='*':
            #rez=cik(float(values['-IN-']))
            rez=cik(float(values['x']))
            
            window['-OUT-'].update(value=round(rez,2))

    window.close()'''