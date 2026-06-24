from fastapi import FastAPI

from weather_service import (
    get_current_weather,
    get_temperature,
    get_humidity,
    get_condition,
    get_wind_speed
)


app = FastAPI()



@app.get("/")
def home():

    return {
        "message":
        "Weather Intelligence API Running"
    }



@app.get("/weather/{city}")
def weather(city):

    return get_current_weather(city)



@app.get("/temperature/{city}")
def temperature(city):

    return get_temperature(city)



@app.get("/humidity/{city}")
def humidity(city):

    return get_humidity(city)



@app.get("/condition/{city}")
def condition(city):

    return get_condition(city)



@app.get("/wind/{city}")
def wind(city):

    return get_wind_speed(city)