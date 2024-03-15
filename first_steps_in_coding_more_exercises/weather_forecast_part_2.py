degrees = float(input())
if 5 <= degrees <= 11.9:
    print("Cold")
elif 11.9 < degrees <= 14.9:  # ако няма долна граница  влиза тук и на др места, затова навсякъде трябва и долна граница
    print("Cool")
elif 14.9 < degrees <= 20:
    print("Mild")
elif 20 < degrees <= 25.9:
    print("Warm")
elif 25.9 < degrees <= 35:
    print("Hot")
else:
    print("unknown")
