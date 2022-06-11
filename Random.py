import random

print('Рандомайзер')
print()

connect = True

while connect == True:
    a = input('От: ')
    print()
    b = input('До: ')
    print()

    finish = random.randint(int(a), int(b))

    print('Ответ: ',)

input()
