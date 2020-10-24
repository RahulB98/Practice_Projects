from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Weather App")
root.iconbitmap("C:/Users/messi/Downloads/favicon.ico")
root.geometry("400x100")

# Create Zip looup function
def zipLookup():
    try:
        api_request = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=25&API_KEY=D4A60EF3-39C1-418E-8433-9E4BE05D4ABB")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_colour = "#0C0"
        elif category == "Moderate":
            weather_colour = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_colour = "#ff9900"
        elif category == "Unhealthy":
            weather_colour = "#FF0000"
        elif category == "Very Unhealthy":
            weather_colour = "#990066"
        elif category == "Hazardous":
            weather_colour = "#660000"

        root.configure(background=weather_colour)
        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 14),
                        background=weather_colour)
        myLabel.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error..."
        myLabel =  Label(root, text=api)
        myLabel.grid(row=1, column=0, columnspan=2)

zip = Entry(root)
zip.grid(row=0, column=0, stick=W+E+N+S)

zipButton = Button(root, text="Look Up Zipcode", command=zipLookup)
zipButton.grid(row=0, column=1, stick=W+E+N+S)

root.mainloop()