x = [1, 2]

if x == 0:
    x = 1
    print('x был равен нулю')

elif type(x) == type(5) or type(x) == type(5.5):
    print('x допустимое значение')

else:
    print('В x не допустимое значение')
    x = 1

print(100/x)
