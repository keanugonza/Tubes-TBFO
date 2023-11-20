import os
import re


def getCurrentDirectory():
    # Mengembalikan directory saat ini
    return os.path.dirname(os.path.realpath(__file__))


def ReadFile(NamaFile):
    # Mengembalikan Array Tag dari file NamaFile

    # Membaca File
    currentDir = getCurrentDirectory()
    f = open(os.path.join(currentDir, f"{NamaFile}"), 'r')
    arr = f.readlines()
    f.close()

    # Menghilangkan Komentar (<!-- comment -->)
    output = ""
    idxLine = 0
    while idxLine < len(arr):
        output += arr[idxLine]
        idxLine += 1

    
    idxLine = 0
    while idxLine < len(output) - 1:
        if (output[idxLine:idxLine + 4] == '<!--'):
            idxSearch = idxLine + 1
            while idxSearch < len(output):
                if output[idxSearch:idxSearch + 3] == '-->':
                    break
                idxSearch += 1
            output = output[:idxLine] + output[idxSearch + 3:]
        idxLine += 1
        
    idxLine = 0
    while idxLine < len(output) - 1:
        if (output[idxLine] == '>' and output[idxLine + 1].isalpha() == True):
            idxSearch = idxLine
            while idxSearch < len(output):
                if output[idxSearch] == '<':
                    break
                idxSearch += 1
            output = output[:idxLine + 1] + " " + output[idxSearch:]
        idxLine += 1

    return output


def bacaFileTXT(namafile):
    # Prosedur pembacaan namafile
    # Fungsi pembacaan namafile
    # Hasil menjadi array of string

    # KAMUS
    global arraytextfile
    # f : file

    # ALGORITMA
    currentDir = getCurrentDirectory()
    f = open(os.path.join(currentDir, f"../txt/{namafile}"), 'r')
    #arraytextfile = f.readlines()
    arr = f.readlines()
    f.close()

    return arr

def splitSyntax(rawSyntax):
    # Memisahkan string yang terpisah oleh spasi
    processedSyntax = rawSyntax.split(" ")

    # Membuat List Separator
    listOfSeparators = [
        '\n',
        '\<',
        '\>',
        '\/',
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

    idxFind = 0
    while idxFind < len(processedSyntax):
        idxSearch = idxFind + 1

        if processedSyntax[idxFind] == "\"":
            while idxSearch < len(processedSyntax):
                if processedSyntax[idxSearch] == "\"":
                    processedSyntax = processedSyntax[:idxFind] + ["validString"] + processedSyntax[idxSearch + 1:]
                    break
                idxSearch += 1
        
        if processedSyntax[idxFind] == "\'":
            while idxSearch < len(processedSyntax):
                if processedSyntax[idxSearch] == "\'":
                    processedSyntax = processedSyntax[:idxFind] + ["validString"] + processedSyntax[idxSearch + 1:]
                    break
                idxSearch += 1
        
        idxFind += 1

    return processedSyntax
