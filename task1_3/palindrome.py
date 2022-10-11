x = input()
text = x.lower().replace(' ','')

print("Ввод: x = " + x)

if text == text[::-1]:
    print("Вывод: true")
else:
    print("Вывод: false")
    # temp = ''.join(reversed(y))
    # if temp == y:

