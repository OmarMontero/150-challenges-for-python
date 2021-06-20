rain = input("It´s raining today?(yes/no)")
rain = str.lower(rain)
if rain == "yes":
    wind = input("It´s windy today?(yes/no)")
    wind = str.lower(wind)
    if wind == "yes":
        print("It´s too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")
    
