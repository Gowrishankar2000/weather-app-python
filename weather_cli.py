import requests
import json
import argparse
import os 
from dotenv import load_dotenv

load_dotenv()

def fetch_weather(city_name):
    API_Key=API_key = os.getenv('OPENWEATHER_API_KEY')
    if not API_key:
             print("❌ Error: API key not found. Set the OPENWEATHER_API_KEY environment variable.")
             return
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'
    response=requests.get(url)
    
    if response.status_code==200:
        data=response.json()
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
            print(f"\n🌦️  Current Weather in {city_name.title()}")
            print(f"Description     : {data['weather'][0]['description']}")
            print(f"Temperature     : {data['main']['temp']}°C")
            print(f"Feels Like      : {data['main']['feels_like']}°C")
            print(f"Humidity        : {data['main']['humidity']}%\n")
    else:
            print(f"❌ Error: Unable to fetch data for '{city_name}'. (Status Code: {response.status_code})")

def main():
    parser = argparse.ArgumentParser(description="Fetch current weather data for a city.")
    parser.add_argument("city", help="City name (e.g., Mumbai, Chennai)")
    args = parser.parse_args()

    fetch_weather(args.city)

if __name__=='__main__':
     main()

