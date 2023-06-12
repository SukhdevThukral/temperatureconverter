digits = (range(1 - 100))
speed = int(input('Speed as per second: '))
print("""Info - Enter K for kilometre per second and M for metre per second(Remember not to give digits as 
'1 m/s converted to km/s""")
unit = input('km/s or m/s: ')
if unit.upper() == "K":
    converted = speed * 1000
    print(f"Speed converted to km/s = {converted}")
else:
    converted = speed // 1000
    print(f"Speed converted to km/s = {converted}")