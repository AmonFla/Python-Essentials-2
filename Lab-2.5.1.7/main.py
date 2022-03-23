def cleantext(text):
    text = text.upper()
    text = text.replace(' ','')
    return text

def palindrome01(text):
    for i in range(len(text)//2):
        if text[i] != text[len(text)-1-i]:
            return "It's not a palindrome"
    return "It's a palindrome"

def palindrome02(text):
    if text == text[len(text)::-1]:
        return "It's a palindrome"
    return "It's not a palindrome"
    
 
def main():
    text = input('Write a text: ')
    print(palindrome01(cleantext(text)))
    print(palindrome02(cleantext(text)))
main()