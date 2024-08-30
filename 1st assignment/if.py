"""massa = float(input("Vazningiz qancha?: "))
keyingisi = input("(K)gs yo (L)bs: ")

if keyingisi.upper() == "K":
    ozgardi = massa / 0.45
    print("Sizning vazningiz: " + str(ozgardi), "Pound ekan")
elif keyingisi.upper() == "L":
    ozgardi = massa * 0.45
    print("Sizning vazningiz: " + str(ozgardi),"Kg ekan")
else:
    print("Notog'ri malumot kiritvordizu brat!")

print("Mayli, sog' bo'lasiz!")

#--------------------------------------------------

harorat = float(input("hozirgi harorat nechada?: "))
unda = input("Celsiusdami C yoki Fahreinheit F?: ")

if unda.upper() == "C":
    ozgartiramiz = (harorat * 9/5) + 32
    print("Harorat " + str(ozgartiramiz), "Fahrenheit ekan")
elif unda.upper() == "F":
    ozgartiramiz = (harorat - 32) * 5/9
    print("Harorat " + str(ozgartiramiz), "Celsius ekan")
else:
    print("Notog'ri malumot kiritvordizu brat!")

#-------------------------------------
summa = float(input("Qancha puliz bor?: "))
valyuta = input("Pul birligini kiriting (USD); (KRW); (RUB); (UZS):")
usd_kurs = 12440
krw_kurs = 11
rub_kurs = 140

if valyuta.upper() == "USD":
     natija = summa / usd_kurs
     print(f"{summa} so'm = {natija} $")
elif valyuta.upper() == "KRW":
     natija = summa / krw_kurs
     print(f"{summa} so'm = {natija} KRW")
elif valyuta.upper() == "RUB":
     natija = summa / rub_kurs
     print(f"{summa} so'm = {natija} RUB")
else:
     print(f"{summa} so'm")"""
#-----------------------------
     
# vazn = float(input("Vazn (kgda) qancha?: "))
# birlik = int(input("tonna (t), gramm (gr), mlgramm (mgr):"))
# tonna = 1000
# gramm = 0.001
# mlgramm = 0.00001
              #birinchi usul - bunisi ishlamadi xatosiniyam uncha tuwunmadim
# if birlik.upper() == "tonna":
#      natija = vazn * tonna
#      print(f"{vazn} kg =", str({natija}), "tonna")
# elif birlik.upper() == "gramm":
#      natija = vazn / gramm
#      print(f"{vazn} kg = {natija} gramm")
# elif birlik.upper() == "mlgramm":
#      natija = vazn / mlgramm
#      print(f"{vazn} kg = {natija} mlgramm")
# else:
#      print(f"{vazn} kg")
                                   #ikkinchi usul

# weight = float(input("Vazn (kgda) qancha?: "))

# birlik = input("tonna (t), gramm (gr), mlgramm (mgr):")


# conversion_factors = {'t': 0.001, 'gr': 1000, 'mgr': 100000}

# if birlik in conversion_factors:
#     converted_weight = weight * conversion_factors[birlik]
#     print(f"{weight} kg teng {converted_weight} {birlik}")
# else:
#     print("Noto'g'ri birlik kiritildi.")

#------------------------------------------------------------

# uzunlik = float(input("O'lchovni (cm)da kiriting: "))

# birlik = input("Qaysi o'lchov birligiga o'tkazish so'ralmoqda? mm; m; km; yd; ft?:")

# turlar = {'mm': 10, 'm': 0.01, 'km': 0.0001, 'yd': 0.010936, 'ft': 0.032808}

# if birlik in turlar:
#     ozgartirilgan_uzunlik = uzunlik * turlar[birlik]
#     print(f"{uzunlik} cm teng {ozgartirilgan_uzunlik} {birlik}")
# else:
#     print("Noto'g'ri birlik kiritildi.")

#----------------------------------------------------------------------

# # bunisi iwlamayabdi 
# ball = float(input("Natijani kiriting (0-100): "))
# baho = "A+, A, B+, B, C+, C, D+, D"

# turlar = {'A+': 90-100,
# 'A': 85-89,
# 'B+': 80-84,
# 'B': 77-79,
# 'C+': 73-76,
# 'C': 70-72,
# 'D+': 67-69,
# 'D': 63-66,
# 'F': 0-62}

# if baho in turlar:
#     print(f"{ball} ball teng {turlar}")
# else:
#     print("Noto'g'ri birlik kiritildi.")

#     #bunisi iktada iwlayabdi - bittada iwlamayabdi 

# ball = float(input("Natijani kiriting (0-100): "))

# baho = {
#     'A+': (90, 100),
#     'A': (85, 89),
#     'B+': (80, 84),
#     'B': (77, 79),
#     'C+': (73, 76),
#     'C': (70, 72),
#     'D+': (67, 69),
#     'D': (63, 66),
#     'F': (0, 62)
# }

# for baho, (lower, upper) in baho.items():
#     if lower <= ball <= upper:
#         print(f"Natija: {ball} ball, baho: {baho}")
#         break
        
# else:
#     print("Noto'g'ri birlik kiritildi.")





