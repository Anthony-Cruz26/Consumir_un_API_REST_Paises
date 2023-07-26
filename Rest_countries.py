import requests
import statistics

# Hacer la solicitud a la API para obtener los datos
url = "https://restcountries.com/v3.1/all"
response = requests.get(url)
data = response.json()

# Lista para almacenar la población de cada país
population_list = []

# Variables para almacenar los datos del país con mayor población y área
max_population_country = None
max_area_country = None

# Variables para calcular la población total y media
total_population = 0

# Extraer los datos necesarios para cada país
for country in data:
    name = country["name"]["common"]
    population = country.get("population", 0)
    area = country.get("area", 0)

    # Agregar la población a la lista
    population_list.append(population)

    # Actualizar el país con mayor población y área si es necesario
    if max_population_country is None or population > max_population_country[1]:
        max_population_country = (name, population)

    if max_area_country is None or area > max_area_country[1]:
        max_area_country = (name, area)

    # Actualizar la población total
    total_population += population

# Calcular la media, mediana y moda de la población
mean_population = statistics.mean(population_list)
median_population = statistics.median(population_list)
mode_population = statistics.mode(population_list)

# Imprimir los resultados
print("Nombre del país, Población, Área:")
for country in data:
    name = country["name"]["common"]
    population = country.get("population", 0)
    area = country.get("area", 0)
    print(f"{name}: {population}, {area}")

print("\nPaís con mayor población:")
print(f"{max_population_country[0]} con {max_population_country[1]} habitantes")

print("\nPaís con mayor área:")
print(f"{max_area_country[0]} con {max_area_country[1]} km²")

print("\nPoblación total:", total_population)
print("Media de la población:", mean_population)
print("Mediana de la población:", median_population)
print("Moda Población:", mode_population)