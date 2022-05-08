import requests
import datetime
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Хмарно \U00002601",
        "Rain": "Дощ \U00002614",
        "Drizzle": "Дощ \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Сніг \U0001F328",
        "Mist": "Туман \U0001F32B",
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        cur_weather = data['main']['temp']

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Look at your window, dude."

        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Weather in {city}\nTemperature: {cur_weather}C° {wd}\n"
              f"Vologist(Humidity): {humidity}%\n"
              f"Wind of change: {wind} m/s\n"
              f"Sunrise: {sunrise_timestamp}\n"
              f"Sunrise: {sunset_timestamp}\n"
              f"Day length: {length_of_day}\n"
              f"Have a nice day!!")

    except Exception as ex:
        print(ex)
        print("Check the city name.")


def main():
    city = input("Please, choose your city...  ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
