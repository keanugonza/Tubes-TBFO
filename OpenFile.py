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
        if (output[idxLine] == '>' and output[idxLine + 1]!='<'):
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
    # arraytextfile = f.readlines()
    arr = f.readlines()
    f.close()

    return arr

def splitSyntax(rawSyntax):
    # Memisahkan string yang terpisah oleh spasi
    processedSyntax = rawSyntax.split(" ")

    # Membuat List Separator
    listOfSeparators = [
        '\n',
        r'\<',
        r'\>',
        r'\/',
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

def getGrammar(processedSyntax):
    grammar = ""
    for i in processedSyntax :
        if i == "html" :
            grammar += "A"
        elif i == "/html" :
            grammar += "a"
        elif i == "head" :
            grammar += "B"
        elif i == "/head" :
            grammar += "b"
        elif i == "body" :
            grammar += "C"
        elif i == "/body" :
            grammar += "c"
        elif i == "title" :
            grammar += "D"
        elif i == "/title" :
            grammar += "d"
        elif i == "link" :
            grammar += "1"
        elif i == "rel" :
            grammar += "2"
        elif i == "href" :
            grammar += "3"
        elif i == "script" :
            grammar += "("
        elif i == "/script" :
            grammar += ")"
        elif i == "src" :
            grammar += "4"
        elif i == "h1" :
            grammar += "T"
        elif i == "/h1" :
            grammar += "t"
        elif i == "h2" :
            grammar += "U"
        elif i == "/h2" :
            grammar += "u"
        elif i == "h3" :
            grammar += "V"
        elif i == "/h3" :
            grammar += "v"
        elif i == "h4" :
            grammar += "W"
        elif i == "/h4" :
            grammar += "w"
        elif i == "h5" :
            grammar += "X"
        elif i == "/h5" :
            grammar += "x"
        elif i == "h6" :
            grammar += "Y"
        elif i == "/h6" :
            grammar += "y"
        elif i == "p" :
            grammar += "F"
        elif i == "/p" :
            grammar += "f"
        elif i == "br" :
            grammar += "5"
        elif i == "em" :
            grammar += "G"
        elif i == "/em" :
            grammar += "g"
        elif i == "b" :
            grammar += "H"
        elif i == "/b" :
            grammar += "h"
        elif i == "abbr" :
            grammar += "I"
        elif i == "/abbr" :
            grammar += "i"
        elif i == "strong" :
            grammar += "J"
        elif i == "/strong" :
            grammar += "j"
        elif i == "small" :
            grammar += "K"
        elif i == "/small" :
            grammar += "k"
        elif i == "hr" :
            grammar += "6"
        elif i == "div" :
            grammar += "L"
        elif i == "/div" :
            grammar += "l"
        elif i == "a" :
            grammar += "M"
        elif i == "/a" :
            grammar += "m"
        elif i == "img" :
            grammar += "7"
        elif i == "alt" :
            grammar += "8"
        elif i == "button" :
            grammar += "N"
        elif i == "/button" :
            grammar += "n"
        elif i == "type" :
            grammar += "0"
        elif i == "form" :
            grammar += "O"
        elif i == "/form" :
            grammar += "o"
        elif i == "action" :
            grammar += "@"
        elif i == "method" :
            grammar += "#"
        elif i == "input" :
            grammar += "9"
        elif i == "table" :
            grammar += "P"
        elif i == "/table" :
            grammar += "p"
        elif i == "tr" :
            grammar += "Q"
        elif i == "/tr" :
            grammar += "q"
        elif i == "td" :
            grammar += "R"
        elif i == "/td" :
            grammar += "r"
        elif i == "th" :
            grammar += "S"
        elif i == "/th" :
            grammar += "s"
        elif i == "id" :
            grammar += "$"
        elif i == "class" :
            grammar += "%"
        elif i == "style" :
            grammar += "^"
        elif i == "=" :
            grammar += "="
        elif i == "\"" :
            grammar += "\""
        elif i == "<" :
            grammar += "<"
        elif i == ">" :
            grammar += ">"
        elif i == "!" :
            grammar += "!"
        elif i == "-" :
            grammar += "-"
        elif i == "coment" :
            grammar += "/"
        elif i == "string" :
            grammar += "~"
    return grammar
