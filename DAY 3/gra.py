class kolko_krzyzyk:
    def __init__(self):
        self.gracz = 'x'
        self.plansza = [[' ', ' ', ' '],
                        [' ', ' ', ' '],
                        [' ', ' ', ' ']]
    
    def ruch(self, miejsce):
        ile_w_dol, ile_w_prawo = miejsce
        self.plansza[ile_w_dol][ile_w_prawo] = self.gracz
        if self.wygranko():
            print(f"Gratulacje! Gracz {self.gracz} wygrywa")
            self.pokaz_plansze()
            return

        self.gracz = 'x' if self.gracz == 'o' else 'o'
    
    def wygranko(self):
        for wiersz in self.plansza:
            if all(miejsce == self.gracz for miejsce in wiersz):
                return True
            
        nowa_plansza = self.transpose()

        for wiersz in nowa_plansza:
            if all(miejsce == self.gracz for miejsce in wiersz):
                return True
        
        if all([self.plansza[0][0] == self.gracz, self.plansza[1][1] == self.gracz, self.plansza[2][2] == self.gracz]):
            return True
        
        if all([self.plansza[0][2] == self.gracz, self.plansza[1][1] == self.gracz, self.plansza[2][0] == self.gracz]):
            return True
        return False
    
    def remis(self):
        for wiersz in self.plansza:
            if any(miejsce == ' ' for miejsce in wiersz):
                return False
        if self.wygranko():
            return False
        return True
    
    def transpose(self):
        return [[self.plansza[j][i] for j in range(len(self.plansza))] for i in range(len(self.plansza[0]))]
    
    def pokaz_plansze(self):
        for wiersz in self.plansza:
            print(wiersz)