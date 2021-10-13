# Programa para calcular o fatorial de um número natural positivo


def main():
    numeros = []
    resultado = 1
    numero = int(input("Insere um número natural positivo: "))
    if numero < 0:
        print("Tens de inserir um número natural POSITIVO!")
        main()

    # 4! = 4*3*2*1

    for i in range(1, numero + 1):
        # Primeiro adicionamos o número dado até ao 1
        numeros.append(i) 

        # Depois, como o for loop está a iterar todos os números entre 1 e o número dado, conseguimos multiplicar o número anterior pelo seguinte
        resultado = resultado * len(numeros)
    print(resultado)
    main()

main()