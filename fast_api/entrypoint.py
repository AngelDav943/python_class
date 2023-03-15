from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "Inicio"


@app.get("/hola")
def adios():
    return "Hola mundo!"


@app.get("/hola/{nombre}")
def adios(nombre : str):
    return "Hola " + nombre


@app.get("/adios")
def adios():
    return "Adios mundoooo"

@app.get("/area/cuadrado/{lado}")
def area_cuadr(lado: int):
    return lado

# nombre, edad, si es mayor de edad
@app.get("/verifmayor/{nombre}/{edad}")
def verifmayor(nombre:str, edad:int):
    if edad >= 18:
        return f"{nombre} es mayor de edad"
    return f"{nombre} es menor de edad"