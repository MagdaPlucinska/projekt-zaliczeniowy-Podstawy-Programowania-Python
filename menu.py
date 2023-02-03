import pasazer
import matplotlib.pyplot as plt
import pandas as pd

class Menu:
    def Wczytajplik(self, list):
        """
        funkcja przyjmuje od uzytkownika i zapisuje do listy dane z pliku csv
        """
        try:
            a = input("podaj sciezke do pliku:")
            path = open(f"{a}","r")
            PassengerId= ''
            Survived= ''
            Pclass = ''
            Name = ''
            Sex = ''
            Age = ''
            SibSp = ''
            Parch = ''
            Ticket = ''
            Fare = ''
            Cabin = ''
            Embarked = ''
            a = path.readline()
            b = a.split(',')
            lista_kolumn = []
            for i in range(0, len(b)):
                lista_kolumn.append(b[i])
            c = path.readline()

            while c!='':
                d = c.replace(", "," ",1)
                lista_wierszy = d.split(',')
                for i in range(0, len(lista_kolumn)):
                    if lista_kolumn[i] == 'PassengerId':
                        PassengerId = lista_wierszy[i]
                    elif lista_kolumn[i] == 'Survived':
                        Survived = lista_wierszy[i]
                    elif lista_kolumn[i] == 'Pclass':
                        Pclass = lista_wierszy[i]
                    elif lista_kolumn[i] == 'Name':
                        Name = lista_wierszy[i]
                    elif lista_kolumn[i] == 'Sex':
                        Sex = lista_wierszy[i]
                    elif lista_kolumn[i] == 'Age':
                        Age = lista_wierszy[i]
                    elif lista_kolumn[i] == 'SibSp':
                        SibSp = lista_wierszy[i]
                    elif lista_kolumn[i] == 'Parch':
                        Parch = lista_wierszy[i]
                    elif lista_kolumn[i] == 'Ticket':
                        Ticket = lista_wierszy[i]
                    elif lista_kolumn[i] == 'Fare':
                        Fare = lista_wierszy[i]
                    elif lista_kolumn[i] == 'Cabin':
                        Cabin = lista_wierszy[i]
                    elif lista_kolumn[i] == 'Embarked':
                        Embarked = lista_wierszy[i]

                obiekt1 = pasazer.Pasazer(PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked)
                flag=0
                for i in list:
                    if PassengerId==i.GetId():
                        flag=1
                        i.Aktualizacjadanych(PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked)
                if flag==0:
                    list.append(obiekt1)
                c = path.readline()
        except:
            print("Blad - podaj sciezke do pliku bez znakow '' ")

    def WyswietlDane(self, lista):
        """
        funkcja wyswietla wybrane dane
        """
        listauzytkownika = []
        print("Kolumny do wyboru to: PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked")
        a = input('Podaj kolumny do wyświetlenia: ')
        b=a.split(',')
        for i in range(0, len(b)):
            listauzytkownika.append(b[i])
        for i in lista:
            i.Wyswietl(listauzytkownika)

    def Pobierzdane(self,lista,a):
        """
        funkcja zwarca liste, w ktorej jednym elementem jest jeden pasazer
        """
        print(len(lista))
        listauzytkownika = []
        listadf=[]
        b=a.split(',')
        for i in range(0, len(b)):
            listauzytkownika.append(b[i])
        for i in lista:
            listadf.append(i.Pobierz(listauzytkownika))
        return listadf

    def Histogram(self,lista):
        """
        funkcja rysuje hisogram dla wybranych danych
        """
        print("kolumny do wyboru to: PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked")
        a = input('podaj jakie dane chcesz wyswietlic: ')
        while True:
            if a=="PassengerId":
                print("nie można wyswietlic histogramu dla PassengerId")
                break
            if a=="Name":
                print("nie można wyswietlic histogramu dla Name")
                break
            if a=="Ticket":
                print("nie można wyswietlic histogramu dla Ticket")
                break
            if a=="Cabin":
                print("nie można wyswietlic histogramu dla Ticket")
                break
            dane = self.Pobierzdane(lista, a)
            df=pd.DataFrame(dane)
            plt.hist(df,bins=10)
            plt.show()
            break

    def Analizadanych(self,lista):
        """
        funkcja wyswietla podstawowe dane dotyczace wybranej kolumny
        """
        print("kolumny do wyboru to: PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked")
        a = input('podaj dla jakiej kolumny chcesz wyswietlic podstawowe informacje: ')
        while True:
            if a == "PassengerId":
                print("nie można wyswietlic histogramu dla PassengerId")
                break
            if a == "Name":
                print("nie można wyswietlic histogramu dla Name")
                break
            if a == "Ticket":
                print("nie można wyswietlic histogramu dla Ticket")
                break
            if a == "Cabin":
                print("nie można wyswietlic histogramu dla Ticket")
                break
        dane = self.Pobierzdane(lista, a)
        df = pd.DataFrame(dane)
        print(df.describe())
        print(df.min())
        print(df.mean())








