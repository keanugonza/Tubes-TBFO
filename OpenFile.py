import os
import re


def getDirectory():
    # Mengembalikan directory saat ini
    return os.path.dirname(os.path.realpath(__file__))


def readFile(NamaFile):
    # Membaca File
    currentDir = getDirectory()
    f = open(os.path.join(currentDir, f"TESTFILE", f"{NamaFile}"), 'r')
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
        '--',
        r'\=',
        r'\"',
    ]

    # Memisahkan string berdasarkan List Separator
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
    # Menghandle string yang bisa menimbulkan error
    for i in range (len(arr)-1):
        if arr[i] == '>' and arr[i+1] != '<':
            while i+1 < len(arr) and arr[i+1] != '<':
                arr.pop(i+1)
                arr.insert(i+1, 'string')
                i += 1
    return arr

def handlePetik(arr):
    # Menghandle petik dan elemen didalamnya yang harus sesuai dengan spesifikasi
    i = 0
    while i <= (len(arr)-1):
        if arr[i] == '"' and arr[i+1] != '"' and arr[i-1] !='"':
            while i <= (len(arr)-1) and arr[i+1] != '"':
                if ((arr[i+1] != 'GET') and (arr[i+1] != 'POST') and (arr[i+1] != 'submit') and (arr[i+1] != 'reset') and (arr[i+1] != 'button') and (arr[i+1] != 'text') and (arr[i+1] != 'password') and (arr[i+1] != 'email') and (arr[i+1] != 'number') and (arr[i+1] != 'checkbox')):
                    arr.pop(i+1)
                    arr.insert(i+1, 'petik')
                i += 1
            i += 3
        i+=1
    return arr

def handleComment(arr):
    # Menghandle comment yang bisa menimbulkan error
    for i in range (len(arr)-2):
        if arr[i] == '<' and arr[i+1] == '!' and arr[i+2] == '--':
            while i+3 < len(arr) and not(arr[i+3] == '--'):
                if (arr[i+3] == '<'):
                    break
                arr.pop(i+3)
                arr.insert(i+3, 'coment')
                i += 1
    return arr

def getGrammar(processedSyntax):
    # Membuat grammar dari arr string yang telah diproses sebelumnya menjadi simbol simbol
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
        elif i == "--" :
            grammar += "-"
        elif i == "coment" :
            grammar += "/"
        elif i == "string" :
            grammar += "~"
        elif i == "submit" :
            grammar += "`"
        elif i == "reset" :
            grammar += "`"
        elif i == "GET" :
            grammar += "+"
        elif i == "POST" :
            grammar += "+"
        elif i == "text" :
            grammar += ";"
        elif i == "password" :
            grammar += ";"
        elif i == "email" :
            grammar += ";"
        elif i == "number" :
            grammar += ";"
        elif i == "checkbox" :
            grammar += ";"
        elif i == "petik":
            grammar += "*"
        else:
            grammar += "."
    return grammar
