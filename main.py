import PySimpleGUI as sg

XML_FILE = "compsciXml/"

def buildWindow():
  sg.theme('DarkAmber')
  layout = [
    [sg.Table(values = [["arroz"],["massa"]],headings = ["Name"],max_col_width=25, auto_size_columns=True,justification='center',key="xmlTable")],
    [sg.Button('Add'),sg.Button('Remove')],
    [sg.Button('Next'),sg.Button('Previous'),sg.Button("Exit")]
  ]
  window = sg.Window('XML GUI',layout,element_justification = "c")
  xmlTable = window["xmlTable"]
  while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
      break
    print('You entered ', values[0])
  window.close() 

def main():
  mytree = ET.parse("compsciXml/")
  myroot = mytree.getroot()
  buildWindow()

if __name__ == "__main__":
  main()