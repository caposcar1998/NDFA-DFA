def main():
    extractDataFile()

def getLetter(line):
    letter = line[line.find(",")+1:line.find("=")]
    print (letter)

def getStates(line):
    state = line.split(',')[0]
    print(state)

def getElements(line):
    splitWith = ">"
    res = line.partition(splitWith)[2] 
    print(res)

def extractDataFile():

    file = "files/test2.txt"
    with open(file) as f:
        line = f.readline()
        lineNumber = 0
        initialNode = None
        finalNode = None
        while line:
            line = f.readline()
            lineNumber += 1
            if (lineNumber == 0):
                print("Nodos")
                print(line)
            if (lineNumber == 1):
                print("lenguaje")
                print(line)
            if (lineNumber == 2):
                initialNode = line
                print("Nodo inicial")
                print (initialNode)
            if (lineNumber == 3):
                finalNode = line
                print("Nodo final")
                print (finalNode)
            if (lineNumber > 3):
                print("Nodo padre")
                getStates(line)
                print("letra que el pertenece")
                getLetter(line)
                print("Elementos que le pertencen")
                getElements(line)

        f.close()

if __name__ == "__main__":
    main()

