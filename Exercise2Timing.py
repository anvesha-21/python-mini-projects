import time

timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("Enter Number:"))

if(hour >= 4 and hour <= 12):
    print("@Good Morning")
elif(hour >= 12 and hour <= 17):
    print("@Good AFterNoon")
elif(hour >= 17 and hour <= 20):
    print("@Good Evening")
else:
    print("GOOD NIGHT")


