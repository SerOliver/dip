

def ucitaj_csv():
    f = open("primer.csv","r", encoding="utf8")
    mList = []
    for line in f:
        try:
            parts = line.split(';')
            kolona0 = float(parts[0])
            kolona1 = float(parts[1])
            print(kolona0, kolona1)
        except Exception as e:
            print(e) 
            pass
    return mList

def izracunaj_preporuku(param1, param2, param3):
    print("param1: {}".format(param1))
    print("param2: {}".format(param2))
    print("param3: {}".format(param3))
    ucitaj_csv()
    promenjiva = param2 + param3
    return promenjiva, 'nesto'
