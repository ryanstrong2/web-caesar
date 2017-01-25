def alphabet_position(letter):
    alph = list('abcdefghijklmnopqrstuvwxyz')
    alpha=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for char in range(len(alpha)):
        if alpha[char] == letter:
            return char
        if alph[char]== letter:
            return char
    return letter
def rotate_character(text, rot):
    alph= list('abcdefghijklmnopqrstuvwxyz')
    alpha=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    while rot >= 27:
        rot-=26
    code=0
    cipher=""
    for item in text:
        charNum = alphabet_position(item)
        if charNum == item:
            cipher+=charNum
            continue
        code = charNum + rot
        if item in alpha:
        # if item in string.ascii_uppercase:
            if code < 26:
                cipher = cipher + alpha[code]
            else:
                cipher= cipher + alpha[code%26]
        else:
            if code < 26:
                cipher = cipher + alph[code]
            else:
                cipher= cipher + alph[code%26]
    return cipher

def encrypt(text, rot):
    newstr=""
    index=0
    for letter in text:
        if letter == " ":
            newstr+=" "
        else:
            newstr += rotate_character(letter, alphabet_position(rot))
            index += 1
    return (newstr)
