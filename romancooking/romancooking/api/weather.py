import requests

def get_weather_data(city):
    API_KEY = 'YOUR_API_KEY'  # Ersetzen Sie dies durch Ihren API-Schlüssel
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data
