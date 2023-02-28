# -------------------- FILE NOT FOUND ERROR HANDLING --------------------
import os.path

# La gestion de cette erreur peut etre faite de 2 manieres differentes
# try / except
# test chemin du fichier

filename = "nombres.txt"

# Test chemin du fichier
if os.path.exists(filename):
    print("Le fichier existe")
    f = open(filename, 'r', encoding='utf-8', newline='')
    text = f.read()
    print(text)
    f.close()
else:
    print("Le fichier n'existe pas")


# Try / Except
try:
    with open(filename, 'r', encoding='utf-8', newline='') as file:
        texte = file.read()
        print(texte)
except FileNotFoundError:
    print("ERREUR: Le fichier est introuvable")
