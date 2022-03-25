from re import L
from pikepdf import Dictionary


def display(strng):
    line = '###'
    landr = '# #'
    left = '#  '
    right = '  #'
    numbers = { '0': [line,landr,landr,landr, line], '1':[right for i in range(5)],
                '2':[line, right, line,left, line], '3':[line, right, line, right, line],
                '4':[landr, landr, line, right, right],'5':[line, left, line,right, line],
                '6':[line, left, line, landr, line], '7':[line, right, right, right, right],
                '8':[line,landr,line,landr, line], '9':[line, landr, line, right, line]  }
    
    for pos in range(5):
        for n in strng:
            print(numbers[n][pos], ' ', end='')
        print()

def main():
    number = input("Ingrese un número:") 
    display(number)
main()