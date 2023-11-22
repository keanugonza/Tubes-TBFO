import os
import re


def getCurrentDirectory():
    # Mengembalikan directory saat ini
    return os.path.dirname(os.path.realpath(__file__))


def ReadRawFile(NamaFile):

    # Membaca File
    currentDir = getCurrentDirectory()
    f = open(os.path.join(currentDir, f"{NamaFile}"), 'r')
    arr = f.readlines()
    f.close()

    output = ""
    idxLine = 0
    while idxLine < len(arr):
        output += arr[idxLine]
        idxLine += 1

    return output

def splitFile(rawFile):
    # Memisahkan string yang terpisah oleh spasi
    processedSyntax = rawFile.split(" ")

    # Membuat List Separator
    listOfSeparators = [
        '\n',
        r'\<',
        r'\>',
        r'\!',
        r'\-',
        r'\=',
        r'\"',
    ]

    for separator in listOfSeparators:
        tempSyntax = []

        for s in processedSyntax:
            tempSyntax += re.split(rf'({separator})', s)

        processedSyntax = tempSyntax

    while '' in processedSyntax:
        processedSyntax.remove('')
    
    while '\n' in processedSyntax:
        processedSyntax.remove('\n')

    return processedSyntax

def handleString(arr):
    for i in range (len(arr)-1):
        if arr[i] == '>' and arr[i+1] != '<':
            while i+1 < len(arr) and arr[i+1] != '<':
                arr.pop(i+1)
                arr.insert(i+1, 'string')
                i += 1
    return arr

def handleComment(arr):
    for i in range (len(arr)-3):
        if arr[i] == '<' and arr[i+1] == '!' and arr[i+2] == '-' and arr[i+3] == '-':
            while i+4 < len(arr) and not(arr[i+4] == '-'):
                if (arr[i+4] == '<'):
                    break
                arr.pop(i+4)
                arr.insert(i+4, 'komen')
                i += 1
    return arr

# def handleTag(arr):
#         for i in range (len(arr)):
#             if arr[i] == '<' 
