letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
text =  input("Enter the text: ")
leap = int(input("Enter the Leap of alphabets: "))
def encript(text,leap):
    code1= text
    code = []
    finalcode = ""
    
    for j in code1:
        if j in capitals:
            if j == " ":  
                code.append(" ")
            else:
                for i in range(0, len(capitals)):
                    if capitals[i] == j:
                        if i + leap >= 26:
                            a = 26 - i
                            code.append(capitals[leap - a])
                        else:
                            code.append(capitals[i + leap])
        else:
            if j == " ":  
                code.append(" ")
            else:
                for i in range(0, len(letters)):
                    if letters[i] == j:
                        if i + leap >= 26:
                            a = 26 - i
                            code.append(letters[leap - a])
                        else:
                            code.append(letters[i + leap])
                
    for k in code:
        finalcode = finalcode + k
    
    print(finalcode) 
    
def decrypt(text,leap):
    code1 = text
    real_word = []
    final_decrypt = ""
    for j in code1:
        if j in capitals:
            if j == " ":
                real_word.append(" ")
            else:
                for i in range(0, len(capitals)):
                    if capitals[i] == j:
                        if i - leap <= 0:
                            a = 26 - i
                            real_word.append(capitals[a-1])
                        else:
                            real_word.append(capitals[i - leap])
        else:
            if j == " ":
                real_word.append(" ")
            else:
                for i in range(0, len(letters)):
                    if letters[i] == j:
                        if i - leap <= 0:
                            a = 26 - i
                            real_word.append(letters[a-1])
                        else:
                            real_word.append(letters[i - leap])

    for k in real_word:
        final_decrypt = final_decrypt + k
    
    print(final_decrypt)
encript(text, leap)
decrypt(text, leap)