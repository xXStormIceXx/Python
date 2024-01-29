def secuencia_fibonacci(n):
    secuencia = [0, 1]
    for i in range(2, n):
        next_term = secuencia[-1] + secuencia[-2]
        secuencia.append(next_term)
    return secuencia

def main():
    print("¡Bienvenido al generador de la Secuencia de Fibonacci!")
    
    while True:
        try:
            n = int(input("\nIngrese un valor entero positivo para generar la secuencia hasta ese término (o 0 para salir): "))
            
            if n < 0:
                print("Por favor, ingrese un valor entero positivo.")
                continue
            
            if n == 0:
                print("¡Hasta luego! Gracias por usar el generador de la Secuencia de Fibonacci.")
                break
            
            resultado_fibonacci = secuencia_fibonacci(n)
            
            print(f"\nLa Secuencia de Fibonacci hasta el término {n} es: {resultado_fibonacci}")
            
            choice = input("¿Desea generar otra secuencia? (Sí/No): ").lower()
            if choice != 'si' and choice != 's':
                print("¡Hasta luego! Gracias por usar el generador de la Secuencia de Fibonacci.")
                break

        except ValueError:
            print("Por favor, ingrese un valor entero válido.")
            continue

if __name__ == "__main__":
    main()