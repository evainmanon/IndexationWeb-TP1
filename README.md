# TP 1 - Construire un crawler minimal
EVAIN Manon 

## Éxecuter le code permettant d'enregistrer le fichier avec les url visités. 

#### 1. Cloner le dépot Git
Dans l'éditeur de code de votre choix, ouvrez le dossier dans lequel vous souhaitez enregistrer les fichiers pour le TP.  
Ouvrez par la suite un terminal. 

Vous pouvez alors écrire la ligne de code suivante :  

``git clone https://github.com/evainmanon/IndexationWeb-TP1.git``

#### 2. Exécuter le fichier main
Afin d'exécuter le fichier, c'est à dire d'obtenir un fichier texte comportant la liste des 50 sites trouvés grâce au crawler.  

Pour cela, vous pouvez écrire dans le terminal la ligne de code suivante : 

``python3 main.py``

*Les changements de paramètres* 

Afin d'exécuter ce crawler, vous pouvez faire le choix de changer deux paramètres. Ces derniers se trouvent dans le fichier main.py.   
- *url_essai* : Il s'agit d'une chaine de caractère comprenant l'url du site pour lequel vous souhaitez utiliser votre crawler.  
- *nb_site* : Ce paramètre permet de déterminer le nombre de site que le crawler va parcourir avant de s'arrêter. Il s'agit donc du nombre de lignes qui seront présente dans le fichier **crawled_webpages.txt**. 

## Explications du code

#### 1. Architecture du code
Ce dépot Git comprends 4 fichiers comprenant le code du crawler ainsi que des fichiers permettant de comprendre le résultat du code ou encore comment est-il possible de le lancer. L'explication de ces 4 fichiers est présentée ci dessous :   
- **main.py** : Ce fichier est un fichier python qui permet l'éxécution de la fonction créant le fichier texte contenant les pages qui ont été visitée par le crawler. Ce fichier permet également de faire la sélection des différents paramètres explicité auparavant.   
- **fonction.txt** : Ce fichier est un fichier python comprenant les différentes fonction nécessaire à la création de la fonction finale permettant de créer le fichier .txt regroupant les différentes url des sites web qui ont été parcourcues pendant le crawl de la page. Le code de ce fichier est commenté, ce qui permet une compréhension linéaire du code.  
- **README.MD** : Ce fichier est le fichier dans lequel nous retrouvons les différentes informations permettant de lancer le code sur sa machine mais également les informations sur le code.  
- **crawled_webpages.txt** : Ce fichier est un exemple de fichier créé par lors du lancement du fichier **main.py**. Il s'agit des pages visitées par le crawler lorsque les paramètres d'entrée sont 
    - url_essai = "https://ensai.fr/"
    - nb_sites = 50  

#### 2. Explications des choix réalisés 

##### a - L'exception RunTimeError 
Lors de l'exécution du crawler, nous avons remarqué que certains sites générait une erreur. En effet, le temps de réponse du site était trop long pour notre machine. Dans ce cas, l'éxécution du code s'arrétait. Afin de remédier à ce problème, nous avons insérer dans la fonction *recuperer_lien* un try/Except.   
Pour chaque site présent dans le fichier robots.txt, nous vérifions que le temps de réponse est inférieur au temps de réponse maximal avant l'erreur. Si le temps de réponse est bien inférieur à ce temps, on ajoute l'url du site à la liste des liens à visiter. En revanche, si ce temps de réponse est supérieur au temps défini, nous n'ajoutons par l'url à la liste des url que le crawler devra parcourir. 

##### b - La fonction can_fetch
Afin de vérifier si nous avons les droits pour accéder au site web, nous faisons appel à la fonction *can_fetch* qui permet de savoir si l'utilisateur '*' à les droits pour ouvrir ce site web. Si l'utilisateur a effectivement les droits pour accéder à ce site, la fonction ajoute l'url de ce site web à la liste des liens à visiter. En revanche, afin de respecter la politesse informatique, une site auquel nous ne pouvons pas accéder n'est pas ajouter dans la liste des sites web à visiter. 