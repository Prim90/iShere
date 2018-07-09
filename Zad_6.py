print ("Podaj sześciocyfrową liczbę w systemie dziesiętnym.")

od = "Liczba: "

liczba2 = (input(od))

liczba10 = (int(liczba2[0])*2**1) + (int(liczba2[1])*2**2) + (int(liczba2[2])*2**4) + (int(liczba2[3])*2**8) + (int(liczba2[4])*2**16) + (int(liczba2[5])*2**36)

print(liczba10)

#Czy da radę to urpościć bez pisania równania na 6 indeksów?

