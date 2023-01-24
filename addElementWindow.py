import PySimpleGUI as sg

def addHandlerWindow():
  layout = [
    [sg.Text("New Element Name:",font=16),sg.InputText(key = "addInput",font=16)],
    [sg.Button("Ok"),sg.Button("Cancel")]
  ]
  window  = sg.Window("Add New element!",layout)
  while True:
    event,values = window.read()
    if event == "Cancel" or event == sg.WIN_CLOSED:
      window.close()
      return None
    if event == "Ok":
      if not values['addInput'].strip():
        errorHandlerWindow("Please input a valid name. Empty names are not allowed!")
      else:
        window.close()
        return values['addInput']