from extractDataFile import createDictionary


def getFirstNode(listNodes):
    firstNode =None
    for node in listNodes:
        if(node["initialNode"] == True):
            firstNode = node
    return firstNode

def getFinalNodes(listNodes):
    finalNodes= []
    for node in listNodes:
        if(node["finalNode"] == True):
            finalNodes.append(node)
    return finalNodes

def ndfaTodfa():
    listNodes = [{'initialNode': True, 'finalNode': True, 'nombreNodo': 'q0', 'letter': 'a', 'elements': ['q0', 'q1']}, {'initialNode': False, 'finalNode': True, 'nombreNodo': 'q1', 'letter': 'a', 'elements': ['q0', 'q1']}]
    firstNode = getFirstNode(listNodes)
    finalNodes = getFinalNodes(listNodes)
    dfaList = []
    dfaList.append(firstNode)

    