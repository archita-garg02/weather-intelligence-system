import requests

from config import (
    WEATHER_API_KEY,
    BASE_URL
)


def get_current_weather(city):

    url = f"{BASE_URL}/weather"


    params = {

        "q": city,

        "appid": WEATHER_API_KEY,

        "units": "metric"

    }


    response = requests.get(
        url,
        params=params
    )


    return response.json()

def get_temperature(city):

       data=get_current_weather(city)

       return{
        "city":city,
        "temperature":data["main"]["temp"]
       }

def get_humidity(city):

    data=get_current_weather(city)

    return {
        "city":city,
        "humidity":data["main"]["humidity"]
    }

def get_condition(city):

    data = get_current_weather(city)

    return {
        "city": city,
        "condition": data["weather"][0]["description"]
    }



def get_wind_speed(city):

    data = get_current_weather(city)

    return {
        "city": city,
        "wind_speed": data["wind"]["speed"]
    }