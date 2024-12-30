from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    Fonction pour lire la liste des librairies à installer
    """
    try:
        with open(file_path, "r", encoding="utf-8") as fichier:
            requirements = fichier.readlines()
            requirements = [ligne.replace("\n","") for ligne in requirements]

            if "-e ." in requirements :
                requirements.remove("-e .")
            
            return requirements

    except FileNotFoundError:
        print("Fichier introuvable.")
    


setup(
    name = "Projet data mining système de recommandation",
    version = "0.0.1",
    author = "Achour",
    author_email = "achoursimoud@gmail.com",
    packages = find_packages(),
    install_requirements = get_requirements("requirements.txt")

)