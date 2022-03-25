from sys import path

path.append('../modules') #funciona si lo ejecuto desde la carpeta donde esta el main.py
# si no estoy en la carpeta necesito rutas absolutas
# path.append('/media/fbonnin/HDD750-Clases/Own/Python-Essentials-2/modules-example/modules')

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))




