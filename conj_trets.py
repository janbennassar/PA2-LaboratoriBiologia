class ConjuntTrets:
    def __init__(self):
        self.__trets = {}
    
    def afegir(self, tret, i, parell):
        if tret in self.__trets:
            self.__trets[tret][0].interseccio(parell)
            self.__trets[tret][1].add(i)
        else:
            self.__trets[tret] = parell, {i}

    def consulta(self, tret):
        if tret in self.__trets:
            print(' ', tret)
            print(self.__trets[tret][0])
            for i in sorted(self.__trets[tret][1]):
                print(' ', i)
        else:
            print('  error')