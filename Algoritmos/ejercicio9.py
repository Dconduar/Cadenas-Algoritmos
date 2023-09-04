fecha_nacimiento = input("Ingresa tu fecha de nacimiento en formato dd/mm/aaaa: ")


partes = fecha_nacimiento.split('/')


dia = partes[0]
mes = partes[1]
año = partes[2]


print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {año}")
