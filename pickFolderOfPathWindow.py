import PySimpleGUI as sg
import os
from errorWindow import *

def newXMLFileWindow():
  layout = [
    [[sg.Text("Choose a location to generate the file path: "),sg.Input(key = "folderLocation",font=16),sg.FolderBrowse()]],
    [[sg.Button("Go"),sg.Button("Go Back")]]
  ]
  window = sg.Window("Select Location",layout,element_justification = "c")
  while True:
    event,values = window.read()
    if event == "Go":
      if not os.path.isdir(values["folderLocation"]):
        errorWindow("Location Error","The location you provided does not exist!")
        continue
      window.close()
      return values["folderLocation"]
    if event == "Go Back":
      window.close()
      return None
    window.close()