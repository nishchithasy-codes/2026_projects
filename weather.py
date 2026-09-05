import requests

api_key = "adc5516138c4f011645220014f3562af"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

data = response.json()

temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
condition = data["weather"][0]["description"]
wind_speed = data["wind"]["speed"]

print()
print("🌦️ Weather Report")
print("------------------------")
print("City:", city)
print("Temperature:", temperature, "°C")
print("Feels Like:", feels_like, "°C")
print("Condition:", condition)
print("Humidity:", humidity, "%")
print("Wind Speed:", wind_speed, "m/s")