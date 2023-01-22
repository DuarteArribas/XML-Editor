import PySimpleGUI as sg
import os
from newXmlFileWindow import *
from filePickerWindow import *

def welcomeWindow():
  layout = [
    [[sg.Text("XML GUI",font = 21)]],
    [[sg.Button("New File"),sg.Button("Open File")]],
    [[sg.Button("Exit")]]
  ]
  window = sg.Window("Welcome!",layout,element_justification = "c")
  while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
      break
    if event == "New File":
      window.close()
      return newXMLFileWindow()
    if event == "Open File":
      window.close()
      return filePickerWindow()