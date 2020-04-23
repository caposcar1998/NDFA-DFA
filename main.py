from extractDataFile import extractDataFile
from nonDeterministicToDeterministic import ndfaTodfa
from nonDeterministicLambdaToNonDeterminstic import lambdaNdfaToNdfa
def main():
    extractDataFile()

    
    lambdaNdfaToNdfa()

    #ndfaTodfa()

if __name__ == "__main__":
    main()

