def record_temperatures(city_temps, city, temperatures):
    """
    Almacena las temperaturas semanales para una ciudad dada.
    `city_temps` es un diccionario donde la clave es la ciudad y el valor es una lista de temperaturas.
    """
    city_temps[city] = temperatures
    print(f"Temperaturas para {city} registradas: {temperatures}")

def find_hottest_and_coldest_week(city_temps):
    """
    Encuentra la temperatura más caliente y la más fría de la semana para cada ciudad.
    """
    results = {}
    for city, temps in city_temps.items():
        if temps:
            hottest = max(temps)
            coldest = min(temps)
            results[city] = {'hottest': hottest, 'coldest': coldest}
        else:
            results[city] = {'hottest': None, 'coldest': None}
    return results

# Demostración
weekly_temperatures = {}

record_temperatures(weekly_temperatures, "Bogotá", [18, 20, 19, 22, 21, 20, 23])
record_temperatures(weekly_temperatures, "Medellín", [25, 27, 26, 28, 27, 29, 28])
record_temperatures(weekly_temperatures, "Cali", [28, 30, 29, 31, 30, 32, 31])
record_temperatures(weekly_temperatures, "Barranquilla", [30, 32, 31, 33, 32, 34, 33])
record_temperatures(weekly_temperatures, "Cartagena", []) # Ciudad sin datos

print("\n--- Análisis de Temperaturas Semanales ---")
analysis_results = find_hottest_and_coldest_week(weekly_temperatures)

for city, data in analysis_results.items():
    if data['hottest'] is not None:
        print(f"Ciudad: {city} - Más Caliente: {data['hottest']}°C, Más Fría: {data['coldest']}°C")
    else:
        print(f"Ciudad: {city} - No hay datos de temperatura.")
