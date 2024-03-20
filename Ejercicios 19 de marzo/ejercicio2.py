edad = 16
tiene_licencia = False

if edad >= 18:
    if tiene_licencia:
        print("Puedes conducir")
    else:
        print("No puedes conducir, ecesitas contar con una licencia")
else:
    print("No puedes conducir aún, no tienes 18 años y debes tener una licencia")
