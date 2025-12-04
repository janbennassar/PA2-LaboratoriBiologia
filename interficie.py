from pytokr import make_tokr
from conj_individus import ConjuntIndividus
from conj_trets import ConjuntTrets

with open(0) as file:
    _, f_item = make_tokr(file)
    while True:
        token = f_item()
        if token == 'experiment':
            n = int(f_item())
            m = int(f_item())
            print(token, n, m)
            preordre = [int(f_item()) for _ in range(n*2+1)]
            parells = [f_item() for _ in range(n)]
            conj_individus = ConjuntIndividus(preordre, parells)
            conj_trets = ConjuntTrets()

        elif token == 'afegir_tret':
            tret = f_item()
            i = int(f_item())
            print(token, tret, i)
            parell = conj_individus.afegir(tret, i)
            conj_trets.afegir(tret, i, parell)

        elif token == 'consulta_tret':
            tret = f_item()
            print(token, tret)
            conj_trets.consulta(tret)

        elif token == 'consulta_individu':
            i = int(f_item())
            print(token, i)
            conj_individus.consulta(i)

        elif token == 'distribucio_tret':
            tret = f_item()
            print(token, tret)
            conj_individus.distribucio(tret)

        elif token == 'fi':
            print(token)
            quit()
