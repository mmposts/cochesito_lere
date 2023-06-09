# cocherito_lere

Ejercicio de clases y Objetos
## TODO:

```python
    TIPO_MOTOR = (
        "cambustion",
        "hibrido",
        "electrico"
    )

    TIPO_COMBUSTIBLE = (
        "gasolina",
        "gasoil",
        "gas"
    )
```

- Coche
    - marca : str
    - modelo : str
    - matricula : str
    - motor: { tipo | combustible | kw_bat }
    - __str__()
- Plaza:
    - numero: int
    - coche: Coche
    - estacionar(coche)
    - desocupar()
    - esta_disponible()
    - __str__()
        VACIO
        Coche
- Parking:
    - CANT_PLAZAS = 200
    - Plazas: []
    - aparcar(Coche)
    - desaparcar(num_plaza)
    - listar()
    - listar_ocupadas()
    - listar_disponibles()
- Main:
    - CREAR ESTAS CLASES
    - Main: generar 200 coches
    - aparcar 90%
    - desaparcar 30% de lo aparcado
    - listar_ocupadas()
    - listar()
    - listar_disponibles()
