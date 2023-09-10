import matplotlib.pyplot as plt

def main():
    print("Bienvenido al Laboratorio de Suma Acumulativa")

    cantidad_numeros = int(input("Ingrese la cantidad de números a sumar: "))
    numeros = [float(input(f"Ingrese el número {i + 1}: ")) for i in range(cantidad_numeros)]
    suma_acumulativa = [sum(numeros[:i + 1]) for i in range(cantidad_numeros)]

    print("Suma acumulativa:")
    [print(f"Para el número {i + 1}: {suma}") for i, suma in enumerate(suma_acumulativa)]

    plt.bar(range(1, cantidad_numeros + 1), suma_acumulativa)
    plt.xlabel("Número de entrada")
    plt.ylabel("Suma acumulativa")
    plt.title("Gráfico de Suma Acumulativa")
    plt.show()

if __name__ == "__main__":
    main()