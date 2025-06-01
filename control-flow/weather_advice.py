# Ask the user about the current weather conditions and provide clothing recommendations based on input.

#weather = ["sunny", "rainy", "cold"]
weather_condition = input("What's the weather like today? (sunny/rainy/cold): ")

if weather_condition == "sunny":
    print("Wear a t-shirt and sunglasses.")

elif weather_condition == "rainy":
    print("Don't forget your umbrella and raincoat.")

elif weather_condition == "cold":
    print("Make sure to wear a warm coat and scarf.")

else:
    print("Sorry, I don't have recommendations for this weather.")



