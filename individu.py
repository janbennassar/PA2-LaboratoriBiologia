from parell_cromosomes import ParellCromosomes

class Individu:
    def __init__(self, s):
        self.__parell = ParellCromosomes(s)
        self.__trets = set()

    def afegir(self, tret):
        self.__trets.add(tret)
        return self.__parell

    def te(self, tret):
        return tret in self.__trets

    def __str__(self):
        
        s = str(self.__parell)
        for tret in sorted(self.__trets):
            s += '\n  ' + tret
        return s