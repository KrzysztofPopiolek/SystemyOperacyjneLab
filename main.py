# kalkulator.py

def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    if y != 0:
        return x / y
    else:
        return "Błąd! Nie można dzielić przez zero."

print("Prosty kalkulator w języku Python")

while True:
    print("\nWybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("0. Wyjście")

    wybor = input("Podaj numer operacji (0-4): ")

    if wybor == "0":
        print("Dziękujemy za skorzystanie z kalkulatora. Do widzenia!")
        break
    elif wybor in ("1", "2", "3", "4"):
        liczba1 = float(input("Podaj pierwszą liczbę: "))
        liczba2 = float(input("Podaj drugą liczbę: "))

        if wybor == "1":
            wynik = dodawanie(liczba1, liczba2)
            print(f"Wynik dodawania: {wynik}")
        elif wybor == "2":
            wynik = odejmowanie(liczba1, liczba2)
            print(f"Wynik odejmowania: {wynik}")
        elif wybor == "3":
            wynik = mnozenie(liczba1, liczba2)
            print(f"Wynik mnożenia: {wynik}")
        elif wybor == "4":
            wynik = dzielenie(liczba1, liczba2)
            print(f"Wynik dzielenia: {wynik}")
    else:
        print("Błędny wybór. Wybierz liczbę od 0 do 4.")
