
input = "11:00 AM"


time = str(input[6:8])

military = 0
if(time == 'PM'):
    military = 1200
hours = int(input[0:2])
minutes = int(input [3:5])
military = military + (hours * 100) + minutes
#print("military time: " , military)
print(str(military))