import PySimpleGUI as sg

def confirmWindow(xmlEl):
  layout = [
    [sg.Text(f"Do you want to remove {xmlEl}?")],
    [sg.Button("Yes"),sg.Button("No")]
  ]
  window = sg.Window("Confirmation",layout)
  while True:
    event,values = window.read()
    if event == "Yes":
      window.close()
      return True
    if event == "No" or event == sg.WIN_CLOSED:
      window.close()
      return False