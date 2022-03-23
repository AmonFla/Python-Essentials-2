from re import A


def encrypt(text, pos):
    encrypted = ''
    for t in text:
        if t.isalpha():
            l = ord(t) + pos
            if t >= 'a' and t <= 'z' and l >= ord('z'):
                l = ord('a') + l - ord('z') - 1 
                if l < ord('a'):
                    l = ord('z')
            elif t >= 'A' and t <='Z' and l >= ord('Z'):
                l = ord('A') + l - ord('Z') - 1
                if l < ord('A'):
                    l = ord('Z')
            encrypted += chr(l)
        else:
            encrypted += t
    return encrypted

def main():
    text = input("Text to encrypt: ")
    pos = input("Shift Value (1..25): ")
    while int(pos) < 1 or int(pos) > 25:
        pos = input("Shift Value must be from 1 to 25: ")
    print(encrypt(text, int(pos)))

main()