#!/usr/bin/env python3
import requests
import os

# Load config from private file
CONFIG_FILE = "/etc/eww_weather"
if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, val = line.strip().split('=', 1)
                os.environ[key] = val
else:
    print("Err")
    exit(1)

# Use environment variables
LATITUDE = float(os.environ.get('LATITUDE', 0))
LONGITUDE = float(os.environ.get('LONGITUDE', 0))
API_KEY = os.environ.get('API_KEY', '')
# -------------------------

def get_weather_icon(weather_id, icon_str):
    # Special handling for Clear Sky (800)
    # We check the icon string: '01d' = day, '01n' = night
    if weather_id == 800:
        if 'n' in icon_str:
            return "🌙"  # Moon for clear night
        else:
            return "☀️"  # Sun for clear day

    # Map other codes to Emojis
    if 200 <= weather_id < 300: return "⛈"  # Thunderstorm
    if 300 <= weather_id < 400: return "🌧"  # Drizzle
    if 500 <= weather_id < 600: return "🌧"  # Rain
    if 600 <= weather_id < 700: return "❄️"  # Snow
    if 700 <= weather_id < 800: return "🌫"  # Atmosphere (Fog, Mist)
    if 801 <= weather_id < 900: return "☁️"  # Clouds
    return "🌤"                         # Default/Unknown

try:
    # Fetch current weather from OpenWeatherMap
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&appid={API_KEY}&units=metric"
    
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()

    # Get Temperature (round to integer)
    temp = int(data['main']['temp'])
    
    # Get Weather Condition ID (e.g., 800) and Icon String (e.g., '01n')
    weather_id = data['weather'][0]['id']
    icon_str = data['weather'][0]['icon']
    
    # Get Icon
    icon = get_weather_icon(weather_id, icon_str)

    # Print clean text for Eww (Example: 🌙 20°C)
    print(f"{icon} {temp}°C")

except Exception as e:
    # If API fails, print a fallback so the bar doesn't break
    print("Err")
