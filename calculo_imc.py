print(" 😄😄​​​Seja bem vindo 😄😄  ")
print(" 🏃‍♂️‍➡️🏃‍♂️‍➡️ ​​​Esse programa soma seu IMC 🏃‍♂️‍➡️🏃‍♂️‍➡️ ")
nome = (input("Insira a seu nome: "))
peso=float(input("Insira o seu peso em kg: "))
altura=float(input("Coloque sua altura: "))
imc =peso / (altura*altura)
print(f"Seu IMC e de:{imc} ")
if imc< 18.5:
    print(f"Sua classificação esta abaixo do peso! ☺️ {imc:.2f} ")    
elif imc >=18.5 and imc<=24.9:
    print(f"a classificação do seu imc e normal! 😐  {imc:.2f} ")
elif imc >=25.0 and imc<=29.9:
    print(f"a classificação do seu imc e Sobrepeso! 🥵 {imc:.2f} ")
else:
    print(f"Obesidade!😡 {imc}")