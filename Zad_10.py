print("Sprawdzimy czy wskazany rok jest przestępny.")

od = "Rok: "

rok = int(input(od))

if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0 #Z jakiegoś powodu na końcu tej komunikuje błąd.
    print("Przestępny")
else:
    print("Nieprzestępny")

