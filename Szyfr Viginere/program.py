import os

def wczytaj_plik(nazwa_pliku):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, nazwa_pliku)
    
    with open(file_path, 'r') as plik:
        return plik.read().replace(" ", "")

def zapisz_plik(nazwa_pliku, zawartosc):
    with open(nazwa_pliku, 'w', encoding='utf-8') as plik:
        plik.write(zawartosc)

def generuj_klucz(tekst, klucz):
    klucz = list(klucz)
    if len(tekst) == len(klucz):
        return klucz
    else:
        for i in range(len(tekst) - len(klucz)):
            klucz.append(klucz[i % len(klucz)])
    return "".join(klucz)

def szyfruj(tekst, klucz):
    szyfrogram = []
    klucz = generuj_klucz(tekst, klucz)
    for i in range(len(tekst)):
        if tekst[i].isalpha():  # Szyfrujemy tylko litery
            if tekst[i].isupper():
                szyfrogram.append(chr((ord(tekst[i]) + ord(klucz[i]) - 2 * ord('A')) % 26 + ord('A')))
            else:
                szyfrogram.append(chr((ord(tekst[i]) + ord(klucz[i]) - 2 * ord('a')) % 26 + ord('a')))
        else:
            szyfrogram.append(tekst[i])
    return "".join(szyfrogram)

def deszyfruj(szyfrogram, klucz):
    odszyfrowany = []
    klucz = generuj_klucz(szyfrogram, klucz)
    for i in range(len(szyfrogram)):
        if szyfrogram[i].isalpha():  # Deszyfrujemy tylko litery
            if szyfrogram[i].isupper():
                odszyfrowany.append(chr((ord(szyfrogram[i]) - ord(klucz[i]) + 26) % 26 + ord('A')))
            else:
                odszyfrowany.append(chr((ord(szyfrogram[i]) - ord(klucz[i]) + 26) % 26 + ord('a')))
        else:
            odszyfrowany.append(szyfrogram[i])
    return "".join(odszyfrowany)

# Główna część programu
if __name__ == "__main__":
    tekst = wczytaj_plik('tekst.txt')
    klucz = wczytaj_plik('klucz.txt')

    zaszyfrowany_tekst = szyfruj(tekst, klucz)
    zapisz_plik('zaszyfrowany_tekst.txt', zaszyfrowany_tekst)
    print(f"Zaszyfrowany tekst: {zaszyfrowany_tekst}")

    odszyfrowany_tekst = deszyfruj(zaszyfrowany_tekst, klucz)
    zapisz_plik('odszyfrowany_tekst.txt', odszyfrowany_tekst)
    print(f"Odszyfrowany tekst: {odszyfrowany_tekst}")
