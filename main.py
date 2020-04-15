def main():
    extractDataFile()

def getLetter(line):
    letter = line[line.find(",")+1:line.find("=")]
    return letter

def getStates(line):
    state = line.split(',')[0]
    state.strip()
    return state

def getElements(line):
    splitWith = ">"
    res = line.partition(splitWith)[2] 
    return res

def createDictionary(initialNode, finalNode, nombreNodo, letters, elements):
    nombreNodo =	{
    "initialNode": initialNode,
    "finalNode": finalNode,
    "nombreNodo": nombreNodo,
    letters: elements
    }
    print(nombreNodo)

def extractDataFile():

    file = "files/test1.txt"
    with open(file) as f:
        line = f.readline()
        lineNumber = 0
        initialNode = None
        finalNode = None
        while line:
            line = f.readline()
            lineNumber += 1
            if (lineNumber == 0):
                pass
            if (lineNumber == 1):
                pass
            if (lineNumber == 2):
                initialNode = line
                groupInitNodes = initialNode.split(',')
            if (lineNumber == 3):
                finalNode = line
                groupFinalNodes = finalNode.split(',')
            if (lineNumber > 3):
                if (getStates(line).rstrip('\n') in finalNode.rstrip('\n') and getStates(line).rstrip('\n') in initialNode.rstrip('\n')):
                   createDictionary(True, True, getStates(line), getLetter(line), getElements(line)) 
                elif (getStates(line).rstrip('\n') not in initialNode.rstrip('\n') and getStates(line).rstrip('\n') in finalNode.rstrip('\n')):
                    createDictionary(False, True, getStates(line), getLetter(line), getElements(line))
                elif (getStates(line).rstrip('\n') in initialNode.rstrip('\n') and getStates(line).rstrip('\n') not in finalNode.rstrip('\n')):
                    createDictionary(True, False, getStates(line), getLetter(line), getElements(line).rstrip('\n'))
                else:
                    createDictionary(False, False, getStates(line), getLetter(line), getElements(line).rstrip('\n'))
        f.close()

if __name__ == "__main__":
    main()

