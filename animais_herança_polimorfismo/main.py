from urso import Urso
from arara import Arara
from baleia import Baleia

def mostrar_animal(animal):
    print(f"Raça: {animal.raca}")
    print(f"Habitat: {animal.habitat()}")
    print(f"Locomoção: {animal.locomocao()}")
    print(f"alimentacao: {animal.alimentacao()}")
    print()

urso = Urso("Urso Pardo")
arara = Arara("Arara Azul")
baleia = Baleia("Baleia Jubarte")

mostrar_animal(urso)
mostrar_animal(arara)
mostrar_animal(baleia)