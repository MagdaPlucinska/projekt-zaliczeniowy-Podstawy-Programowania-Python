import menu
lista_pasazerow=[]
menu=menu.Menu()

while True:
    try:
        wybor=int(input('Podaj komunikat: 1 - Dodaj nowy plik; 2-Wysiwetl dane; 3-Narysuj histogram; 4- Wyswietl podstawowe inoformacjie o danych; 5-Zamknij program'))
        if wybor==1:
            menu.Wczytajplik(lista_pasazerow)
            """
            funkcja przyjmuje sciezke do pliku, zapisuje i aktualizuje zebrane dane
            """
        if wybor==2:
            menu.WyswietlDane(lista_pasazerow)
            """
            funkcja wysiwetla wybrane charakterystyki
            """
        if wybor==3:
            menu.Histogram(lista_pasazerow)
            """
            funkcja wyswietla histogram dla wybranych danych
            """
        if wybor==4:
            menu.Analizadanych(lista_pasazerow)
            """
            funkcja wyswietla podstawowe inofmracje o wybraych danych 
            """
        if wybor==5:
            break
    except:
        print("Nie ma takiej operacji")
