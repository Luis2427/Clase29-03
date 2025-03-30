"""
# Elabore un programa, para una organización reguladora ambiental, e ingresar: Monto Base en dólares, Categoría, Ruido en Decibeles, Porcentaje de Penalidad y tipo de cambio a soles; 
para mostrar el Monto Base en soles, el Monto de Penalidad y el Monto a Pagar, ambos en soles
"""

# ENTRADA
monto = int(input("Ingrese monto: "))
Tipocategoria = str(input("Ingese categoria (A) / (B) / (D) / (E): "))

# PORCESO

if(Tipocategoria == "A"): 
   comisionporcategoria = 0.5
elif(Tipocategoria == "B"): 
   comisionporcategoria = 0.07
elif(TIpocategoria == "C"): 
    comisionporcategoria = 0.09
elif(Tipocategoria == "D"): 
   comisionporcategoria = 0.12
elif(Tipocategoria == "E"): 
   comisionporcategoria = 0.15

   TipocategoriaA = monto*comisionporcategoria*10/100
   TipocategoriaB = monto*comisionporcategoria*10/100
   TipocategoriaC = monto*comisionporcategoria*10/100
   TipocategoriaD = monto*comisionporcategoria*10/100
   TipocategoriaE = monto*comisionporcategoria*10/100
comisioncategoria=monto*comisionporcategoria*10/100

cambiosoles= (comisioncategoria*3.64)
# SALIDA
print("La comision es de: ",comisioncategoria)
print("En soles es: ",cambiosoles)
