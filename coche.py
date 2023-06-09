from random import randint, uniform

TIPO_MOTOR = (
    "combustion",
    "hibrido",
    "electrico"
)

TIPO_COMBUSTIBLE = (
    "gasolina",
    "gasoil",
    "gas"
)

KW_BAT = {
    "min": 6,
    "max": 80
}

class Coche:
    def __init__(self, marca: str, modelo: str, matricula: str ) -> None:

        def crear_motor():
            usa_combustible = (
                TIPO_MOTOR[0],
                TIPO_MOTOR[1]
            )
            usa_bateria = (
                TIPO_MOTOR[1],
                TIPO_MOTOR[2]
            )

            motor = {
                "tipo": TIPO_MOTOR[randint(0, 2)]
            }

            if motor["tipo"] in usa_combustible:
                motor["combustible"] = TIPO_COMBUSTIBLE[randint(0, 2)]
                print("combustible añadido")

            if motor["tipo"] in usa_bateria:
                motor["kw_bat"] = uniform(KW_BAT["min"], KW_BAT["max"])
                print("kw_bat añadido")

            return motor

        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.motor = crear_motor()

    def __str__(self) -> str:
        buffer = f"{self.marca} - {self.modelo} [{self.matricula}]\n"
        buffer += f"    - {self.motor['tipo']}\n"
        if "combustible" in self.motor:
            buffer += f"    - {self.motor['combustible']}\n"
        if "kw_bat" in self.motor:
            buffer += f"    - {self.motor['kw_bat']}\n"

        return f"{buffer}"
