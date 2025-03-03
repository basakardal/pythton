bagaj=int (input("toplam bagaji girin: "))
if bagaj<=20:
     print ("herhangi bir ücret ödemeniz gerekmiyor" )
else:
     fark=bagaj-20
     print("fazla bagaj için",10*fark,"TL ödemelisiniz")
print("iyi yolculuklar")