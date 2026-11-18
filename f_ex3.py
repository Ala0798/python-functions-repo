def aria(lungime, latime):
    lungime = 50
    latime = 40
    return lungime * latime
lungime2 = int(input())
latime2 = int(input())
aria = aria(lungime2, latime2)
print(f"aria este: {aria}")

def aria2(lungime, latime):
    lungime = lungime2
    latime = latime2
    return lungime * latime
rezultat = aria2(1, 2)
print(rezultat)