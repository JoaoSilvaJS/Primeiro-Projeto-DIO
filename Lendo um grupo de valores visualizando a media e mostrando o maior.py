# Escreva um programa que leia um grupo de valores (não sabemos quantos são) para calcular e visualizar a média desses
# valores e, também, determinar e visualizar o maior deles

contador = soma = media = maior = 0
while True:
    num = int(input('Digite um valor (0 para encerrar): '))
    if num == 0:
        break
    soma += num
    contador += 1
    media = soma / contador
    if contador == 1:
        maior = num
    else:
        if num > maior:
            maior = num
print(f'A soma dos valores é: {soma} \nA média dos valores é {media:.2f}\nE o maior valor digitado foi {maior}')
