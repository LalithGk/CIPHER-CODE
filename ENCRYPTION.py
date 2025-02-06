letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    code = input("Enter the message: ").lower()
    if " " in code:
        print("Invalid Try without spaces: ")
        continue
    break

morsecode = []
finalcode = ""
steps = int(input("Enter the gap: "))
for i in range(0,len(letters)):
    for j in code:
        if letters[i] == j:
            if i + steps >= 26:
                a = 26 - i
                morsecode.append(letters[steps - a])
            else:

                morsecode.append(letters[i+steps])
for k in morsecode:
    finalcode = finalcode + k
print(finalcode)