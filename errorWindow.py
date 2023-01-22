import PySimpleGUI as sg

def errorWindow(errorTitle,errorMsg):
  layout = [
    [sg.Text(errorMsg,size=(len(errorMsg),1),font=16)],
    [sg.Button("Ok")]
  ]
  window = sg.Window(errorTitle,layout,element_justification = "c")
  while True:
    event,values = window.read()
    if event == "Ok" or event == sg.WIN_CLOSED:
      window.close()
      break