# Programa conversor de temperatura

print(".................................")
print("...VALOR EN GRADOS CENTIGRADOS...")
print(".................................")

# input

c = int(input("Digite el valor en grados centigrados: "))

#processing
f =(c+273.15)
k =(c*1.8+32)

#output
print(".................................")
print("...........RESULTADOS............")
print(".................................")

print("resultado grados farenheit " + str(f))
print("resultado grados kelvin " + str(k))

