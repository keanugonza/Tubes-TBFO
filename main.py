from argparse import ArgumentParser
import sys
import OpenFile

if __name__ == "__main__":
    parser = ArgumentParser()
    if (len(sys.argv)>1) :
        fileName = str(sys.argv[1])
    else :
        fileName = "inputAcc.html"

    arr = OpenFile.ReadRawFile(fileName)
    arr = OpenFile.splitFile(arr)
    arr = OpenFile.handleString(arr)
    arr = OpenFile.handleComment(arr)

    print(arr)
