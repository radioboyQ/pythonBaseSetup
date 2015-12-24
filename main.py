

import sys,os

def main():
    ##### Sanity checking #####
    #Check current Python version
    checkVersion()
    #Try to import libraries


    ##### Variables #####
    #Debug mode does not require command line args.
    debugMode = True
    if debugMode == True:
        pass
        inputFileName = "someFileName"
    elif len(sys.argv) == 1 and debugMode == False:
        printHelp()


        

    #Check if inputFile is a file
    checkIfFile(inputFileName)

def printHelp():
    print("[*] Usage: " + os.path.basename(__file__) + " command argument thingies. ")
    sys.exit()


def checkIfFile(unTestedFileName):
    #Check if the string provided is actually a file in the system
    #This should work if the file is a symbolic link too
    isFileBool = os.path.isfile(unTestedFileName)
    if isFileBool == True:
        print("[*] Input file exists. Continuing.")
    else: #Input file does not exist or is not a file.
        print("[!] Input file does not exist. ")
        printHelp()


def checkVersion():
    #Check that we are running Python 3 or later
    #If not 3.X then 2.7.X
    ##If not 2.7.X, exit with error
    if sys.version_info >= (3, 0):
        print("[*] Python version greater then 3 detected, continuing. ")
    elif sys.version_info >= (2,7):
        #If 2.7, print warning, but continue
        print("[!] Python version 2.7 detected.  It should work, but Python 3 is reccomended.")
    else:
        #If less then 2.7, exit throwing an error that the version is too old.
        print("[!] Python version is too old! Please run with at least version 3.  \n [!] Exiting.")
        sys.exit()


if __name__ == '__main__':
    main()
