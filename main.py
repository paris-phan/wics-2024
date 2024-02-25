from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import math
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder


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

    def militaryToStandard(time):
        time = int(time)
    
        hours = math.floor(time /100)
        minutes = (time % 100)*.6
    
        if minutes >= 60:
            extra_hours = minutes // 60
            minutes = minutes % 60
            hours += extra_hours

        period = "AM"
        if hours >= 12:
            period = "PM"
            if hours > 12:
                hours -= 12
        if hours == 0:
            hours = 12
        if time == 2400:
            period = "AM"
            
        minutes = int(minutes)
        
        if minutes ==0:
            return str(hours) +":"+ str(minutes) + "0" + period
        return str(hours) + ":"+ str(minutes) + period

        
    def displayResults(timeDifference, day1, day2, day3, departingCity, arrivingCity):
        def open_new_window(timeDifference, day1, day2, day3, departingCity, arrivingCity):
            root.destroy()
        
            new_window = Tk()
            new_window.title("Results")
            new_window.geometry("450x200")

            day1 = militaryToStandard(day1)
            day2 = militaryToStandard(day2)
            day3 = militaryToStandard(day3)

            infoString = arrivingCity + " is " + str(abs(round(timeDifference,3))) + " hours ahead of " + departingCity
            if(timeDifference < 0):
                infoString = infoString.replace("ahead", "behind")

            label = Label(new_window, text=infoString)
            label.pack()

            label2 = Label(new_window, text="Sleep at " + str(day1)+ " 1 day before your departure") 
            label2.pack()

            label3 = Label(new_window,  text="Sleep at " + str(day2)+ " 2 days before your departure")
            label3.pack()

            label4 = Label(new_window,  text="Sleep at " + str(day3)+ " 3 days before your departure")
            label4.pack()

            new_window.mainloop()

        try:    
            open_new_window(timeDifference, day1, day2, day3, departingCity, arrivingCity)
        except Exception as error:
            print("ERROR in displayResults! give a fuck", error)
        return
        
    def getGeoLocation(city, country):
        try:
            print("Getting GeoLocation for: " + city + ", " + country)
            geolocator = Nominatim(user_agent="main")
            
            location = geolocator.geocode(city + ", " + country)
            return getTimeZone(location.longitude)
        except:
            print("ERROR in getGeoLocation()! give a fuck")

    def getTimeZone(longitude):
        try:
            print("Getting Timezone")
                
            timeZoneHours = (longitude / 0.004167) / 3600
            return timeZoneHours
            


        except:
            print("ERROR in getTimeZone()! give a fuck")

    #convert time format '11:00 PM' to military
    def standardToMilitary(input):
        try:
            time = str(input[6:8])
            print(time)
            military = 0
            if(time == 'PM'):
                military = 1200
            hours = int(input[0:2])
            minutes = int(input [3:5])
            military = military + (hours * 100) + minutes
            #print("military time: " , military)
            return military
        except:
            print("Error in standardToMilitary!")

        
        
 
    def calculate():
        print("Calculating...")
        try:
            departingCity = depCity.get()
            departingCountry = depCountry.get()
            arrivingCity = arrCity.get()
            arrivingCountry = arrCountry.get()
            sleepTimeValue = standardToMilitary(sleepTime.get())


            
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
                if(sleepTimeValue == ""):
                    sleepTimeEntry.selectbackground("red")
                return
            
            departingTimezone = getGeoLocation(departingCity, departingCountry)
            arrivingTimezone = getGeoLocation(arrivingCity, arrivingCountry)
            timeDifference = arrivingTimezone - departingTimezone

            offsetPerDay = timeDifference / 3 * 100
            day1 = sleepTimeValue - offsetPerDay
            day2 = day1 - offsetPerDay
            day3 = day2 - offsetPerDay

            if(day3 > 2400):
                day3 = day3-2400
            if(day2 > 2400):
                day2 = day2-2400
            if(day1 > 2400):
                day1 = day1-2400

            print("Departing from: " + departingCity + ", " + departingCountry)
            displayResults(timeDifference, day1, day2, day3,departingCity, arrivingCity)
            


        except Exception as error:
            print("ERROR in calculate()! give a fuck", error)
            return
            
        




    




    ### MAIN WINDOW
    ### MAIN WINDOW

    root = Tk()

    depCity = StringVar()       #ex. 'Charlottesville'
    depCountry = StringVar()    #ex. 'United States'
    arrCity = StringVar()       #ex. 'London'
    arrCountry = StringVar()    #ex. 'England'
    sleepTime = StringVar()        #ex. 2300 [Military time]

    root.title("JetLag Calculator")
    #root.geometry("800x1080")

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
    sleepTimeEntry = Entry(root, textvariable=sleepTime)
    sleepTimeEntry.grid(row=5, column=1)

    calculate = Button(root, text="Calculate", command=calculate)
    calculate.grid(row=6, column=0, columnspan=2)

    reset = Button(root, text="Reset", command=closeWindow)
    reset.grid(row=6, column=0)

    quit = Button(root, text="Quit", command=root.destroy)
    quit.grid(row=6, column=1)

    root.mainloop()



main()


