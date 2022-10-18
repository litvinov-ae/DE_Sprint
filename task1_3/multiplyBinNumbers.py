x1 = 111
x2 = 101

def is_system(number_one, sec_number):
    count1 = 0
    count2 = 0
    for char in number_one:
        for i in range(len(number_one)):
            if char in "01":  # проверка на принадлежность нужной системе
                count1 += 1
                break
    for char in sec_number:
        for i in range(len(sec_number)):
            if char in "01":  # проверка на принадлежность нужной системе
                count2 += 1
                break
    if count1 == len(number_one) and count2 == len(sec_number):  # все ли цифры прошли проверку
        return True
    else:
        return False
 
 
def bin_mult(number_one, sec_number):
    na, nb = len(a), len(b)
    res = [False] * (na+nb)
    b = [True if d == '1' else False for d in b[::-1]]
    a = [True if d == '1' else False for d in a[::-1]]
    
    for i in range(nb):
        if b[i]:
            t = False
            for j in range(na):
                res[i+j], t = res[i+j]^a[j]^t, (res[i+j]+a[j]+t) > 1
            res[i+j+1] = t 
    tmp = ['1' if d else '0' for d in res[::-1]]
    return ''.join(tmp).lstrip('0')
    
 
num1 = '0000110011100000' #input()
num2 = '10011101000000000000' #input()
res_ab = int(num1,2)*int(num2,2)
ab_mul = bin_mult(num1, num2)
print(ab_mul)
print(int(ab_mul,2))
print(res_ab)
 
 
def main():
    number_one = input("Enter your first number in binary system: ")
    sec_number = input("Enter your second number in binary system: ")
    if is_system(number_one, sec_number):
        number_one = str(operation(number_one, sec_number))
        return number_one
    else:
        return "You entered incorrect data"
 
main() 
 
out = 1
while out != 0:
    print(main())
    print("\nDo you want to continue? 1 - yes, 0 - no\n")
    out = int(input())