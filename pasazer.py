class Pasazer:
    def __init__(self,PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked):
        self.PassengerId=PassengerId
        self.Survived=Survived
        self.Pclass=Pclass
        self.Name=Name
        self.Sex=Sex
        self.Age=Age
        self.SibSp=SibSp
        self.Parch=Parch
        self.Ticket=Ticket
        self.Fare=Fare
        self.Cabin=Cabin
        self.Embarked=Embarked

    def Pobierz(self,lista):
        """
        funkcja zwraca informacje zwraca dane zawarte w konstrukturze klasy pasazer
        """
        dane = ''
        for item in range (0,len(lista)):
            if lista[item]=='PassengerId':
                if dane != '':
                    dane=dane+','
                dane = dane + self.PassengerId
            elif lista[item]=='Survived':
                if dane != '':
                    dane=dane+','
                dane = dane + self.Survived
            elif lista[item]=='Pclass':
                if dane != '':
                    dane=dane+','
                dane = dane + self.Pclass
            elif lista[item]=='Name':
                if dane != '':
                    dane=dane+','
                dane = dane + self.Name
            elif lista[item]=='Sex':
                if dane != '':
                    dane=dane+','
                dane = dane + self.Sex
            elif lista[item]=='Age':
                if dane != '':
                    dane=dane+','
                dane = dane + self.Age
            elif lista[item]=='SibSp':
                if dane != '':
                    dane=dane+','
                dane = dane + self.SibSp
            elif lista[item]=='Parch':
                if dane != '':
                    dane=dane+','
                dane = dane + self.Parch
            elif lista[item]=='Ticket':
                if dane != '':
                    dane=dane+','
                dane = dane + self.Ticket
            elif lista[item]=='Fare':
                if dane != '':
                    dane=dane+','
                dane = dane + self.Fare
            elif lista[item]=='Cabin':
                if dane != '':
                    dane=dane+','
                dane = dane + self.Cabin
            elif lista[item]=='Embarked':
                if dane != '':
                    dane=dane+','
                dane = dane + self.Embarked
            else:
                print(f"Nie znaleziono cechy {lista[item]}. Podaj prawidlowa nazwe bez znaku spacji.")
        return dane

    def Wyswietl(self, lista):
        """
        funkcja wyswietla elementy listy
        """
        print(self.Pobierz(lista))

    def GetId(self):
        """
        funkcja dodaje nowego pasażera
        """
        return self.PassengerId

    def Aktualizacjadanych(self,PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked):
        """
        funckja sprawdza czy dany pasazer juz istnieje - jezeli nie to dodaje/aktualizuje dane
        """
        if self.PassengerId=='':
            self.PassengerId=PassengerId
        elif self.Survived=='':
            self.Survived=Survived
        elif self.Pclass=='':
            self.Pclass=Pclass
        elif self.Name=='':
            self.Name=Name
        elif self.Sex=='':
            self.Sex=Sex
        elif self.Age=='':
            self.Age=Age
        elif self.SibSp=='':
            self.SibSp=SibSp
        elif self.Parch=='':
            self.Parch=Parch
        elif self.Ticket=='':
            self.Ticket=Ticket
        elif self.Fare=='':
            self.Fare=Fare
        elif self.Cabin=='':
            self.Cabin=Cabin
        elif self.Embarked=='':
            self.Embarked=Embarked





