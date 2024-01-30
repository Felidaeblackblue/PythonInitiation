import platform
import socket
from pathlib import Path
import psutil
import os
import time

# Informations sur le système
# print("Nom d'hôte :", socket.gethostname())
# print("Adresse IP :", socket.gethostbyname(socket.gethostname()))
# print("Architecture du processeur :", platform.machine())
# print("Version du système d'exploitation :", platform.version())


#Liste des fichiers
# def list_files_and_sizes(directory):
#     path = Path(directory)
#     files = path.iterdir()
#     for file in files:
#         if file.is_file():
#             size = file.stat().st_size
#             print(f"{file.name}: {size} bytes")

# directory_path = "../Python"
# list_files_and_sizes(directory_path)


# # Obtenir des informations sur la mémoire
# mem_info = psutil.virtual_memory()

# # Afficher l'utilisation de la mémoire
# print('Mémoire totale :', mem_info.total)
# print('Mémoire disponible :', mem_info.available)
# print('Mémoire utilisée :', mem_info.used)
# print('Pourcentage d\'utilisation de la mémoire :', mem_info.percent)



#shutil
import shutil

# Récupérer l'espace disque
total, used, free = shutil.disk_usage("/")

# Afficher les informations
print(f"Espace disque total : {total / (2**30):.2f} Go")
print(f"Espace disque utilisé : {used / (2**30):.2f} Go")
print(f"Espace disque disponible : {free / (2**30):.2f} Go")

