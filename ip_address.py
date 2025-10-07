import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connecté au broker !")
        try:
            peer = client._sock.getpeername()
            print(f"Broker connecté sur {peer}")  # Affiche le tuple complet
        except Exception as e:
            print("Impossible de récupérer l'adresse du broker :", e)
    else:
        print("Échec de la connexion, code :", rc)

client = mqtt.Client()
client.on_connect = on_connect

client.connect("localhost", 1883, 60)
client.loop_start()

import time
time.sleep(2)
client.loop_stop()