from argparse import ArgumentParser
import sys
import OpenFile
import OpenPDA

if __name__ == "__main__":
    parser = ArgumentParser()
    fileName = sys.argv[2]
    filePDA = sys.argv[1]
    arr = OpenFile.readFile(fileName)
    arr = OpenFile.splitFile(arr)
    arr = OpenFile.handleString(arr)
    arr = OpenFile.handleComment(arr)
    arr = OpenFile.handlePetik(arr)
    arr = OpenFile.getGrammar(arr)
    OpenPDA.start(filePDA)
    OpenPDA.process(arr)
