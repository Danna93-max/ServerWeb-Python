from fastapi import FastAPI
import json
# Crear una instància de la aplicación FastAPI
app = FastAPI()
#Funció per carregar les dades dels alumnes des d'un fitxer JSON
def carregar_dades():
    try:
        with open("alumnes.json", "r") as fitxer:
            return json.load(fitxer)
    except FileNotFoundError:
        # Si el fitxer no existeix, retornem una llista buida
        return []
# Carregar les dades dels alumnes al iniciar l'aplicació
alumnes = carregar_dades()

#Ruta principal al inici de l'aplicació
@app.get("/")
def home():
    return "Institut TIC de Barcelona"

# Ruta per obtenir la llista d'alumnes
@app.get("/alumnes/")
def total_alumnes():
    return {"total": len(alumnes)}

# Ruta per obtenir un alumne per ID
@app.get("/id/{numero}")
def obtenir_alumne(numero: int):
    for alumne in alumnes:
        if alumne["id"] == numero:
            return alumne
    return {"error": "Alumne no trobat"}

# Ruta per eliminar un alumne per ID
@app.delete("/del/{numero}")
def eliminar_alumne(numero: int):
    global alumnes
    # Filtrar la llista d'alumnes per eliminar l'alumne amb el ID especificat
    alumnes = [a for a in alumnes if a["id"] != numero]
    # Guardar els canvis al fitxer JSON
    with open("alumnes.json", "w") as fitxer:
        json.dump(alumnes, fitxer, indent=4)
    return {"resultat": "Alumne eliminat"}

# Ruta per afegir un nou alumne
@app.post("/alumne/")
def afegir_alumne(alumne: dict):
    global alumnes
    # Calcular un nou ID per l'alumne sumant 1 al màxim ID existent
    nou_id = max([a["id"] for a in alumnes], default=0) + 1
    alumne["id"] = nou_id
    alumnes.append(alumne)
    # Guardar els canvis al fitxer JSON
    with open("alumnes.json", "w") as fitxer:
        json.dump(alumnes, fitxer, indent=4)
    return {"resultat": "Alumne afegit", "id": nou_id}

