from turtle import Turtle

seta = Turtle()
seta.speed(1)

print("Tente fazer um quadrado")

while True:
    # Aqui é feito o motimento de direção
    direcao = input("Em qual direção deseja ir? f=frente | t=tras :")
    pixels = int(input("Quantos pixels deseja andar? :"))
    if direcao == "f":
        seta.forward(pixels)
    elif direcao == "t":
        seta.backward(pixels)

    # Aqui é feito o movimento de rotaçãao
    rotacao = input("Rotação da seta , e=esquerda | d=direita :")
    pixels = int(input("Quantos pixels deseja girar? :"))
    if rotacao == "e":
        seta.left(pixels)
    elif rotacao == "t":
        seta.right(pixels)

    continuar = input("Desenha continuar ?")
    if continuar == "S" or "s" or "sim" or "SIM" or "\n":
        continue
    else:
        break
