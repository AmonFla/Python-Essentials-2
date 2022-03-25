def main():
    letters = {}
    filename = input("Filename to read: ")
    file = open(filename,'r')
    for c in file.read():        
        if c.isalnum():
            if c.lower() in letters.keys():
                letters[c.lower()]+=1
            else:
                letters[c.lower()] = 1
    file.close()
    for lkey in sorted(letters):
        print(lkey,'->',letters[lkey])

main()