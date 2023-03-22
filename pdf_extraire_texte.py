# EXTRAIRE LE TEXTE DES FICHIERS PDF
from PyPDF2 import PdfFileReader, PdfFileWriter

f = open('recap.pdf', 'rb')
reader = PdfFileReader(f)

# Obtenir une page specifique
page0 = reader.getPage(0)

# Extraire le texte de cette page
texte = page0.extractText()
# print(texte)

# Remplacer les caracteres mal decodes
# On remplace au cas par cas avec la methode replace()
texte = texte.replace("Ò", '"').replace("‘", "è").replace("‹", "à").replace("”", "é").replace("Õ", "'")
print(texte)
f.close()