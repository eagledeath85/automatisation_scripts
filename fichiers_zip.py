import zipfile
import shutil

# Creation du fichier zip. Le parametre ZIP_DEFLATED active la compression
fichier_zip = zipfile.ZipFile("fichiers_excel.zip", 'w', zipfile.ZIP_DEFLATED)

# Ajout de fichiers dans le fichier zip
fichier_zip.write("octobre.xlsx")
fichier_zip.write("novembre.xlsx")
fichier_zip.write("decembre.xlsx")

# Fermeture du fichier zip
fichier_zip.close()


# Pour creer un fichier zip a partir d'un repertoire, on peut utiliser la utils shutil
# make_archive("nom_du_fichier_zip", "type_de_compression", "repertoire_ou_se_situent_les_fichiers")
shutil.make_archive("fichiers_excel_2", "zip", "fichiers_excel")

# Pour dezipper un fichier zip on peut utiliser la fonction unpack_archive("nom_du_fichier_a_dezipper", "nom_du_repertoire")
shutil.unpack_archive("fichiers_excel_2.zip", "extraction_zip")