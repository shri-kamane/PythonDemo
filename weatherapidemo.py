import requests
name="Pavan"
city="Pune"
url="https://api.open-meteo.com/v1/forecast"
params = {'latitude': 18.5204, 'longitude': 73.8567, 'current_weather': True}
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    print(f"Hello {name} from {city}!")
    print("Current temperature of pune:")
    print(data['current_weather']['temperature'])