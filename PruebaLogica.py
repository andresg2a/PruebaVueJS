def buscar_limites(lista_numeros, numero):
    menor = 'X'
    mayor = 'X'
    
    for num in lista_numeros:
        if num < numero:
            menor = num
        elif num > numero and mayor == 'X':
            mayor = num
            break
    return menor, mayor

def main():
    # Entrada de la cantidad de números en la lista
    n = int(input())
    
    # Entrada de la lista de números (ya ordenada de menor a mayor)
    lista_numeros = list(map(int, input().split()))
    
    # Entrada de la cantidad de consultas
    q = int(input())
    
    # Entrada de los números a consultar
    consultas = list(map(int, input().split()))
    
    # Procesamiento y salida de los resultados
    for consulta in consultas:
        menor, mayor = buscar_limites(lista_numeros, consulta)
        print(f"{menor} {mayor}")

# Llamada al main para ejecutar el programa
if __name__ == "__main__":
    main()
