import random
temp = int(random.choice(["10","12","14","16","18","20","22"]))
forecast = random.choice  (["cloudy","sunny","rainy"])
if temp >= 14 and forecast == "cloudy":
    print(f"The Temp is {temp} and the forecast is {forecast}. Wear a thick winter coat it may be chilly")
elif temp <= 16 and forecast == "cloudy":
    print(f"The Temp is {temp} and the forecast is {forecast}.It's starting to get quite warm! Still rememeber to wear long sleeves though")
elif temp <= 20 and forecast == "sunny":
    print(f"The Temp is {temp} and the forecast is {forecast}.It's lovely weather wear some nice short sleaves")
elif temp <= 15 and forecast == "rainy":
    print(f"The Temp is {temp} and the forecast is {forecast}.You don't need a thick winter coat. Rememeber to wear a rain coat though")