# 1. Tehtävä
print("Hei, Laura Erelaakso!")


# 2. Tehtävä

# 2.1
# Huomautus, en saanut tuota yhtä väliä pois vaikka yritin.
username = input("Mikä sinun nimesi on? ")
print("Morjes"",", username,"!")
username = input

# 2.2

import math
r_string = input("Mikä ympyrän säde on (m)? ")
r = float(r_string)
area = math.pi * r * r
print(f"{r} (m) säteisen ympyrän pinta-ala on n. {area:.3f} neliömetriä.")

# 2.3

a_string = input("Mikä on suorakulmion kannan pituus (m)? ")
o_string = input("Mikä on suorakulmion korkeus (m)? ")
a = float(a_string)
o = float(o_string)
area = a * 2 + o * 2
area1 = a * o
print(f"Suorakulmion piiri on {area: .3f}")
print(f"Suorakulmion pinta-ala on {area1: .3f}")

# 2.4

j_string = input("Syötä kokonaisluku: ")
k_string = input("Syötä toinen kokonaisluku: ")
l_string = input("Syötä kolmas kokonaisluku: ")
j = float(j_string)
k = float(k_string)
l = float(l_string)
area2 = j + k + l
area3 = j * k * l
area4 = (j+k+l)/3
print(f"Lukujen summa on {area2: .0f}")
print(f"Lukujen tulo on {area3: .0f}")
print(f"Lukujen keskiarvo on {area4: .3f}")


