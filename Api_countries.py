import requests


def Listar_nombre_paises(url):
    paises = requests.get(url)
    paises = paises.json()

    for pais in paises:
        print(f"Nombre Oficial en Español: {pais['translations']['spa']['official']}")
        print(f"La capital es: {pais['capital'][0]}")
        print(f"La moneda es: {pais['currencies']}")

        idd_root = pais.get('idd', {}).get('root', '')
        idd_suffixes = pais.get('idd', {}).get('suffixes', [])

        if idd_root and idd_suffixes:
            idd_full_code = f"{idd_root}{'/'.join(idd_suffixes)}"
            print(f"El código telefónico es: {idd_full_code}")
        elif idd_root:
            print(f"El código telefónico es: {idd_root}")


def obtener_paises(url):
    response = requests.get(url)
    paises = response.json()
    return paises

def pais_de_mayor_poblacion(paises):
    pais_mayor_poblacion = max(paises, key=lambda x: x['population'])
    return pais_mayor_poblacion['translations']['spa']['official'], pais_mayor_poblacion['population']

def pais_de_mayor_area(paises):
    pais_mayor_area = max(paises, key=lambda x: x['area'])
    return pais_mayor_area['translations']['spa']['official'], pais_mayor_area['area']

def poblacion_total(paises):
    poblacion_total = sum(pais['population'] for pais in paises)
    return poblacion_total

def media_poblacion(paises):
    poblaciones = [pais['population'] for pais in paises]
    media = sum(poblaciones) / len(poblaciones)
    return media

def mediana_poblacion(paises):
    poblaciones = [pais['population'] for pais in paises]
    poblaciones_ordenadas = sorted(poblaciones)
    n = len(poblaciones_ordenadas)
    if n % 2 == 0:
        mediana = (poblaciones_ordenadas[n//2 - 1] + poblaciones_ordenadas[n//2]) / 2
    else:
        mediana = poblaciones_ordenadas[n//2]
    return mediana

def moda_poblacion(paises):
    poblaciones = [pais['population'] for pais in paises]
    contador = {}
    for poblacion in poblaciones:
        contador[poblacion] = contador.get(poblacion, 0) + 1
    moda = max(contador, key=contador.get)
    return moda

if __name__ == "__main__":
    url = 'https://restcountries.com/v3.1/independent?status=true&fields=translations,capital,currencies,idd,population,area'
    paises = obtener_paises(url)

    nombre_mayor_poblacion, mayor_poblacion = pais_de_mayor_poblacion(paises)
    nombre_mayor_area, mayor_area = pais_de_mayor_area(paises)
    total_poblacion = poblacion_total(paises)
    media = media_poblacion(paises)
    mediana = mediana_poblacion(paises)
    moda = moda_poblacion(paises)

    print(f"País con mayor población: {nombre_mayor_poblacion} (Población: {mayor_poblacion})")
    print(f"País con mayor área: {nombre_mayor_area} (Área: {mayor_area} km²)")
    print(f"Población total: {total_poblacion}")
    print(f"Media de población: {media}")
    print(f"Mediana de población: {mediana}")
    print(f"Moda de población: {moda}")

url = 'https://restcountries.com/v3.1/independent?status=true&fields=translations,capital,currencies,idd'

Listar_nombre_paises(url)



