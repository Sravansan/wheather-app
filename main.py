import requests
import tkinter
from tkinter import *

def get_weather():
    city = entry.get()
    api_key = "your_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"] - 273.15  # Kelvin to Celsius

        z = x["weather"]
        weather_description = z[0]["description"]

        result_label['text'] = f"{city.capitalize()}: {weather_description.capitalize()}, {current_temperature:.2f}°C"
    else:
        result_label['text'] = "City not found!"

window = Tk()
window.minsize(400, 400)
window.title("Hava Durumu")

label1 = Label(window, text="Enter the city name:")
label1.grid(row=0, column=0)

entry = Entry(window)
entry.grid(row=0, column=1)

get_weather_button = Button(window, text="Submit", command=get_weather)
get_weather_button.grid(row=1, columnspan=2)

result_label = Label(window, text="")
result_label.grid(row=2, columnspan=2)

window.mainloop()
