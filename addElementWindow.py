import PySimpleGUI as sg
from tagValidation import *
from errorWindow   import *

def addHandlerWindow():
  layout = [
    [sg.Text("New Element Name:",font=16),sg.InputText(key = "addInput",font=16)],
    [sg.Text("Description:",font=16),sg.InputText(key = "desc",font=16)],
    [sg.Button("Ok"),sg.Button("Cancel")]
  ]
  window  = sg.Window("Add New element",layout)
  while True:
    event,values = window.read()
    if event == "Cancel" or event == sg.WIN_CLOSED:
      window.close()
      return None,None
    if event == "Ok":
      if not values["addInput"].strip():
        errorWindow("Input Error","Please input a valid name. Empty names are not allowed!")
      else:
        if not validateTag(values["addInput"]):
          errorWindow("Tag Error",f"{values['addInput']} contains invalid characters for xml tags! Check naming rules at https://www.w3schools.com/xml/xml_elements.asp#midcontentadcontainer")
          continue
        window.close()
        return values["addInput"],values["desc"]