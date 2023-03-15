from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()

personas = []

class Libro(BaseModel):
    nombre:str
    fecha:str

class Persona(BaseModel):
    nombre:str
    libros:list[Libro]

def persona_existe(id): # Verifica si usuario existe
    return id > 0 and id <= len(personas)

@app.get("/")
def hello_world():
    return {
        "titulo":"Biblioteca",
        "version":"v0.0.1"
    }
    
@app.get("/personas")
def personas_all():
    return personas

@app.get("/personas/{id}")
def personas_all(id: int):
    if persona_existe(id):
        return personas[id - 1]
    
@app.post("/personas")
def personas_add(nombre: str):
    usuario = {
        "nombre": str(nombre).lower(),
        "libros": []
    }
    personas.append(usuario)
    return usuario

@app.put("/personas")
def personas_modify(id: int, nuevo_nombre:str):
    if persona_existe(id): # Verifica si usuario existe
        personas[id - 1]["nombre"] = str(nuevo_nombre).lower()
        return True

@app.delete("/personas")
def personas_delete(id: int):
    if persona_existe(id): # Verifica si usuario existe
        personas.pop(id - 1)
        return True

@app.post("/libro")
def libro_add(id: int, libro:str):
    if persona_existe(id):
        personas[id - 1]["libros"].append({
            "nombre": libro,
            "fecha": str(date.today()),
            "estado": "prestado"
        })
        return True