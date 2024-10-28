import random 

print("SELAMAT DATANG DI LOVEMETER")

nama_dia = "Nadya"

cocok = random.random()
print("Kecocokan Anda", cocok * 100, "%")

if cocok > 0.9:
    print("Anda sangat cocok dengan " + nama_dia + "!")
elif 0.7 <= cocok <= 1.0:
    print("Anda lumayan cocok dengan " + nama_dia + "!")
else :
    print("Anda tidak cocok dengan " + nama_dia + "!")    