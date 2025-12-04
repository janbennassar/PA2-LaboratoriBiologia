class ParellCromosomes:
    def __init__(self, s):
        self.__m = len(s)//2
        self.__c1 = [g for g in s[:self.__m]]
        self.__c2 = [g for g in s[self.__m:]]

    def interseccio(self, parell):
        for i in range(self.__m):
            if self.__c1[i] != parell.__c1[i] or self.__c2[i] != parell.__c2[i]:
                self.__c1[i], self.__c2[i] = '--'

    def __str__(self):
        s1, s2 = '', ''
        for g1, g2 in zip(self.__c1, self.__c2):
            s1 += g1
            s2 += g2
        return '  ' + s1 + '\n  ' + s2