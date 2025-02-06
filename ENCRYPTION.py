letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text =  input("Enter the text: ")
leap = int(input("Enter the Leap of alphabets: "))
def encript(text,leap):
    code1= text.lower()
    code = []
    finalcode = ""
    for j in code1:
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
    code1 = text.lower()
    real_word = []
    final_decrypt = ""
    for j in code1:
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
# encript(actual_text, leap)
decrypt(text, leap)