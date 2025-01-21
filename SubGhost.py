import requests
import os
import sys
import time
import re
from pystyle import Colors, Colorate, Center
from sys import stderr

if os.name == "nt":  # Check if the OS is Windows
    os.system("cls")  # Clear the screen for Windows OS
else:
    os.system("clear")  # Clear the screen for Unix-like OS

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLEU = '\033[34m'


description = """
         .-.
       .'   `.          ----------------------------
       :g g   :         | GHOST - Finder Subdomain |  
       : o    `.        |       @CODE BY HackFut   |
      :         ``.     ----------------------------
     :             `.
    :  :         .   `.
    :   :          ` . `.
     `.. :            `. ``;
        `:;             `:' 
           :              `.
            `.              `.     . 
              `'`'`'`---..,___`;.-'

          """

banner = """
          #Contact : t.me/H4ckfutSec
          #Github  : https://github.com/HackfutSec
          #License : MIT  
          [Warning] I am not responsible for the way you will use this program [Warning]"""

print(Colorate.Horizontal(Colors.red_to_yellow, Center.XCenter(banner)))
print(Colorate.Horizontal(Colors.blue_to_green, Center.XCenter(description)))


def get_subdomains(domain):
    """
    Fonction qui récupère les sous-domaines d'un domaine en utilisant une API publique.
    Gère les erreurs de connexion et de réponse.
    """
    url = f"https://jonlu.ca/anubis/subdomains/{domain}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie si le code HTTP est 200
        subdomains = response.json()
        return subdomains
    except requests.exceptions.RequestException as e:
        print(bcolors.RED + f"\n[] Error fetching subdomains: {e}")
        return []

def save_subdomains_to_file(domain, subdomains, file_format='txt'):
    """
    Enregistre les sous-domaines dans un fichier. Permet de choisir le format d'exportation.
    """
    filename = f"{domain}_subdomains.{file_format}"
    try:
        if file_format == 'txt':
            with open(filename, 'w') as file:
                for subdomain in subdomains:
                    file.write(subdomain + "\n")
        elif file_format == 'csv':
            import csv
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                for subdomain in subdomains:
                    writer.writerow([subdomain])
        print(bcolors.GREEN + f"\n[] Subdomains saved to {filename}")
    except Exception as e:
        print(bcolors.RED + f"\n[] Error saving subdomains to file: {e}")

def validate_domain(domain):
    """
    Valide le domaine pour s'assurer qu'il a un format correct.
    """
    regex = r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
    if re.match(regex, domain):
        return True
    return False

def main():
    """
    Fonction principale qui permet à l'utilisateur de saisir un ou plusieurs domaines, 
    puis récupère et enregistre les sous-domaines.
    """
    domains_input = input(bcolors.YELLOW + "\n[] Enter the domain(s) (e.g., google.com or google.com,example.com): ")
    domains = [domain.strip() for domain in domains_input.split(',')]
    
    file_format = input(bcolors.YELLOW + "\n[] Choose file format (txt/csv): ").strip().lower()
    if file_format not in ['txt', 'csv']:
        print(bcolors.RED + "Invalid file format chosen. Defaulting to 'txt'.")
        file_format = 'txt'

    for domain in domains:
        if not validate_domain(domain):
            print(bcolors.RED + f"\n[] Invalid domain format: {domain}")
            continue
        
        print(bcolors.YELLOW + f"\n[] Searching for subdomains of {domain}...")
        subdomains = get_subdomains(domain)
        if subdomains:
            save_subdomains_to_file(domain, subdomains, file_format)
        else:
            print(bcolors.RED + f"\n[] No subdomains found or error occurred for {domain}.")
        
        time.sleep(2)  # Délai entre les requêtes pour éviter un envoi excessif

if __name__ == "__main__":
    main()
