def search(frase, word):
    pos = 0
    for l in word:
        pos = frase.find(l,pos)
        if pos == -1:
            return False
    return True

def main():
    word = input("Ingrese una palabra: ")
    frase = input("Ingrese una frase: ")
    if search(frase.lower(),word.lower()):
        print("Yes")
    else:
        print("No")

main()