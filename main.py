from argparse import ArgumentParser
import sys
import OpenFile
# import TXT_to_DICT
# import FA
# from CFG_to_CNF import CFGtoCNF
# from CYK import cyk

if __name__ == "__main__":
    parser = ArgumentParser()
    if (len(sys.argv)>1) :
        fileName = str(sys.argv[1])
    else :
        fileName = "inputAcc.html"

    arr = OpenFile.ReadFile(fileName)
    arr = OpenFile.splitSyntax(arr)

    print(arr)
