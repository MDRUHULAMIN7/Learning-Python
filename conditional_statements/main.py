# name = 4

# if name == 1:
#     print("sss")
# elif name == 4:
#     print("4")
# else:
#     print("sssssssssssss")
temperature = float(input("Enter temperature in Celsius: "))

if temperature < 0:
    print("Freezing Cold ❄️")
elif 0 <= temperature <= 10:
    print("Very Cold 🥶")
elif 10 < temperature <= 20:
    print("Cold 🧦")
elif 20 < temperature <= 30:
    print("Pleasant ☁️")
elif 30 < temperature <= 40:
    print("Hot 🔥")
else:
    print("Very Hot 🫠")