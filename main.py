from welcomeWindow import *
from treeWindow    import *        
from xmlParser     import *

def main():
  sg.theme('DarkAmber')
  xmlFile = welcomeWindow()
  xmlTree = ET.parse(xmlFile)
  xmlRoot = xmlTree.getroot()
  treeWindow(xmlTree,xmlRoot,xmlFile)

if __name__ == "__main__":
  main()