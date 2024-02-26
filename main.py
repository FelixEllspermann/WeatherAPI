import requests


def weather_description_from_code(weather_code):
    descriptions = {
        0: "Clear sky",
        1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Fog", 48: "Depositing rime fog",
        51: "Drizzle: Light", 53: "Drizzle: Moderate", 55: "Drizzle: Dense intensity",
        56: "Freezing Drizzle: Light", 57: "Freezing Drizzle: Dense intensity",
        61: "Rain: Slight", 63: "Rain: Moderate", 65: "Rain: Heavy intensity",
        66: "Freezing Rain: Light", 67: "Freezing Rain: Heavy intensity",
        71: "Snow fall: Slight", 73: "Snow fall: Moderate", 75: "Snow fall: Heavy intensity",
        77: "Snow grains",
        80: "Rain showers: Slight", 81: "Rain showers: Moderate", 82: "Rain showers: Violent",
        85: "Snow showers slight", 86: "Snow showers heavy",
        95: "Thunderstorm: Slight or moderate",
        96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail"
    }
    return descriptions.get(weather_code, "Unknown weather code")


def get_weather(latitude, longitude):
    base_url = "https://api.open-meteo.com/v1/forecast"
    query_parameters = {
        'latitude': latitude,
        'longitude': longitude,
        'current_weather': 'true'
    }
    response = requests.get(base_url, params=query_parameters)
    weather_data = response.json()

    if 'current_weather' in weather_data:
        temperature = weather_data['current_weather']['temperature']
        weather_code = weather_data['current_weather']['weathercode']
        description = weather_description_from_code(weather_code)
        print(f"Current Temperature: {temperature}°C, Weather Description: {description}")
    else:
        print("Weather data not found.")


if __name__ == "__main__":
    latitude = input("Enter latitude: ")
    longitude = input("Enter longitude: ")
    get_weather(latitude, longitude)
