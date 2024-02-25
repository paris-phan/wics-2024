from tkinter import *
from tkinter import ttk

from geopy.geocoders import Nominatim


##test loc api call
#import requests
#response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA')

canvas_height = 1080
canvas_width = 1920
canvas_colour = "gray30"

def main():

    def closeWindow():
        root.destroy()
        main()
        
    def displayResults():
        ###TODO: display results
        return
    
    def getGeoLocation(city, country):
        try:
            print("Getting GeoLocation...")
            address = city + ", " + country
            geolocator = Nominatim(user_agent="Geopy Library")

            getLoc = geolocator.geocode(address)

            print(getLoc.address)
            print((getLoc.latitude, getLoc.longitude))
        except:
            
            print("ERROR in getGeoLocation()! give a fuck")
 
    
    def calculate():
        print("Calculating...")
        try:
            departingCity = depCity.get()
            departingCountry = depCountry.get()
            arrivingCity = arrCity.get()
            arrivingCountry = arrCountry.get()
            #sleepTime = sleepTime.get()
            sleepTime= int(sleepTime.get())
            #depCityEntry.selectbackground("red")
            if(departingCity == "" or departingCountry == "" or arrivingCity == "" or arrivingCountry == ""):
                print("Missing Inputs")
                if(departingCity == ""):
                    depCityEntry.selectbackground("red")
                if(departingCountry == ""):
                    depCountryEntry.selectbackground("red") 
                if(arrivingCity == ""):
                    arrCityEntry.selectbackground("red")
                if(arrivingCountry == ""):
                    arrCountryEntry.selectbackground("red")
                return
            
            getGeoLocation(departingCity, departingCountry)
            

    
    




            
        except:
            print("ERROR in calculate()! give a fuck")
            return
            
        
        print("Departing from: " + departingCity + ", " + departingCountry)



    




    ### MAIN WINDOW

    root = Tk()

    depCity = StringVar()       #ex. 'Charlottesville'
    depCountry = StringVar()    #ex. 'United States'
    arrCity = StringVar()       #ex. 'London'
    arrCountry = StringVar()    #ex. 'England'
    sleepTime = StringVar()        #ex. 2300 [Military time]

    root.title("JetLag Calculator")
    root.geometry("800x1080")

    label1 = Label(root, text="Enter the following fields to get you roptimized sleep schedule")
    label1.grid(row=0, column=0, columnspan=2)

    # Labels for the entry fields
    Label(root, text="Departing City:").grid(row=1, column=0, sticky=E)
    Label(root, text="Departing Country:").grid(row=2, column=0, sticky=E)
    Label(root, text="Arriving City:").grid(row=3, column=0, sticky=E)
    Label(root, text="Arriving Country:").grid(row=4, column=0, sticky=E)
    Label(root, text="What time you want to go to bed at:").grid(row=5, column=0, sticky=E)

 
    depCityEntry = Entry(root, textvariable=depCity)
    depCityEntry.grid(row=1, column=1)
    depCountryEntry = Entry(root, textvariable=depCountry)
    depCountryEntry.grid(row=2, column=1)
    arrCityEntry = Entry(root, textvariable=arrCity)
    arrCityEntry.grid(row=3, column=1)
    arrCountryEntry = Entry(root, textvariable=arrCountry)
    arrCountryEntry.grid(row=4, column=1)
    sleepTime = Entry(root, textvariable=sleepTime)
    sleepTime.grid(row=5, column=1)

    calculate = Button(root, text="Calculate", command=calculate)
    calculate.grid(row=6, column=0, columnspan=2)

    reset = Button(root, text="Reset", command=closeWindow)
    reset.grid(row=6, column=0)

    quit = Button(root, text="Quit", command=root.destroy)
    quit.grid(row=6, column=1)

    root.mainloop()



main()






