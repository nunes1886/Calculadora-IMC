#Calculator IMC
print("IMC calculator")

print("")

peso = float(input("Seu peso aqui: "))

print("")

altura = float(input("Sua altura aqui: "))

print("")

imc = peso / altura **2

print("Your IMC: %.2f" % imc)

print("")

if imc < 18.5:
  print("Baixo peso")
  
if imc == 18.6 or 24.9:
  print("Peso normal")
  
  if imc == 25:
    print("Sobrepeso")