x = input()

def is_palindrome(text):
    text = x.lower().replace(' ','')
    if text == text[::-1]:
        return True
    else:
        return False

print("Ввод: x = " + x)
print("Вывод: " + is_palindrome(x))