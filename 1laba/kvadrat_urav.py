print("Введите по очереди значения коэффициентов квадратного уравнения a, b, c:")
a = float(input())
b = float(input())
c = float(input())
disc = b**2 - 4*a*c
if a == 0 and b == 0 and c != 0:
    print('Решения нет')
elif a == 0 and b == 0 and c == 0:
    print('х любое число')
elif a == 0 and b !=0 and c !=0:
    print(-c/b)
elif disc > 0:
    x1 = (-b + disc**0.5) / (2*a)
    x2 = (-b - disc ** 0.5) / (2 * a)
    print('Первый корень:', x1)
    print('Второй корень:', x2)
elif disc == 0:
    x = -b / (2*a)
    print('Единственный корень:', x)
else:
    print('Действительных корней нет.')