Styczen = 1.592824484
Luty = -0.4535091012
Marzec = 2.324671717
Kwiecien = 1.261254407
Maj = 1.782526286
Czerwiec = 2.329384541
Lipiec = 1.502229842
Sierpien = 1.782526286
Wrzesien = 2.328848994
Pazdziernik = 0.6169213482
Listopad = 2.352295886
Grudzien = 0.3377795452
Styczen_2 = 1.577035247
Luty_2 = -0.2927814426
Marzec_2 = 2.48619659
Kwiecien_2 = 0.2671103178
Maj_2 = 1.417952672
Czerwiec_2 = 1.054243267
Lipiec_2 = 1.480520104
Sierpien_2 = 1.577035247
Wrzesien_2 = -0.07742069031
Pazdziernik_2 = 1.165733399
Listopad_2 = -0.4041867176
Grudzien_2 = 1.499708521

wysokosc_kredytu = float(input("Podaj wysokosc twojego kredytu: "))
oprocentowanie = float(input("Podaj wysokosc stalego oprocentowania kredytu: "))
wysokosc_raty = float(input("Podaj wysokosc stalej raty kredytu: "))

# pozostala_wartosc_kredytu = (1 + ((oprocentowanie+inflacja)/1200)) * wysokosc_kredytu - 200
# print("Twoja pozostała kwota kredytu to {}, to {} mniej niż w poprzednim miesiącu.".format(msc, oprocentowanie))


# 1 + ((inflacja+oprocentowanie)/1200) * wysokosc_kredytu - wysokosc_raty
#inflacja= None
#pozostala_kwota_kredytu: None

szablon = "\nTwoja kwota kredytu po uwzglednieniu inflacji to {} PLN, to {} PLN mniej niz w poprzednim miesiacu!"

#Styczen

inflacja=Styczen
pozostala_kwota_kredytu= (1 + ( (inflacja + oprocentowanie) / 1200)) * wysokosc_kredytu - wysokosc_raty

print(szablon.format(round(pozostala_kwota_kredytu, 2), round(wysokosc_kredytu-pozostala_kwota_kredytu), 2), end=' ')

wysokosc_kredytu=pozostala_kwota_kredytu

#Luty

inflacja=Luty
pozostala_kwota_kredytu= (1 + ( (inflacja + oprocentowanie) / 1200)) * wysokosc_kredytu - wysokosc_raty

print(szablon.format(round(pozostala_kwota_kredytu, 2), round(wysokosc_kredytu-pozostala_kwota_kredytu), 2), end=' ')

wysokosc_kredytu=pozostala_kwota_kredytu

#Marzec

inflacja=Marzec
pozostala_kwota_kredytu= (1 + ( (inflacja + oprocentowanie) / 1200)) * wysokosc_kredytu - wysokosc_raty

print(szablon.format(round(pozostala_kwota_kredytu, 2), round(wysokosc_kredytu-pozostala_kwota_kredytu), 2), end=' ')

wysokosc_kredytu=pozostala_kwota_kredytu

#Kwiecien

inflacja=Kwiecien
pozostala_kwota_kredytu= (1 + ( (inflacja + oprocentowanie) / 1200)) * wysokosc_kredytu - wysokosc_raty

print(szablon.format(round(pozostala_kwota_kredytu, 2), round(wysokosc_kredytu-pozostala_kwota_kredytu), 2), end=' ')

wysokosc_kredytu=pozostala_kwota_kredytu

#Maj

inflacja=Maj
pozostala_kwota_kredytu= (1 + ( (inflacja + oprocentowanie) / 1200)) * wysokosc_kredytu - wysokosc_raty

print(szablon.format(round(pozostala_kwota_kredytu, 2), round(wysokosc_kredytu-pozostala_kwota_kredytu), 2), end=' ')

wysokosc_kredytu=pozostala_kwota_kredytu

#Czerwiec

inflacja=Czerwiec
pozostala_kwota_kredytu= (1 + ( (inflacja + oprocentowanie) / 1200)) * wysokosc_kredytu - wysokosc_raty

print(szablon.format(round(pozostala_kwota_kredytu, 2), round(wysokosc_kredytu-pozostala_kwota_kredytu), 2), end=' ')

wysokosc_kredytu=pozostala_kwota_kredytu

#Lipiec

inflacja=Lipiec
pozostala_kwota_kredytu= (1 + ( (inflacja + oprocentowanie) / 1200)) * wysokosc_kredytu - wysokosc_raty

print(szablon.format(round(pozostala_kwota_kredytu, 2), round(wysokosc_kredytu-pozostala_kwota_kredytu), 2), end=' ')

wysokosc_kredytu=pozostala_kwota_kredytu

#itd.