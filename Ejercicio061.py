# IMC
# IMC = PESO / (ALTURA**2)

peso = float(input("Ingese peso: "))
altura = float(input("Ingrese altura"))
IMC = peso / altura **2 

if(IMC < 18.5): 
    print("Por debajo")
elif(18.5 <= IMC and IMC <= 24.9): 
    print("Saludable")
elif(25 <= IMC and IMC <= 29.9): 
    print("Sobrepeso")
elif(30 <= IMC and IMC <= 34.9): 
    print("Obesidad 1")
elif(35 <=IMC and IMC <= 39.9): 
    print("Obesidad 2")
else(IMC > 40):
    print("Obesidad 3")
