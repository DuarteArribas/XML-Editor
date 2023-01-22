import re
import sys
import PySimpleGUI as sg
from errorWindow import *

def rootPickerWindow():
  layout = [
    [[sg.Text("What is the root element of the new xml file?"),sg.Input(key = "rootEl",font=16)]],
    [[sg.Button("Go"),sg.Button("Exit")]]
  ]
  window   = sg.Window("XML root chooser",layout,element_justification = "c")
  while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
      sys.exit(0)
    if event == "Go":
      root = values["rootEl"]
      if not root:
        continue
      if _validateTag(root):
        window.close()
        return values["rootEl"]
      else:
        errorWindow("Tag error",f"{root} contains invalid characters for xml tags! Check naming rules at https://www.w3schools.com/xml/xml_elements.asp#midcontentadcontainer")

def _validateTag(tag):
  return bool(re.match(r"^[a-zA-Z_][a-zA-Z\d_.-]*$",tag))