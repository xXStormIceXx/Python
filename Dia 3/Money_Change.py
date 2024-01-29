def cambio_monedas(n):
    return [10]* ((n//10)) + [5]*((n%10//5)) + [1]*((n*10)%5)
n = int(input())
if n <= 1000 and n > 0:
    respuesta = cambio_monedas(n)
    print(n, respuesta)
