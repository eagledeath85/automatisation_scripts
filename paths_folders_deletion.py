import os.path


# La fonction os.path.join(args1, args2, ...) permet de construire un chemin a partir des elements passes en argument
filename = os.path.join("rep", "my_file.txt") # path = rep/myfile.txt pour Linux et macOS // path = rep\myfile.txt pour Windows
print(filename)


# La fonction os.mkdir() permet de creer un repertoire
os.mkdir("folder_path or folder_name")

# La fonction os.rmdir() permet de supprimer un repertoire
os.rmdir("folder_path or folder_name")

# La fonction os.remove() permet de supprimer un fichier
os.remove("file path or file_name")