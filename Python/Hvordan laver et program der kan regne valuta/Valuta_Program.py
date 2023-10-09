
Kurs = 0.14 


print("euro to DKK")
print("how much")
DKK = input()
DKK = float(DKK)
euro = Kurs * DKK

fee = euro/100*2

euroout = euro-fee


print(str(euroout))




