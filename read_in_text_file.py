output_filename = "nombres.txt"

# read() permet de lire le fichier et de recuperer son contenu sous forme de texte
# readlines() permet de lire le fichier et de recuperer son contenu sous forme de collection (liste) dont
# chaque element correspond a une ligne du fichier
# readline() permet de lire une ligne a la fois. Cette fonction est generalement utilisee dans une boucle

with open(output_filename, 'r', encoding='utf-8', newline='') as output_file:
    text = output_file.read()
    print(text)
    text = output_file.readline()
    # le mot cle end permet de specifier quel caractere termine la ligne lue
    # par defaut, la fonction print() ajoute un \n a la fin de chaque ligne lue
    print(text, end="")