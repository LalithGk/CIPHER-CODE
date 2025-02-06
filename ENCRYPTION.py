letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encript(code,steps):
    code1= code.lower()
    morsecode = []
    finalcode = ""
    for j in code1:
        if j == " ":  
            morsecode.append(" ")
        else:
            for i in range(0, len(letters)):
                if letters[i] == j:
                    if i + steps >= 26:
                        a = 26 - i
                        morsecode.append(letters[steps - a])
                    else:
                        morsecode.append(letters[i + steps])
    for k in morsecode:
        finalcode = finalcode + k
    
    print(finalcode) 
    
def decrypt(code,steps):
    code1 = code.lower()
    morsecode = []
    finalcode = ""
    for j in code1:
        if j == " ":
            morsecode.append(" ")
        else:
            for i in range(0, len(letters)):
                if letters[i] == j:
                    if i - steps <= 0:
                        a = 26 - i
                        morsecode.append(letters[a-1])
                    else:
                        morsecode.append(letters[i - steps])
    for k in morsecode:
        finalcode = finalcode + k
    
    print(finalcode)
encript("z i", 2)
decrypt("a", 1)