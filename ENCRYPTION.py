letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
code = input("Enter the message: ").lower()

morsecode = []
finalcode = ""
steps = int(input("Enter the gap: "))

for j in code:
    if j == " ":  # Handle spaces directly
        morsecode.append(" ")
    else:
        for i in range(0, len(letters)):
            if letters[i] == j:
                if i + steps >= 26:
                    a = 26 - i
                    morsecode.append(letters[steps - a])
                else:
                    morsecode.append(letters[i + steps])

print(morsecode)

for k in morsecode:
    finalcode = finalcode + k

print(finalcode)