import csv
import pandas as pd
import os
from datetime import datetime

# Donnée reçue par le rdk chaque 5min

# Nom du fichier CSV
fichier1 = "positions.csv"
fichier2 = "positions_b.csv"
fichier = ""

if 1>0:
    fichier = fichier1
else:
    fichier = fichier2
    
if not os.path.exists(fichier):
    with open(fichier, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Time", "Latitude", "Longitude", "Photo"])

def ajouter_point(latitude, longitude, photo_path=None):

    temps = datetime.now().strftime("%Y-%m-%d %H:%M")

    if photo_path is None:
        photo_path = ""

    with open(fichier, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([temps, latitude, longitude, photo_path])


ajouter_point(48.8566, 2.3522, "photos/paris.jpg") 