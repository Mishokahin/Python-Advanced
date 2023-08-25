def forecast(*args):
    city_weather = {"Sunny": [],
                    "Cloudy": [],
                    "Rainy": []
                    }
    result = []

    for arg in args:
        city, weather = arg
        city_weather[weather].append(city)

    for w in city_weather:
        for c in sorted(city_weather[w]):
            if len(city_weather[w]) > 0:
                result.append(f"{c} - {w}")

    return "\n".join(result)


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))