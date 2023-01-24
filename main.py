from welcomeWindow import *
from treeWindow    import *        
from xmlParser     import *

def main():
  sg.theme('DarkAmber')
  while True:
    xmlFile = welcomeWindow()
    if xmlFile:
      xmlTree = ET.parse(xmlFile)
      xmlRoot = xmlTree.getroot()
      treeWindow(xmlTree,xmlRoot,xmlRoot,xmlFile)

if __name__ == "__main__":
  main()