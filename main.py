import random
import time
import sys
 
sys.setrecursionlimit(10000)
 
def generar_datos(n=20, minimo=1, maximo=100):
    """Genera una lista de n enteros aleatorios entre minimo y maximo."""
    return [random.randint(minimo, maximo) for _ in range(n)]
 
# Parte VI. Quick Sort
def quick_sort(datos, pivote_tipo="ultimo", mostrar_traza=False, nivel=0):
    lista = datos.copy()
 
    # Caso base: una lista vacía o de un solo elemento ya está ordenada
    if len(lista) <= 1:
        return lista
 
    # Selección del pivote 
    if pivote_tipo == "ultimo":
        pivote = lista[-1]
        resto = lista[:-1]
    elif pivote_tipo == "primero":
        pivote = lista[0]
        resto = lista[1:]
    elif pivote_tipo == "centro":
        centro = len(lista) // 2
        pivote = lista[centro]
        resto = lista[:centro] + lista[centro + 1:]
    else:
        raise ValueError("pivote_tipo debe ser 'ultimo', 'primero' o 'centro'")
 
    # Separar menores y mayores respecto al pivote 
    menores = [x for x in resto if x <= pivote]
    mayores = [x for x in resto if x > pivote]
 
    if mostrar_traza:
        sangria = "  " * nivel
        print(f"{sangria}Pivote: {pivote}")
        print(f"{sangria}Menores: {menores}")
        print(f"{sangria}Mayores: {mayores}")
        print()
 
    # Llamadas recursivas y combinación del resultado 
    izquierda_ordenada = quick_sort(menores, pivote_tipo, mostrar_traza, nivel + 1)
    derecha_ordenada = quick_sort(mayores, pivote_tipo, mostrar_traza, nivel + 1)
 
    return izquierda_ordenada + [pivote] + derecha_ordenada
 
 

# Parte VIII. Comparación experimental (tiempos de ejecución)
def medir_tiempo_quicksort(n):
    datos = [random.randint(1, 1_000_000) for _ in range(n)]
    inicio = time.perf_counter()

    quick_sort(datos)
    fin = time.perf_counter()

    return fin - inicio
 
 
def experimento_tiempos(tamanos=(100, 500, 1000, 5000)):
    resultados = {}
    for n in tamanos:
        resultados[n] = medir_tiempo_quicksort(n)
    return resultados
 
 
# Parte IX. Diferentes condiciones de entrada
def experimento_condiciones(n=1000):

    # Lista aleatoria
    caso_a = random.sample(range(1, 10000), n)  

    # Lista ya ordenada
    caso_b = list(range(n))        

     # Lista ordenada inversa                   
    caso_c = list(range(n, 0, -1))                   
 
    resultados = {}

    for nombre, lista in (("Aleatoria", caso_a),
                           ("Ordenada", caso_b),
                           ("Invertida", caso_c)):
        inicio = time.perf_counter()
        quick_sort(lista)
        fin = time.perf_counter()
        resultados[nombre] = fin - inicio
 
    return resultados
 
# Parte X. Comparación con sort() / sorted() de Python
def comparacion_con_sorted(n=100_000):
    datos = [random.randint(1, 10_000_000) for _ in range(n)]
 
    inicio = time.perf_counter()
    quick_sort(datos)
    tiempo_quicksort = time.perf_counter() - inicio
 
    inicio = time.perf_counter()
    sorted(datos)
    tiempo_sorted = time.perf_counter() - inicio
 
    return tiempo_quicksort, tiempo_sorted
 
def main():
    # Parte I: datos base para todos los algoritmos
    datos = generar_datos(20)
    print("Lista original:")
    print(datos)
    print()
 
    # Parte VI: ordenamiento simple con pivote = último elemento
    print("Lista ordenada con Quick Sort (pivote = último elemento):")
    print(quick_sort(datos))
    print()
 
    # Parte VI: recorrido manual / traza con la lista del enunciado
    lista_manual = [10, 7, 8, 9, 1, 5]
    print("=" * 60)
    print("Traza de Quick Sort (pivote = último elemento)")
    print("Lista:", lista_manual)
    print("=" * 60)
    resultado = quick_sort(lista_manual, pivote_tipo="ultimo", mostrar_traza=True)
    print("Lista ordenada:", resultado)
    print()
 
    print("=" * 60)
    print("Traza de Quick Sort (pivote = primer elemento)")
    print("Lista:", lista_manual)
    print("=" * 60)
    resultado = quick_sort(lista_manual, pivote_tipo="primero", mostrar_traza=True)
    print("Lista ordenada:", resultado)
    print()
 
    print("=" * 60)
    print("Traza de Quick Sort (pivote = elemento central)")
    print("Lista:", lista_manual)
    print("=" * 60)
    resultado = quick_sort(lista_manual, pivote_tipo="centro", mostrar_traza=True)
    print("Lista ordenada:", resultado)
    print()
 
    # Parte VIII: tiempos de ejecución para distintos tamaños
    print("=" * 60)
    print("Parte VIII. Comparación experimental de tiempos (Quick Sort)")
    print("=" * 60)
    tiempos = experimento_tiempos()
    for n, t in tiempos.items():
        print(f"n = {n:>6}  ->  {t:.6f} segundos")
    print()
 
    # Parte IX: comportamiento según condición de entrada
    print("=" * 60)
    print("Parte IX. Comportamiento según condición de entrada (n = 1000)")
    print("=" * 60)
    condiciones = experimento_condiciones()
    for nombre, t in condiciones.items():
        print(f"{nombre:<10} ->  {t:.6f} segundos")
    print()
 
    # Parte X: Quick Sort del estudiante vs sorted() de Python
    print("=" * 60)
    print("Parte X. Quick Sort implementado vs sorted() (n = 100 000)")
    print("=" * 60)
    t_quick, t_sorted = comparacion_con_sorted()
    print(f"Quick Sort (propio): {t_quick:.6f} segundos")
    print(f"sorted() (Python):   {t_sorted:.6f} segundos")
 
 
if __name__ == "__main__":
    main()