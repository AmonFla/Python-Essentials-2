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
    filesplit = filename.split('.')
    filesplit[-1] = 'hist'
    newfile = open('.'.join(filesplit), 'w')
    for lkey in sorted(letters.items(), key=lambda x:x[1], reverse=True):
        newfile.write(lkey[0]+'->'+str(lkey[1])+'\n')


main()