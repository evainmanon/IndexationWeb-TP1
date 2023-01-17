#Import nécessaire au fonctionnement du code
from urllib import robotparser as rb
from bs4 import BeautifulSoup
from time import sleep

import requests
import itertools

#Fonction qui récupère la liste des liens accessibles dans une page
def recuperer_liens(url):

    liens=[]
    try:
        site_test= requests.get(url)
        site = BeautifulSoup(site_test.text, 'html.parser')

        #Lecture du /robots.txt
        robots = rb.RobotFileParser()
        robots.set_url(url)
        robots.read()

        for link in site.find_all('a'):
            href = link.get('href')
            if href != None: 
                if href[0:4]=='http' and robots.can_fetch("*", href):
                    liens.append(href)
        return liens
    except RuntimeError:
        return []
       
#Fonction qui parcours les différents liens 
def crawler(url, nb_site): 
    liste_lien_a_parcourir = [url]
    liste_lien_parcouru = []
    while len(liste_lien_a_parcourir)!= 0 and len(liste_lien_parcouru)<nb_site :
        liste_lien_a_parcourir = list(itertools.chain(liste_lien_a_parcourir, recuperer_liens(liste_lien_a_parcourir[0])))
        liste_lien_parcouru.append(liste_lien_a_parcourir.pop(0))
        sleep(5)
    return liste_lien_parcouru

#Fonction qui crée le fichier .txt
def creation_fichier(url, nb_site):
    liste_lien = crawler(url, nb_site)
    file = open("crawled_webpages.txt", "w") 
    for lien in liste_lien : 
        file.write(lien + "\n") 
    file.close()
    return None