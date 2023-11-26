from argparse import ArgumentParser
import sys
import OpenFile
import pda

if __name__ == "__main__":
    parser = ArgumentParser()
<<<<<<< Updated upstream
    if (len(sys.argv)>1) :
        fileName = str(sys.argv[1])
    else :
        fileName = "test.html"

    arr = OpenFile.ReadRawFile(fileName)
=======
    fileName = sys.argv[2]
    filePDA = sys.argv[1]
    arr = OpenFile.readFile(fileName)
>>>>>>> Stashed changes
    arr = OpenFile.splitFile(arr)
    arr = OpenFile.handleString(arr)
    arr = OpenFile.handleComment(arr)
    arr = OpenFile.handlePetik(arr)
    arr = OpenFile.getGrammar(arr)
<<<<<<< Updated upstream


    print(arr)
=======
    pda.start(filePDA)
    pda.process(arr)
>>>>>>> Stashed changes
