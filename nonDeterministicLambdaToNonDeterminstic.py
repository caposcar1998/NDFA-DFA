from extractDataFile import createDictionary


def getFirstNodes(listNodes):
    firstNodes =[]
    for node in listNodes:
        if(node["initialNode"] == True):
            firstNodes.append(node)
    return firstNodes

def getFinalNodes(listNodes):
    finalNodes= []
    for node in listNodes:
        if(node["finalNode"] == True):
            finalNodes.append(node)
    return finalNodes

def getNodesToLambdaGeneral(firstNodes, listNodes):
    
    tableNodes = []
    lamndaNodes= []
    for node in listNodes:
        if (node['letter'] == "l" ):
            lamndaNodes.append(node)
    
    for lambdaNode in lamndaNodes:
        resultNodes=[]
        resultNodes.append(lambdaNode)
        getLambdaNodes( lambdaNode,lamndaNodes,resultNodes)
        tableNodes.append(resultNodes)

    return tableNodes
            
def getLambdaNodes(node, listNodes,resultNodes):

    if("L" in node['elements'] ):
        resultNodes.append(node)
        return
    else:
        for newNode in listNodes:
            if(newNode["nombreNodo"] in node['elements']):
                resultNodes.append(newNode)
        return(getLambdaNodes(newNode, listNodes,resultNodes))
        
def getLettersNodes(lambdaNodes, listNodes,letter,secondRow):
    for lambdaNode in lambdaNodes:
        letterList = []
        for nodeInfo in lambdaNode:
            for checkNode in listNodes:
                if((nodeInfo["elements"][0] == checkNode["nombreNodo"] or nodeInfo["nombreNodo"] == checkNode["nombreNodo"]) and checkNode["letter"] == letter):
                    if(checkNode["elements"][0] != "L"):
                        letterList.append(checkNode)
        secondRow.append(letterList)



def getLastLambdaNodes(secondRow, listNodes, thirdRow, letter):
    lambaNodes =[]
    resultNodes=[]
    for letterRow in secondRow:
        print()
        print(letterRow)
        for value in letterRow:
            for checkNode in listNodes:
                if (value["elements"][0] ==  checkNode["nombreNodo"]):
                    if (checkNode["elements"][0] != "L" and checkNode["letter"] == letter):
                        print(checkNode['nombreNodo'])
                    if (checkNode["letter"] == "l"): 
                        thirdRowRecursion(checkNode, listNodes,resultNodes)


def thirdRowRecursion(node, listNodes, resultNodes):
    if ("L" in node["elements"] ):
        print(node['nombreNodo'])
        return
    else:
        for checkNode in listNodes:
            if (checkNode["nombreNodo"] in node['elements']):
                print(checkNode['nombreNodo'])
        return(thirdRowRecursion(checkNode, listNodes, resultNodes))


def  lambdaNdfaToNdfa():
    language = ["a","b","l"]
    listNodes= [{'initialNode': True, 'finalNode': False, 'nombreNodo': 'q0', 'letter': 'a', 'elements': ['q0']}, {'initialNode': False, 'finalNode': False, 'nombreNodo': 'q1', 'letter': 'a', 'elements': ['L']}, {'initialNode': False, 'finalNode': False, 'nombreNodo': 'q2', 'letter': 'a', 'elements': ['q1']}, {'initialNode': False, 'finalNode': True, 'nombreNodo': 'q3', 'letter': 'a', 'elements': ['L']}, {'initialNode': True, 'finalNode': False, 'nombreNodo': 'q0', 'letter': 'b', 'elements': ['L']}, {'initialNode': False, 'finalNode': False, 'nombreNodo': 'q1', 'letter': 'b', 'elements': ['q2']}, {'initialNode': False, 'finalNode': False, 'nombreNodo': 'q2', 'letter': 'b', 'elements': ['L']}, {'initialNode': False, 'finalNode': True, 'nombreNodo': 'q3', 'letter': 'b', 'elements': ['q3']}, {'initialNode': True, 'finalNode': False, 'nombreNodo': 'q0', 'letter': 'l', 'elements': ['q1']}, {'initialNode': False, 'finalNode': False, 'nombreNodo': 'q1', 'letter': 'l', 'elements': ['q3']}, {'initialNode': False, 'finalNode': False, 'nombreNodo': 'q2', 'letter': 'l', 'elements': ['L']}, {'initialNode': False, 'finalNode': True, 'nombreNodo': 'q3', 'letter': 'l', 'elements': ['L']}]
    firstNodes = getFirstNodes(listNodes)
    finalNodes =  getFinalNodes(listNodes)
    dnfaList = []
    dnfaList.append(firstNodes)
    lambdaNodes = getNodesToLambdaGeneral(firstNodes, listNodes)
    secondRow=[]
    getLettersNodes(lambdaNodes,listNodes,"a",secondRow)
    thirdRow=[]
    getLastLambdaNodes(secondRow, listNodes, thirdRow, "a")

    """
    print("resultado")
    print("tablaUno")
    for lambdaRow in lambdaNodes:
        for node in lambdaRow:
            print(node)
        print("cambio")
    print("tablaDos")
    for letterRow in secondRow:
        print(letterRow["elements"])
    print("tablaTres")
    for lambdaRow in thirdRow:
        print(lambdaRow)
    """
