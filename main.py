import requests

API_KEY = "494240e0c2e79e91a921159ffe7d3629"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter your City: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather_desc = data['weather'][0]['description']
    print("The Weather is: ", weather_desc)
    temperature = data['main']['temp']
    temp_cel = round(temperature - 273.15, 2)
    print("Temperature: ", temp_cel, " celsius")

else:
    print("An Error Occurred!")
