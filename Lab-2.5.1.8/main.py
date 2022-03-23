def countLetters(letter, text):
    count = 0
    for l in text:
        if letter == l:
            count+=1
    return count 

def areAnagram(text1,text2):
    for l in text1:
        if countLetters(l,text2) != countLetters(l,text1):
            return False
    return True

def main():
    text1 = input('Add first text: ')
    text2 = input('Add second text: ')
    if areAnagram(text1.upper(), text2.upper()):
        print("Anagrams")
    else:
        print("Not anagrams")

main()