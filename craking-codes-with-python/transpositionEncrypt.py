import pyperclip


def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    print(ciphertext + '|')

    pyperclip.copy(ciphertext)


def encryptMessage(key, message):
    ciphertext = [''] * key

    for col in range(key):
        pointer = col

    while pointer < len(message):
        ciphertext[col] += message[pointer]
        pointer += key

    return ''.join(ciphertext)


# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function
if __name__ == '__main__':
    main()
