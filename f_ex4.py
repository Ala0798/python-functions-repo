def aria(lungime, latime):
    lungime = 50
    latime = 40
    return lungime * latime   # 40 x 50  = 2000

lungime2 = int(input())
latime2 = int(input())

rezultat1 = aria(lungime2, latime2)  # 2000
print(f"aria este: {rezultat1}")

def aria2(lungime, latime):
    lungime = lungime2
    latime = latime2
    return lungime * latime

rezultat2 = aria2(1, 2)
print(rezultat2)  # 20