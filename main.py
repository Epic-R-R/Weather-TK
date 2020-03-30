import json
import requests
import tkinter as tk
from tkinter import *
from tkinter import messagebox


def widgets():
    cityLable = Label(root, text="Enter city : ", bg="skyblue")
    cityLable.grid(row=0, column=0, padx=10, pady=5)
    cityEntry = Entry(root, width=36, textvariable=cityName)
    cityEntry.grid(row=0, column=1, padx=10, pady=5)

    findButton = Button(root, text="Find", command=findWeather)
    findButton.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

    clearButton = Button(root, text="Clear", command=clear)
    clearButton.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

    cityCoord = Label(root, text="Coordinates : ", bg="skyblue")
    cityCoord.grid(row=2, column=0, padx=10, pady=5)
    root.cityCoord = Entry(root, width=36)
    root.cityCoord.grid(row=2, column=1, padx=10, pady=5)

    tempLabel = Label(root, text="Temperature : ", bg="skyblue")
    tempLabel.grid(row=3, column=0, padx=10, pady=5)
    root.tempEntry = Entry(root, width=36)
    root.tempEntry.grid(row=3, column=1, padx=10, pady=5)

    humidityLabel = Label(root, text="Humidity : ", bg="skyblue")
    humidityLabel.grid(row=4, column=0, padx=10, pady=5)
    root.humidityEntry = Entry(root, width=36)
    root.humidityEntry.grid(row=4, column=1, padx=10, pady=5)

    windLabel = Label(root, text="Wind : ", bg="skyblue")
    windLabel.grid(row=5, column=0, padx=10, pady=5)
    root.windEntry = Entry(root, width=36)
    root.windEntry.grid(row=5, column=1, padx=10, pady=5)

    pressureLabel = Label(root, text="Pressure : ", bg="skyblue")
    pressureLabel.grid(row=6, column=0, padx=10, pady=5)
    root.pressureEntry = Entry(root, width=36)
    root.pressureEntry.grid(row=6, column=1, padx=10, pady=5)

    descLabel = Label(root, text="Description : ", bg="skyblue")
    descLabel.grid(row=7, column=0, padx=10, pady=5)
    root.descEntry = Entry(root, width=36)
    root.descEntry.grid(row=7, column=1, padx=10, pady=5)


def findWeather():
    apiKey = "f004740f49ac507666c365cd4a28367d"
    url = "http://api.openweathermap.org/data/2.5/weather?"
    cityname = cityName.get()
    req = f"{url}appid={apiKey}&q={cityname}&units=metric"
    response = requests.get(req)
    jsonResponse = response.json()
    if jsonResponse["cod"] != 404:
        weatherpar = jsonResponse["main"]
        coordinates = jsonResponse["coord"]
        latitude = str(coordinates["lat"])
        longitude = str(coordinates["lon"])
        wind = jsonResponse["wind"]
        windspeed = str(wind["speed"])
        if "deg" in wind.keys():
            windDirect = str(wind["deg"])
        else:
            windDirect = ""
        temperature = str(weatherpar["temp"])
        pressure = str(weatherpar["pressure"])
        humidiy = str(weatherpar["humidity"])
        weatherDesc = jsonResponse["weather"]
        weatherDesctiption = weatherDesc[0]["description"]
        root.cityCoord.insert("0", f"Latitude : {latitude} Longtitude : {longitude}")
        root.tempEntry.insert("0", f"{temperature} °C")
        root.humidityEntry.insert("0", f"{str(humidiy)} %")
        root.windEntry.insert("0", f"Speed : {windspeed} Meter/Sec Direction : {windDirect}")
        root.pressureEntry.insert("0", f"{pressure} Hpa")
        root.descEntry.insert("0", weatherDesctiption)
    else:
        messagebox.showerror("Error", "City Not Found")


def clear():
    cityName.set("")
    root.cityCoord.delete(0, END)
    root.tempEntry.delete(0, END)
    root.humidityEntry.delete(0, END)
    root.windEntry.delete(0, END)
    root.pressureEntry.delete(0, END)
    root.descEntry.delete(0, END)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Weather TK")
    root.config(background="skyblue")
    root.geometry("570x320")
    root.resizable(False, False)
    cityName = StringVar()
    widgets()
    root.mainloop()
