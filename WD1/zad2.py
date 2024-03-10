# Zad 1. Napisz skrypt, który pobiera od użytkownika zdanie i liczy ilość słów. Użyj funkcji input
a = str(input())
print("Liczba slow w podanym slowie", a.count(' ')+1)

"""
Zad 2. Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz obliczenia: ab + c.
Użyj funkcji readline() i write()).
"""



# Zad3. Napisz skrypt, który sprawdzi czy wczytany napis jest palindromem.
# TODO do funkcji
string = "kajak kajak kajak"
string_as_list = list(string)
string_as_list.reverse()
if string_as_list == list(string):
    print("palidrom")
else:
    print("nie palidrom")
"""
Zad4. Napisz skrypt, który sprawdzi czy wczytana liczba jest pierwsza.
Zad5. Napisz skrypt, który sprawdzi ile jest liczb doskonałych do liczby 1000.
Zad 6. Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float. 
Następnie za pomocą użycia pętli for podnieś każdą liczbę do kwadratu.
Zad 7. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb, 
następnie dodaje do listy tylko parzyste liczby.
"""

"""
Zad 8. Napisz skrypt, w którym utworzysz listę z elementami dowolnego typu. 
Utwórz słownik, gdzie klucze będą poszczególnymi elementami z listy, 
a wartość to ilość wystąpień klucza w liście. Następnie usuń wszystkie elementy ze słownika, które nie będą liczbami.
"""
list_tmp = ("aa", 1, 1.643, "tst", "tst", 1, 3, -4, 1, 1.543, -123.12, 1, 1.43, "a")
dictionary = {}
for i in range(0, len(list_tmp)):
    dictionary[list_tmp[i]] = list_tmp[i]
    dictionary[list_tmp[i]] = list_tmp.count(list_tmp[i])
# print(dictionary)
keys_to_remove = []
for i in dictionary:
    if type(i) is str:
        keys_to_remove.append(i)
for i in keys_to_remove:
    del dictionary[i]
# print(dictionary)
