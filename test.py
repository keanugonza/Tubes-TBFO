arr= '"'

if arr == "\"":
    print("betul")

    def handlePetik(arr):
    i = 0
    while i <= (len(arr)-1):
        if arr[i] == '"' and arr[i+1] != '"' and ((arr[i+1] != 'GET') and (arr[i+1] != 'POST') and (arr[i+1] != 'submit') and (arr[i+1] != 'reset') and (arr[i+1] != 'button') and (arr[i+1] != 'text') and (arr[i+1] != 'password') and (arr[i+1] != 'email') and (arr[i+1] != 'number') and (arr[i+1] != 'checkbox'))::
            arr.pop(i+1)
            arr.insert(i+1, 'petik')
            i += 3
        i+=1
    return arr