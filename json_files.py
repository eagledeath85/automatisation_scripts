# ----------------- JSON, MANIPULER DES DONNEES STRUCTUREES -----------------
import json

# Personne
#   nom: str
#   age: int
#   amis: [str]

personnes = {
    "nom": "Paul",
    "age": 25,
    "amis": ["Farid", "Mouloud", "Jean"],
        }

filename = "fichier_json.txt"
# Serialiser DATA -> TXT "" (json): dumps
# Deserialiser TXT (json) -> DATA:  loads


# dumps() permet de convertir un element en json (on le serialise)
personne_json = json.dumps(personnes)
print(f"JSON cree : {personne_json}")

# On peut ensuite ecrire cette chaine de caractere dans un fichier
with open(filename, 'w', encoding='utf-8', newline='') as json_file_to_write:
    json_file_to_write.write(personne_json)


# loads() permet de lire un fichier json et le deserialiser en objets
# On ouvre le fichier
with open(filename, 'r', encoding='utf-8', newline='') as json_file_to_read:
    # On lit le contenu du fichier et on le stocke dans une variable
    donnees_json = json_file_to_read.read()
    # On deserialise le contenu de la variable et on recupere un dictionnaire dans notre cas
    personne = json.loads(donnees_json)
    print(f"DATA reconstituee : {personne}")
