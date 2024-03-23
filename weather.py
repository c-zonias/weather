import requests

api_key = '4749218e17bcc6dede4747840809cb5f'

input = ("Enter City: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {input} is: {weather}")
    print(f"The temperature in {input} is: {temp}ºF")