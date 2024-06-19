import requests
from tkinter import *

def weather():
    city = city_listbox.get()
    api_key = "bd5e378503939ddaee76f12ad7a97608"  # Replace "YOUR_API_KEY" with your actual OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res = requests.get(url)
    output = res.json()

    weather_status = output['weather'][0]['description']
    temperature = output['main']['temp']
    humidity = output['main']['humidity']
    wind_speed = output['wind']['speed']

    weather_status_label.configure(text="Weather Status: " + weather_status)
    temperature_label.configure(text="Temperature: " + str(temperature) + "°C")
    humidity_label.configure(text="Humidity: " + str(humidity) + "%")
    wind_speed_label.configure(text="Wind Speed: " + str(wind_speed) + " m/s")

window = Tk()
window.geometry("400x350")

city_name_list = ["Lucknow", "Delhi", "Bangalore", "Pune", "Tamil Nadu"]

city_listbox = StringVar(window)
city_listbox.set("Select the city")
option = OptionMenu(window, city_listbox, *city_name_list)
option.grid(row=2, column=2, padx=150, pady=10)

b1 = Button(window, text="Press", width=15, command=weather)
b1.grid(row=5, column=2, padx=150)

weather_status_label = Label(window, font=("times", 10, "bold"))
weather_status_label.grid(row=10, column=2)

temperature_label = Label(window, font=("times", 10, "bold"))
temperature_label.grid(row=12, column=2)

humidity_label = Label(window, font=("times", 10, "bold"))
humidity_label.grid(row=14, column=2)

wind_speed_label = Label(window, font=("times", 10, "bold"))
wind_speed_label.grid(row=16, column=2)

window.mainloop()
