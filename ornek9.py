liste=[]
toplam=0
for i in range(5):
    liste.append(int(input("bir sayıyı girin: ")))
for i in range(5):
    toplam=toplam+liste[i]
print("toplam: ",toplam)