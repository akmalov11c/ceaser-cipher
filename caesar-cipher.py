# A Caesar Cipher Program
import os.path

def welcome():
    print("Welcome to the Caesar Cipher\nThis program encrypts and decrypts text with the Caesar Cipher. ")
    return

def enter_message():
    mode = ''
    message = ''
    shift = 0
    while mode != 'e' and mode != 'd':
        mode = input("Would you like to encrypt (e) or decrypt (d)? : ")
        if mode == 'e':
            while not message:
                message = input("What message would you like to encrypt: ")
                if not message:
                    print("Invalid Message")
            while True:
                shift = input("What is the shift number: ")
                if not shift.isdigit():
                    print("Invalid Shift")
                else:
                    shift = int(shift)
                    break
        elif mode == 'd':
            while not message:
                message = input("What message would you like to decrypt: ")
                if not message:
                    print("Invalid Message")
            while True:
                shift = input("What is the shift number: ")
                if not shift.isdigit():
                    print("Invalid Shift")
                else:
                    shift = int(shift)
                    break
        else:
            print("Invalid Mode ")
    return (mode, message.upper(), shift)


def encrypt(message,shift):
    encrypted_message = ''
    for letter in message.upper():
        if letter.isalpha():
            shifted_letter = ord(letter) + shift
            if shifted_letter > ord('Z'):
                shifted_letter -= 26
            elif shifted_letter < ord('A'):
                shifted_letter += 26
            encrypted_message += chr(shifted_letter)
        else:
            encrypted_message += letter
    return encrypted_message



def decrypt(message,shift):
    return encrypt(message, -shift)


def process_file(filename, mode,shift):
    list_messages = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip('\n')
            if mode == 'e':
                processed_message = encrypt(line, shift)
            elif mode == 'd':
                processed_message = decrypt(line, shift)
            else:
                print("Invalid Mode")
                return []

            list_messages.append(processed_message)
    return list_messages

def write_messages(lines):
    with open("results.txt", 'w') as file:
        for line in lines:
            file.write(line + '\n')
        print("Output written to results.txt")
    return


def is_file(filename):
    if os.path.isfile(filename):
        return True
    else:
        return False


def message_or_file():
    mode = ''
    filename = None
    message = None
    shift = 0

    while mode not in ['e', 'd']:
        mode = input("Would you like to encrypt (e) or decrypt (d)? : ")
        if mode not in ['e', 'd']:
            print("Invalid Mode")

    src = ''
    while src not in ['c', 'f']:
        src = input("Would you like to read from a file (f) or the console (c)? : ")
        if src == 'f':
            filename = ""
            while not os.path.isfile(filename):
                filename = input("Enter a filename: ")
                if not os.path.isfile(filename) or filename == '':
                    print("Invalid Filename")
                else:
                    shift_input = input("What is the shift number: ")
                    while not shift_input.isdigit():
                        print("Invalid Shift")
                        shift_input = input("What is the shift number: ")
                    shift = int(shift_input)
        elif src == 'c':
            if mode == 'e':
                while not message:
                    message = input("What message would you like to encrypt: ")

            if mode == 'd':
                while not message:
                    message = input("What message would you like to decrypt: ")

            if (mode == 'e' or mode == 'd') and src == 'c':
                shift_input = input("What is the shift number: ")
                while not shift_input.isdigit():
                    print("Invalid Shift")
                    shift_input = input("What is the shift number: ")
                shift = int(shift_input)
    return (mode, message, filename, shift)
    
def main():
    welcome()

    while True:
        mode, message, filename, shift = message_or_file()

        if mode == 'e':
            if filename:
                lines = process_file(filename, mode, shift)
                write_messages(lines)
            else:
                encrypted = encrypt(message, shift)
                print(encrypted)
        elif mode == 'd':
            if filename:
                lines = process_file(filename, mode, shift)
                write_messages(lines)
            else:
                decrypted = decrypt(message, shift)
                print(decrypted)

        another = ''
        while another not in ['y', 'n']:
            another = input('Would you like to encrypt or decrypt another message? (y/n): ')
            if another not in ['y', 'n'] or another == '':
                print('Invalid Mode')
        if another == 'n':
            print("Thanks for using the program, goodbye!")
            break


# Program execution begins here
if __name__ == '__main__':
    main()
