"""
Objetivo: En la Universidad "Del Futuro", se necesita un programa
         con las siguientes caracteristicas.
Ingresos
   Debera ingresar un monto 
Descuentos
   Debera ingresar un monto 
Neto a Pagar 
   Debera calcular la suma Total de Ingresos - Total de Descuentos

Se debe ingresar la cantidad de días laborados
"""

ingreso = float(input("Digite el ingreso: ")) # 1000
#descuento5taCategoria = float(input("Digite el descuento: "))
díasNOLaborados = int(input("Digite la cantidad de días NO laborados: ")) #2
descuentoRentaQuinta = int(input("Digite el dcto de renta de quinta")) #2
#PROCESO
pagopordía = ingreso / 30
díaLaborado = 30 - díasNOLaborados
netoPagar = pagopordía * díaLaborado
#SALIDA
print("El Neto a pagar es: ",netoPagar-descuentoRentaQuinta)