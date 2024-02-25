longitude = 42.15188
negative = False
if(longitude < 0):
    negative = True
    longitude *= -1
    
degrees = int(longitude)
timeValue = (longitude % 1) * 60
minutes = int(timeValue)
seconds = int((timeValue % 1) * 60)

print(degrees, minutes, seconds)