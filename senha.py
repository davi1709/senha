from random import randint,choice
def gerarsenha(tamanho):
    letras = "abcdefghijklmnopqrstuvwxyz"
    especiais = "!@#$%¨&*()+_-"
    numeros = "0123456789"
    for i in range(tamanho):
        aleatorio = choice(letras + numeros + especiais)
        print(aleatorio, end="")


gerarsenha(int(input("Digite o número de caractéres que sua senha deve ter: ")))