# import sys

# komentowanie / odkomentowanie ctrl + /
# nazwy zmiennych rozdzielamy podloga - przyjete tak jest w libach, camelCase działą
# skrot do reformatowania ctrl + alt + L
# odswiezyc sobie vima
a = 56
print(a)
print(type(a))
b = 5.5
print(b)
print(type(b))
zmienna_tekstowa = "wizualizacja danych"
print(zmienna_tekstowa)
print(type(zmienna_tekstowa))
b = 2
g = b ** 2
print(g)
h = pow(b, 2)
print(h)
i = 6 ** (1 / 2)
j = pow(6, 1 / 2)
print(i)
print(j)
print("liczba a jest rowna {:d}, liczba b jest rowna {:d}".format(a, b))
# a = input("Wprowadz liczbe: ")
# print(a)
# print(type(a))  # input z marszu castuje do stringow
# print(a * 5)
#
# a = int(a)
# print(type(a))
# print(a * 5)
#
# sys.stdout.write("Wprowadz liczbe b: ")
# b = sys.stdin.readline()
# print(b)
# print(type(b))

lista = [5, 6.6, 34, 'a', 'b', [2, 3, 4], 'ab']
print(lista)
lista.append(67)
print(lista)
lista.insert(2, 'c')
print(lista)
lista.extend([20, 21, 22])
print(lista)
lista.pop()
print(lista)
lista.pop(2)
print(lista)
lista.remove([2, 3, 4])
del lista[1]
print(lista)
lista.reverse()
print(lista)
# lista.sort() sort tylko kiedy w liscie sa same wartosci ktore mozemy posortowac/przyrownac

slownik = {"klucz": "wartosc", 1: 2, 'a': 5, 4: 'b'}
print(slownik)
print(slownik[4])
slownik[6] = 45
print(slownik)
slownik.pop(1)  # usuwa element z kluczem 1
print(slownik)
print(slownik.keys())
print(slownik.values())
del slownik[6]

a = 6
b = 7

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is greater than b")

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# if (a > b) & (c > d):
#     print(a, c)
# else:
#     print(b, d)

for i in range(8):
    print(i)
else:
    print('koniec petli')

for i in range(2, 8, 2):
    print(i)
else:
    print('koniec petli')

for i in lista:
    print(i)

for i in range(0, 5):
    for j in range(0, 5):
        result = i + j
        print(result)
    print(' ')

licznik = 0
while licznik < len(lista):
    print(lista[licznik])
    licznik += 1
else:
    print("koniec whila")

licznik = 0
while licznik != 10:
    if licznik == 7:
        print(licznik)
        break
    else:
        licznik += 1
else:
    print('licznik')

# stworzyc liste z liczbami,
# wczytac z inputa wartosc,
# przeleciec po liscie do konca i sprawdzicz czy a-item=0,
# jesli tak to wylistować

new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("podaj wartosc A do zprawdzenia")
a = int(input("podaj wartosc A do zprawdzenia"))
licznik = 0
while licznik < len(new_list):
    if a - new_list[licznik] == 0:
        print("wartosc ", new_list[licznik], " odjeta od ", a, " wynosi zero")
    licznik += 1
print("koniec petli")
