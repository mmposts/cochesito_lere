from parking import Parking
from coche import Coche

parking = Parking()

coches = [
  Coche("Peugot", "307", "7778-MXD"),
  Coche("Ciröen", "C5", "1234-ABC")  
]

print("Hola Cochecito Lere")
for coche in coches:
    print(f"Coche: {coche}")
