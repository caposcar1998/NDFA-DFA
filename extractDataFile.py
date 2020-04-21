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
    node =	{
    "initialNode": initialNode,
    "finalNode": finalNode,
    "nombreNodo": nombreNodo,
    "letter": letters,
    "elements": elements
    }
    return node

def extractDataFile():

    file = "files/test2.txt"
    with open(file) as f:
        line = f.readline()
        lineNumber = 0
        initialNode = None
        finalNode = None
        listNodes = []
        while line:
            line = f.readline()
            lineNumber += 1
            if (lineNumber < 1):
                print(line)
            if (lineNumber == 1):
                #Imprime el afabeto
                pass
            if (lineNumber == 2):
                initialNode = line
                groupInitNodes = initialNode.split(',')
            if (lineNumber == 3):
                finalNode = line
                groupFinalNodes = finalNode.split(',')
            if (lineNumber > 3):
                if(getStates(line).rstrip("\n") == ""):
                    continue
                if (getStates(line).rstrip('\n') in finalNode.rstrip('\n') and getStates(line).rstrip('\n') in initialNode.rstrip('\n')):
                   listNodes.append(createDictionary(True, True, getStates(line), getLetter(line), getElements(line).rstrip('\n').split(',')))
                elif (getStates(line).rstrip('\n') not in initialNode.rstrip('\n') and getStates(line).rstrip('\n') in finalNode.rstrip('\n')):
                    listNodes.append(createDictionary(False, True, getStates(line), getLetter(line), getElements(line).split(',')))
                elif (getStates(line).rstrip('\n') in initialNode.rstrip('\n') and getStates(line).rstrip('\n') not in finalNode.rstrip('\n')):
                    listNodes.append(createDictionary(True, False, getStates(line), getLetter(line), getElements(line).rstrip('\n').split(',')))
                else:
                    listNodes.append(createDictionary(False, False, getStates(line), getLetter(line), getElements(line).rstrip('\n').split(',')))
        f.close()
        print(listNodes)

