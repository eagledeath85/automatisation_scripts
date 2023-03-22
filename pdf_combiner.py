# Lire des fichiers PDF et extraire le texte
# Ecrire des PDF
#   - Combiner
#   - Rotation de pages, superposer des pages
#   - Ne peut pas : rajouter du texte ou des images

from PyPDF2 import PdfFileWriter, PdfFileReader

# Creation d'un pdf vide
contenu_de_sortie = PdfFileWriter()

fichier_pdf_presentation = open('presentation.pdf', 'rb')  # rb est l'option pour "read binary" car le pdf est un format binaire
fichier_pdf_recap = open('recap.pdf', 'rb')

reader_presentation = PdfFileReader(fichier_pdf_presentation)
reader_recap = PdfFileReader(fichier_pdf_recap)

# Obtenir le nombre de pages
print(f"Nombre de pages du fichier recap : {reader_recap.getNumPages()}")

# Obtenir une page specifique
contenu_page = reader_presentation.getPage(0)

# Ajout de cette page dans le contenu de sortie
contenu_de_sortie.addPage(contenu_page)
for i in range(reader_recap.getNumPages()):
    contenu_de_sortie.addPage(reader_recap.getPage(i))


# Ajout du contenu de sortie dans le fichier de sortie
    # Ouverture du fichier de sortie
fichier_sortie = open('fichier_sortie.pdf', 'wb')   # wb est l'option pour "write binary" car le pdf est un format binaire
    # Ecriture du contenu de sortie dans le fichier de sortie
contenu_de_sortie.write(fichier_sortie)

# Fermeture de tous les fichiers
fichier_sortie.close()
fichier_pdf_presentation.close()
fichier_pdf_recap.close()