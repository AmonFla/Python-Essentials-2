from importlib.resources import contents
import os.path

class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    # Write your code here.
    pass

class FileEmpty(StudentsDataException):
    # Write your code here.
    pass

class FileNoExists(StudentsDataException):
    # Write your code here.
    pass

def main():
    notes = {}
    try:
        filename = input('Filename: ')
        if not os.path.exists(filename):
            raise FileNoExists('File not exists')       
        if os.path.getsize(filename) == 0:
            raise FileEmpty('Empty File')
        file = open(filename,'rt')
        for line in file:
            line = line.replace('\n','')
            columns = line.split(' ')
            if len(columns) != 3:
                raise BadLine("Each line must contains 3 elements")
            else:                
                try:
                    columns[2] = float(columns[2])
                except ValueError:
                    raise BadLine("Last element must be a float")
            name = columns[0]+' '+columns[1]
            if name in notes.keys():
                notes[name]+=float(columns[2])
            else:
                notes[name]=float(columns[2])
        file.close()
    except (FileNoExists,FileEmpty) as e:
        print(e)
    except BadLine as e:
        print(e)
        file.close()
    except Exception as e:
        print(e)
    else:
        for n in sorted(notes):
            print(n,notes[n], sep='\t')
main()
