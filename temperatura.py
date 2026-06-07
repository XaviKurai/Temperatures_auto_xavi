import requests, json
from datetime import datetime

LAT = 41.3851   # Barcelona
LON = 2.1734
TODAY = datetime.now().strftime('%Y-%m-%d')

url = (
    'https://api.open-meteo.com/v1/forecast'
    f'?latitude={LAT}&longitude={LON}'
    '&hourly=temperature_2m'
    f'&start_date={TODAY}&end_date={TODAY}'
    '&timezone=Europe/Madrid'
)

resp = requests.get(url)
data = resp.json()
temps = data['hourly']['temperature_2m']

result = {
    'date':    TODAY,
    'location': 'Barcelona',
    'max_temp': max(temps),
    'min_temp': min(temps),
    'avg_temp': round(sum(temps) / len(temps), 2),
    'hourly':   temps
}

filename = f"temp_{datetime.now().strftime('%Y%m%d')}.json"
with open(filename, 'w') as f:
    json.dump(result, f, indent=2)

print(f'Fitxer guardat: {filename}')
