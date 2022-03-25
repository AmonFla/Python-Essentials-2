def validLines(sudoku):
    for line in sudoku:
        for number in range(1,10):
            pos = 0
            for i in range(2):
                pos = line.find(str(number), pos)
                if pos == -1:
                    return False
    return True

def validColumn(sudoku):
    for col in range(9):
        for number in range(1,10):
            count = 0
            for lin in range (9):
                if sudoku[lin][col] == str(number):
                    count += 1
                    if count == 2:
                        return False
    return True
    
def validSquare(sudoku):
    for sqrcol in range(3):
        for sqrlin in range(3):
            for number in range(1,10):
                count = 0
                for col in range(3):
                    for lin in range (3):
                        if sudoku[lin+sqrlin*3][col+sqrcol*3] == str(number):
                            count += 1
                            if count == 2:
                                return False
    return True
    
def validateSudoku(sudoku):
    if not validLines(sudoku):
        return False
    elif not validColumn(sudoku):
        return False
    elif not validSquare(sudoku):
        return False
    return True

def main():
    sudoku = []
    for i in range(9):
        sudoku.append(input("Ingrese una línea del sudoky: "))
    # sudoku=['295743861','431865927','876192543','387459216','612387495','549216738','763524189','928671354','154938672'] # result = yes
    # sudoku=['195743862','431865927','876192543','387459216','612387495','549216738','763524189','928671354','254938671'] # result = no
    if validateSudoku(sudoku):
        print("Yes")
    else:
        print("No")

main()

