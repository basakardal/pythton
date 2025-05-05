liste=[10,11,12,13,14,15,16,17,18,19,20]
liste2=[21,22,23,24,25]
birlesik_liste=liste+liste2
for liste in birlesik_liste:
    if liste %4==0:
        print(liste)