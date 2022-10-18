import roman

x = int(input('> '))
print("Ввод: x = " + str(x))
def checkInputNum(num):
    return num > 0 and num <= 2000
    
if checkInputNum(x):
    print("Вывод: " + roman.toRoman(x))
else:
    print("Введеное число вне допустимого диапазона")    