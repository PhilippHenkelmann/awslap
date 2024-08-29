import requests
from django.shortcuts import render

def get_weather_data(city):
    API_KEY = 'YOUR_API_KEY'  # Ersetzen Sie dies durch Ihren API-Schlüssel
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Überprüfen Sie, ob die Anfrage erfolgreich war
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching data for {city}: {e}")
        return {}

def home_view(request):
    cities = ['Rome', 'Cologne', 'Xanten', 'Carthage', 'Athens', 'Ephesus', 'Alexandria']
    weather_data = {}

    for city in cities:
        data = get_weather_data(city)
        temperature = data.get('main', {}).get('temp', 'N/A')  # Temperatur abrufen
        weather_data[city] = temperature

    return render(request, 'home.html', {'weather_data': weather_data})
