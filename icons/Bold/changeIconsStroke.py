#coding:utf-8
import os, sys

def printHelpAndExit():
    print("""
Usage:  python3 changeIconStroke.py <newStrokeValue> [newColorHexValue] [directory]
            
        newStrokeValue = 1, ..., 9
        newStrokeValue is an hexadecimal value without #

        Ex: python3 changeIconStroke.py 2 fafaaf
            python3 changeIconStroke.py 3
            python3 changeIconStroke.py 1 ./icons
            python3 changeIconStroke.py 2 fafaaf ./icons
            """)
    exit(0)

################################### VÉRIFICATIONS #####################################
if (len(sys.argv) - 1 == 0):
    printHelpAndExit()
else:
    directory = './'
    if(sys.argv[1] == "-h"):
        printHelpAndExit()
    elif(len(sys.argv) - 1 == 1):
        if(sys.argv[1].isnumeric() and len(sys.argv[1])==1 and sys.argv[1] != '0'):
            files = os.listdir()
            newStrokeValue = sys.argv[1]
        else:
            printHelpAndExit()
    elif(len(sys.argv) - 1 == 2):
        if(sys.argv[1].isnumeric() and len(sys.argv[1])==1 and sys.argv[1] != '0'):
            newStrokeValue = sys.argv[1]
        else:
            printHelpAndExit()
        if(os.path.isdir(sys.argv[2])):
            directory = sys.argv[2]
            files = os.listdir(directory)
        else:
            try:
                int(sys.argv[2], 16) #Si le 2e argument est un hexadécimal il n'y aura pas d'erreur
                newColorHexValue = "#"+sys.argv[2]
                files = os.listdir()
            except:
                printHelpAndExit()
    elif(len(sys.argv) - 1 == 3):
        if(sys.argv[1].isnumeric() and len(sys.argv[1])==1 and sys.argv[1] != '0'):
            newStrokeValue = sys.argv[1]
        else:
            printHelpAndExit()
        if(os.path.isdir(sys.argv[3])):
            directory = sys.argv[3]
            files = os.listdir(directory)
        else:
            printHelpAndExit()
        try:
            int(sys.argv[2], 16) #Si le 2e argument est un hexadécimal il n'y aura pas d'erreur
            newColorHexValue = "#"+sys.argv[2]
        except:
            printHelpAndExit()
    else:
        printHelpAndExit()
################################### FIN VÉRIFICATIONS #####################################

for file in files:
    if(file.find(".svg")+1):
        directoryFile = directory + file if(os.path.exists(directory + file)) else directory + '/' + file
        if(not os.path.exists(directoryFile)):
            printHelpAndExit()
        f = open(directoryFile, "r+")
        code = f.readline()
        if("newColorHexValue" in locals().keys()): #si la variable newColorHexValue existe
            code = code[: code.find('stroke="')+len('stroke="')] + newColorHexValue + code[code.find('"', code.find('stroke="')+len('stroke="')) : code.find('stroke-width="')+len('stroke-width="')] + newStrokeValue + code[code.find('stroke-width="')+len('stroke-width="')+len(newStrokeValue) :]
            f.close()
            f = open(directoryFile, "w")
            f.write(code)
            f.close()
        else:
            f.seek(code.find('stroke-width="')+len('stroke-width="'), 0)
            f.write(newStrokeValue)
            f.close()
