class NarzedziaTekstowe():
    @staticmethod
    def policzSamogloski(tekst):
        liczbaSamoglosek = 0
        samogloski = "aeuioąęóyAĄEĘYUIOÓ"
        if tekst == None:
            return liczbaSamoglosek
        for litera in tekst:
            if litera in samogloski:
                liczbaSamoglosek += 1
        return liczbaSamoglosek

    @staticmethod
    def usunPowtorzenia (tekst):
        tekstBezPowtorzen =""
        if len(tekst)<1:
            return tekstBezPowtorzen
        tekstBezPowtorzen = tekst[0]
        for i in range(1,len(tekst)):
            if tekst[i]!= tekst[i-1]:
                tekstBezPowtorzen = tekstBezPowtorzen + tekst[i]
        return tekstBezPowtorzen

tekstDoTestowania = input("Podaj tekst")
print("Liczba samoglosek "+str(NarzedziaTekstowe.policzSamogloski(tekstDoTestowania)))
print("tekst bez powtorzen "+ NarzedziaTekstowe.usunPowtorzenia(tekstDoTestowania))
print("tekst bez powtorzen "+ NarzedziaTekstowe.usunPowtorzenia(""))