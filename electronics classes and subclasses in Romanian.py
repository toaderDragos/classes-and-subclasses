#! python 3
# Proiect final 7 clase Electronice Toader Dragos

dict_consum = {}
dict_pret = {}
lista_producatori = []

print(
    'Obiectele introduse pot apartine urmatoarelor categorii: Electrocasnice_mari, Electrocasnice_mici, Frigider, Aragaz, Mixer, Fier_calcat')


class catalog(object):
    clasa = ['Electrocasnice_mici', 'Electrocasnice_Mari']
    subclasa = {'Fier de calcat': [], 'Frigider': [], 'Mixer': [], 'Aragaz': []}

    def __init__(self, NUME='', pret=0, consum='', producator='', codProdus=0):
        """ Introducem datele de la tastatura, fara parametri de intrare, deoarece devine foarte neclar la subclase"""
        self.NUME = input('Introduceti Numele produsului:\t')
        self.pret = int(input('Introduceti Pretul:\t'))  # il transform in int pt a-l sorta usor
        self.consum = input('Introduceti Consumul:\t')
        self.producator = input('Introduceti producatorul:\t')
        self.codProdus = input('Introduceti codul produsului:\t')
        dict_consum.setdefault(self.consum, self.NUME)  # Introducem cate 2 elemente intr-un dictionar
        dict_pret.setdefault(self.pret, self.NUME)  # Introducem cate 2 elemente intr-un dictionar
        lista_producatori.append((self.producator, self.NUME))  # Introducem cate 2 elemente intr-o lista de tupluri

    def sorteaza_dupa_consum(self):
        """Clasa A este considerata in acest program inaintea lui A+++"""
        dict_consum.setdefault(self.consum, self.NUME)
        return 'Consumul si Numele produsului incepand de la cel mai eficient{}'.format(sorted(dict_consum.items()))

    def cauta_producatori(self):
        """ Dintr-o lista de tupluri cu 2 elemente extragem prin ciclare producatorii doriti"""
        a = input('Ce producator cautati?\t')
        b = 0  # b este o variabila oarecare
        print('De la producatorul ' + a + ' avem obiectele: ')
        for (i, k) in lista_producatori:
            if a.lower() == i.lower():
                print(k)
                b = b + 1  # daca b se schimba atunci acel obiect al producatorului EXISTA pe stoc
        if b == 0:
            print('---  \n(Nu s-a  gasit nici un obiect!)')

    def sorteaza_dupa_pret(self):
        """Introducem intr-un dictionar perechi de Nume si Pret si apoi le sortam"""
        dict_pret.setdefault(self.pret, self.NUME)
        return 'Pretul si Numele produsului incepand de la cel mai ieftin{}'.format(sorted(dict_pret.items()))

    def afiseaza_subclasa(self):
        alege = input('''Introduceti o subclasa pentru a vedea obiectele introduse in ea, dintre urmatoarele:
Frigider, Fier de calcat, Mixer, Aragaz\n''')
        print('Obiectele din clasa ' + alege + ' sunt: ')
        g = catalog.subclasa[alege]
        for elem in g:
            print(elem)


class Electrocasnice_mari(catalog):
    def __init__(self, NUME='', pret=0, consum='', producator='', codProdus=0, adancime=0, latime=0, inaltime=0):
        super().__init__(NUME, pret, consum, producator, codProdus)
        self.adancime = input('Introduceti adancimea:\t')
        self.latime = input('Introduceti latimea:\t')
        self.inaltime = input('Introduceti inaltimea:\t')


class Electrocasnice_mici(catalog):
    def __init__(self, NUME='', pret=0, consum='', producator='', codProdus=0, lungime_cablu=0, baterie=''):
        super().__init__(NUME, pret, consum, producator, codProdus)
        self.lungime_cablu = input('Introduceti lungimea cablului:\t')
        self.baterie = input('Introduceti tipul bateriei:\t')


class Frigider(Electrocasnice_mari):
    def __init__(self, NUME='', pret=0, consum='', producator='', codProdus=0, adancime=0, latime=0, inaltime=0,
                 capacitate_congelator=0, capacitate_frigider=0):
        super().__init__(NUME, pret, consum, producator, codProdus, adancime, latime, inaltime)
        self.capacitate_congelator = input('Introduceti capacitatea congelatorului(litri):\t')
        self.capacitate_frigider = input('Introduceti capacitatea frigiderului(litri):\t')
        catalog.clasa.append('Electrocasnice Mari')
        catalog.subclasa['Frigider'].append(self.NUME)


class Aragaz(Electrocasnice_mari):
    def __init__(self, NUME='', pret=0, consum='', producator='', codProdus=0, adancime=0, latime=0, inaltime=0,
                 nr_arzatoare=0):
        super().__init__(NUME, pret, consum, producator, codProdus, adancime, latime, inaltime)
        self.nr_arzatoare = input('Introduceti numarul de arzatoare:\t')
        catalog.clasa.append('Electrocasnice Mari')
        catalog.subclasa['Aragaz'].append(self.NUME)


class Mixer(Electrocasnice_mici):
    def __init__(self, NUME='', pret=0, consum='', producator='', codProdus=0, lungime_cablu=0, baterie=0,
                 rotatii_min=0):
        super().__init__(NUME, pret, consum, producator, codProdus, lungime_cablu, baterie)
        self.rotatii_min = input('Introduceti numarul de rotatii pe minut:\t')
        catalog.clasa.append('Electrocasnice Mici')
        catalog.subclasa['Mixer'].append(self.NUME)


class Fier_calcat(Electrocasnice_mici):
    def __init__(self, NUME='', pret=0, consum='', producator='', codProdus=0, lungime_cablu=0, baterie='', rezervor=0):
        super().__init__(NUME, pret, consum, producator, codProdus, lungime_cablu, baterie)
        self.rezervor = input('Introduceti capacitatea rezervorului:\t')
        catalog.clasa.append('Electrocasnice Mici')
        catalog.subclasa['Fier de calcat'].append(self.NUME)
