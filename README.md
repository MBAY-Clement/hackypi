# HackyPi Scripts 🔥

Bienvenue sur HackyPi Scripts, un ensemble de scripts dédiés à l'extraction et au déchiffrement de mots de passe stockés localement sur un système. Ces scripts sont conçus pour être exécutés à partir d'une clé HackyPi, permettant d'automatiser la récupération de données sensibles depuis des logiciels couramment utilisés (https://shop.sb-components.co.uk/products/hackypi-compact-diy-usb-hacking-tool).

🔹 Ce script permet d'extraire les fichiers de profil Firefox et d'en récupérer les mots de passe enregistrés. <br>
🔹 Il fonctionne en copiant les bases de données SQLite et les fichiers de chiffrement associés, puis en les exploitant pour afficher les identifiants stockés.


# 🦊 Dump Firefox Profile – Extraction des mots de passe

🔹 Ce script permet d'extraire via deux clés USB les fichiers de profil Firefox présents sur le poste.

Une fois extrait nous utilisons le projet github https://github.com/unode/firefox_decrypt pour déchiffrer les mots de passe présents sur les profils. 

![image](https://github.com/user-attachments/assets/fdb813b8-ed76-4d35-af9d-ecb21ebcf247)


Les fichiers du profil se retrouvent sur le chemin : <br> C:\Users\<NomUtilisateur>\AppData\Roaming\Mozilla\Firefox\Profiles

Fonctionnement du script : 
 - Une clé USB HackyPI qui va permettre d'executer le code powershell
 - Une clé USB "HACK" qui va permettre de récuperer les fichiers extraits.


# 🛠️ mRemoteNG dump du fichier ConfCons.xml 

🔹 Ce script cible l’application mRemoteNG, un gestionnaire de connexions RDP, SSH, et autres protocoles.
🔹 Il récupère le fichier de configuration ConfCons.xml, qui contient les identifiants stockés pour les connexions distantes.

Le fichier Conf.Cons.xml se trouve sur le chemin : C:\Users\<user>\AppData\Roaming\mRemoteNG

Fonctionnement du script : 
 - Une clé USB HackyPI qui va permettre d'executer le code powershell
 - Une clé USB "HACK" qui va permettre de récuperer le fichier extrait.

Une fois le fichier extrait et copié sur la clé USB "HACK", nous utilisons le projet github https://github.com/haseebT/mRemoteNG-Decrypt pour déchiffer un mot de passe présent dans un le fichier ConfCons.xml

![image](https://github.com/user-attachments/assets/ade95673-75dc-4445-bb40-ead13cdf4cf6)



