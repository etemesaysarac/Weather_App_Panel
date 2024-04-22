import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests
from tkinter.font import BOLD, Font

window = Tk()
window.title('Weather Map Application')
window.minsize(600,600)
window.config(padx=20,pady=20)

image = tkinter.PhotoImage(file="image3.png", width=200, height=200)
label_image = ttk.Label(image=image)
label_image.pack()

label_title = Label(window, text='Enter your City Name')
label_title.config(pady=5)
label_title.pack()
entry_title = Entry()
entry_title.focus()
entry_title.pack()

def weatherCheck():
    api_key = "19020da4a11117180df6bc3b31a6fec5"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = entry_title.get()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        label1 = Label(window,font=("Arial", 15, BOLD), text='According to Your City Information : \n\nYour city name = {}, \nTemperature (in kelvin unit) = {}, \n Atmospheric pressure (in hPa unit) = {}, \n Humidity (in percentage) =  {}, \n Description = {}.'.format(city_name,current_temperature, current_pressure, current_humidity,weather_description ))
        label1.pack()

    else:
        print(" City Not Found ")

button = Button(text = 'Weather Check', command = weatherCheck)
button.pack()

window.mainloop()