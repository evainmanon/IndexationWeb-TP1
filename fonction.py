#Import nécessaire au fonctionnement du code
from urllib import robotparser as rb
from bs4 import BeautifulSoup
from time import sleep

import requests
import itertools



#Fonction qui récupère la liste des liens accessibles dans une page
def recuperer_liens(url):

    #Création de la liste des liens qui sont sités par une page web 
    liens=[]

    try:
        site_test= requests.get(url)
        site = BeautifulSoup(site_test.text, 'html.parser')

        #Lecture du /robots.txt
        robots = rb.RobotFileParser()
        robots.set_url(url)
        robots.read()

        #Pour chaque liens présents dans le fichier robots.txt, on vérifie que le lien n'est pas vide d'une part et d'une autre part.
        #On vérifie également pour chaque si que l'url commence bien par 'http' et que l'utilisateur à les droits pour accéder à ce site web. 
        for link in site.find_all('a'):
            href = link.get('href')
            if href != None: 
                if href[0:4]=='http' and robots.can_fetch("*", href):
                    liens.append(href)
        
        #Si il n'y a pas d'erreur, la fonction renvoies la liste des 'bons' liens présents dans le fichier robots.txt
        return liens

    except RuntimeError:

        #Si le temps de réponse du site web est trop long, la fonction renvoie une liste vide. 
        return []



#Fonction qui parcours les différents liens 
def crawler(url, nb_site): 

    #Initialisation de deux listes, la première contenant les sites à parcourir et la seconde, la liste des liens qui ont été parcourus. 
    liste_lien_a_parcourir = [url]
    liste_lien_parcouru = []

    #On réalise une boucle while sur la taille des listes. Soit nous avons parcouru tous les sites web, soit nous avons atteints le nombre de sites que nous souhaitons dans notre fichier final.
    while len(liste_lien_a_parcourir)!= 0 and len(liste_lien_parcouru)<nb_site :

        #On ajoute à la liste des liens à parcourir les liens présents dans le fichier robots.txt du premier élément de cette dernière liste. 
        liste_lien_a_parcourir = list(itertools.chain(liste_lien_a_parcourir, recuperer_liens(liste_lien_a_parcourir[0])))

        #On enlève le premier élément de la liste des liens à parcourir et on ajoute ce dernier à la liste des liens parcourus.
        liste_lien_parcouru.append(liste_lien_a_parcourir.pop(0))

        #On ajoute un délai de 5 secondes
        sleep(5)

    #La fonction renvoie la liste des liens qui a été parcourue par le crawler
    return liste_lien_parcouru



#Fonction qui crée le fichier .txt
def creation_fichier(url, nb_site):

    #On utilise la fonction crawler afin de déterminer la liste des liens qui ont été visités 
    liste_lien = crawler(url, nb_site)

    #Création du fichier .txt contenant l'ensemble des url des sites visités par le crawler. On saute une ligne entre chaque url (\n). 
    file = open("crawled_webpages.txt", "w") 
    for lien in liste_lien : 
        file.write(lien + "\n") 
    file.close()

    return None