print(" *** Wind classification ***")
wind = float(input("Enter wind speed (km/h) : "))
print("Wind classification is",end=' ')
if wind<51.99 :
    print("Breeze.")
elif 52.00<wind<55.99 :
    print("Depression.")
elif 56.00<wind<101.99 :
    print("Tropical Storm.")
elif 102.00<wind<208.99 :
    print("Typhoon.")
else :
    print("Super Typhoon.")
