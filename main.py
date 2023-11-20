from argparse import ArgumentParser
import sys
import OpenFile

if __name__ == "__main__":
    parser = ArgumentParser()
    if (len(sys.argv)>1) :
        fileName = str(sys.argv[1])
    else :
        fileName = "inputAcc.html"

    arr = OpenFile.ReadFile(fileName)
    arr = OpenFile.splitSyntax(arr)

    print(arr)
