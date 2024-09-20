weather1 = 'sunny'
weather2 = 'rainy'
weather3 = 'cold'

weather = input ("What's the weather like today? (sunny/rainy/cold): ")
if weather == weather1:
    print ("Wear a t-shirt and glasses.")
elif weather == weather2:
    print ("Don't forget your umbrella and raincoat.")
elif weather == weather3:
    print ("Make sure to wear a warm coat and a scarf.")

else:
    print ("Sorry, I don't have recommendations for this weather.")