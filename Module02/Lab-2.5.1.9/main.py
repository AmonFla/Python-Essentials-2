def DigitOfLife(number):
    while (len(number) != 1):
        digit = 0
        for n in number:
            digit += int(n)
        number = str(digit) 
    return digit

def main():
    date = input('Write a date (YYYYMMDD/YYYDDMM/MMDDYYYY): ')
    while not date.isdigit() or len(date) != 8:
        date = input('Wrong format. Write a date (YYYYMMDD/YYYDDMM/MMDDYYYY): ')
    print(DigitOfLife(date))
main()