precio = input("Ingresa el precio en euros (con dos decimales): ")


euros, centimos = precio.split('.')


print(f"El precio es {euros} euros y {centimos} céntimos.")
