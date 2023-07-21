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


url = 'https://restcountries.com/v3.1/independent?status=true&fields=translations,capital,currencies,idd'

Listar_nombre_paises(url)



