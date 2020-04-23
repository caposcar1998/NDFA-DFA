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


def getNodesToLambdaWithA(firstNodes, listNodes):

    for node in listNodes:
        if (node['letter'] == "l" ):
            listaCrear = [] 
            print(node)
            getNext( node,"b",listNodes, listaCrear)
            print(listaCrear)
            print("cambio")




def getNext(node, letter, listNodes, listaCrear):
    if("L" in node['elements']     ) :
        listaCrear.append(node)
        return 
    else:
        for node in listNodes:
            if (node['letter'] == "l"):
                newNode = node
    return getNext(newNode, letter, listNodes, listaCrear)

def  lambdaNdfaToNdfa():
    language = ["a","b","l"]
    listNodes= [{'initialNode': True, 'finalNode': False, 'nombreNodo': 'q0', 'letter': 'a', 'elements': ['q0']}, {'initialNode': False, 'finalNode': False, 'nombreNodo': 'q1', 'letter': 'a', 'elements': ['L']}, {'initialNode': False, 'finalNode': False, 'nombreNodo': 'q2', 'letter': 'a', 'elements': ['q1']}, {'initialNode': False, 'finalNode': True, 'nombreNodo': 'q3', 'letter': 'a', 'elements': ['L']}, {'initialNode': True, 'finalNode': False, 'nombreNodo': 'q0', 'letter': 'b', 'elements': ['L']}, {'initialNode': False, 'finalNode': False, 'nombreNodo': 'q1', 'letter': 'b', 'elements': ['q2']}, {'initialNode': False, 'finalNode': False, 'nombreNodo': 'q2', 'letter': 'b', 'elements': ['L']}, {'initialNode': False, 'finalNode': True, 'nombreNodo': 'q3', 'letter': 'b', 'elements': ['L']}, {'initialNode': True, 'finalNode': False, 'nombreNodo': 'q0', 'letter': 'l', 'elements': ['q1']}, {'initialNode': False, 'finalNode': False, 'nombreNodo': 'q1', 'letter': 'l', 'elements': ['q3']}, {'initialNode': False, 'finalNode': False, 'nombreNodo': 'q2', 'letter': 'l', 'elements': ['L']}, {'initialNode': False, 'finalNode': True, 'nombreNodo': 'q3', 'letter': 'l', 'elements': ['L']}]
    firstNodes = getFirstNodes(listNodes)
    finalNodes =  getFinalNodes(listNodes)
    dnfaList = []
    dnfaList.append(firstNodes)
    getNodesToLambdaWithA(firstNodes, listNodes)
   
