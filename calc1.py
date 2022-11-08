import PySimpleGUI as sg

sg.theme('DarkBrown5')

def reiz(x,y):
  return x*y

def dal(x,y):
    return x/y

def sask(x,y):
    return x+y

def atn(x,y):
    return x-y

layout=[[sg.T('rekinasana')], 
      [sg.T('pirmais skaitlis'), sg.I(key='x')],
      [sg.T('otrais skaitlis'), sg.I(key='y')],
      [sg.T(key='-OUT-')],
      [sg.B('+'), sg.B('*'), sg.B('/'), sg.B('-'), sg.Exit()]]

window=sg.Window('kalkulators', layout)
while True:
    event, values=window.read()
    if event==sg.WIN_CLOSED or event == 'Exit':
        break
    elif event=='*':
        rez=reiz(float(values['x']),float(values['y']))
        window['-OUT-'].update(value=round(rez,2))

    elif event=='/':
        rez=dal(float(values['x']),float(values['y']))
        window['-OUT-'].update(value=round(rez,2))

    elif event=='+':
        rez=sask(float(values['x']),float(values['y']))
        window['-OUT-'].update(value=round(rez,2))

    elif event=='-':
        rez=atn(float(values['x']),float(values['y']))
        window['-OUT-'].update(value=round(rez,2))    

window.close()
