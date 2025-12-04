from individu import Individu

class ConjuntIndividus:
    def __init__(self, preordre, parells):
        self.__individus = [None] + [Individu(s) for s in parells]
        self.__arbre = self.__Arbre(preordre)
    
    def afegir(self, tret, i):
        if self.__individus[i].te(tret):
            print('  error')
        return self.__individus[i].afegir(tret)

    def consulta(self, i):
        if i < len(self.__individus):
            print(self.__individus[i])
        else:
            print('  error')
            
    def distribucio(self, tret):
        d = self.__arbre.distribucio(tret, self.__individus)
        if d:
            print(' ', *d)
        else:
            print('  error')
    
    class __Arbre:
        def __init__(self, preordre):
            assert preordre
            self.__root = preordre.pop(0)
            if self.__root != 0:
                self.__left = __class__(preordre)
                self.__right = __class__(preordre)

        def distribucio(self, tret, individus):
            if self.__root != 0:
                left = self.__left.distribucio(tret, individus)
                right = self.__right.distribucio(tret, individus)
                if individus[self.__root].te(tret):
                    n = [self.__root]
                elif left or right:
                    n = [-self.__root]
                else:
                    n = []
                return left + n + right
            else:
                return []