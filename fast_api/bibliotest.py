from fastapi import FastAPI

app = FastAPI()

usuarios = [
    {
        "nombre":"Juan",
        "libros":[
            {
                "nombre":"Libro A",
                "fecha" :"01/03/2023",
                "estado":"prestado"
            },
            {
                "nombre":"Habitos Atomicos",
                "fecha" :"01/03/2022",
                "estado":"prestado"
            }
        ]
    },
    {
        "nombre":"David",
        "libros":[
            {
                "nombre":"Libro A",
                "fecha" :"01/03/2023",
                "estado":"prestado"
            }
        ]
    }
]

@app.get("/usuario/{id}")
def usuario(id:int):
    return usuarios[id-1]


@app.get("/libro/{id}/{id_libro}")
def datoslibro(id:int, id_libro:int):
    return usuarios[id - 1]["libros"][id_libro - 1]