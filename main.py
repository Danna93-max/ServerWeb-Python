from fastapi import FastAPI
import json

app = FastAPI()

def carregar_dades():
    try:
        with open("alumnes.json", "r") as fitxer:
            return json.load(fitxer)
    except FileNotFoundError:
        return []

alumnes = carregar_dades()

@app.get("/")
def home():
    return "Institut TIC de Barcelona"

@app.get("/alumnes/")
def total_alumnes():
    return {"total": len(alumnes)}

@app.get("/id/{numero}")
def obtenir_alumne(numero: int):
    for alumne in alumnes:
        if alumne["id"] == numero:
            return alumne
    return {"error": "Alumne no trobat"}

@app.delete("/del/{numero}")
def eliminar_alumne(numero: int):
    global alumnes
    alumnes = [a for a in alumnes if a["id"] != numero]
    with open("alumnes.json", "w") as fitxer:
        json.dump(alumnes, fitxer, indent=4)
    return {"resultat": "Alumne eliminat"}

@app.post("/alumne/")
def afegir_alumne(alumne: dict):
    global alumnes
    nou_id = max([a["id"] for a in alumnes], default=0) + 1
    alumne["id"] = nou_id
    alumnes.append(alumne)
    with open("alumnes.json", "w") as fitxer:
        json.dump(alumnes, fitxer, indent=4)
    return {"resultat": "Alumne afegit", "id": nou_id}

