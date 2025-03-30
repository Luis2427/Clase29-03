'''
Objetivo: En la Universidad "Del Futuro", se necesita un programa
          con las siguientes caracterisicas.
Ingresos
	Deberá ingresar un monto
Descuentos
	Deberá ingresar un monto
Neto a pagar
	Deberá calcular la Suma Total de Ingresos - Total de Descuentos

Se debe ingresar la cantidad de días NO laborados
'''
# ENTRADA
ingreso = float(input("Digite el ingreso: ")) # 1000
diasNoLaborados = int(input("Digite el cantidad de días NO laborados: ")) # 2
descuentoRentaQuinta = int(input("Digite el dcto de renta de quinta: ")) # 2
TipoAFP = str(input("Ingerese la AFP HABITAT(HA) / INTEGRA(IN) / PRIMA(PI) / PROFUTURO(PO): "))

#PROCESO
#########AFP10
AFP10 = ingreso*10/100
#########AFPcomision
if(TipoAFP == "HA"): 
    comisionSobreFlujo = 1.47
elif(TipoAFP == "IN"): 
    comisionSobreFlujo = 1.55
elif(TipoAFP == "PI"): 
    comisionSobreFlujo = 1.60
else: 
    comisionSobreFlujo = 1.69

AFPcomision = ingreso*comisionSobreFlujo*10/100
#########AFPprima
AFPprima = ingreso*1.37*10/100


pagoPorDia = ingreso / 30
diaLaborado = 30-diasNoLaborados
netoPagar = (pagoPorDia * diaLaborado) - descuentoRentaQuinta - (AFP10 + AFPcomision + AFPprima)

#SALIDA
#
print("AFP 10%: ",AFP10)
print("AFP Comisión",AFPcomision)
print("AFP Prima",AFPprima)

print("El Neto a pagar es: ",netoPagar)