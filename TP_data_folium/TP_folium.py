#!/usr/bin/env python
# coding: utf-8

# Avant de faire ce TP, il est important de créer un dossier dans lequel vous allez sauvegarder ce notebook

# ## Carte sur folium

# ### Une carte simple

# https://pixees.fr/informatiquelycee/n_site/snt_carto_osmPerso.html
# 
# Nous allons utiliser les cartes proposées par Open Street Map et le langage Python afin de générer des cartes personnalisées. Plus exactement, nous allons utiliser une bibliothèque Python nommée Folium. Une bibliothèque Python permet de rajouter des fonctionnalités au langage de base. Folium va donc nous permettre de créer nos propres cartes à partir des cartes proposées par Open Street Map. 
# 
# 
# 1. Exécutez le code suivant

# In[ ]:


import folium
c= folium.Map(location=[46.078025, 6.409053])
c.save('maCarte.html')


# puis regardez dans le dossier, un nouveau fichier est apparu. Qu'est-ce qui a permi de créer ce fichier ? 

# > la fonction save "..html" qui sauvegarde le résultat de c ! 

# 
# 2. Double-cliquez sur ce nouveau fichier. Quel est le programme qui permet de l'ouvrir et pourquoi ?  

# > l'extension html s'ouvre avec un explorateur internet. 

# Le fichier maCarte.html fait apparaître une une véritable carte et pas une simple image (il est possible de zoomer ou de se déplacer mais pour cela il faut une connexion à internet ! ). 
# 
# 3. Sur quelle ville est-elle centrée ? Quelles sont ses coordonnées GPS ? Comment pouvez-vous relier ces coordonnées au programme ci-dessus ? 

# > Bonne   Latitude/Longitude

# Le programme est simple à comprendre :
# 
# La première ligne : "import folium" permet d'importer la bibliothèque folium afin de pouvoir l'utiliser.
# 
# La deuxième ligne est le coeur de notre programme, nous définissons une variable "c" qui va contenir notre objet carte. "folium.Map(location=[46.078025, 6.409053])" génère cet objet carte, la carte sera centrée sur le point de latitude "46.078025" et de longitude "6.409053". Plus généralement nous avons "folium.Map(location=[latitude, longitude])". Il suffit donc de renseigner la bonne longitude et la bonne latitude pour que la carte soit centrée sur le point désiré.
# 
# La dernière ligne permet de générer la page HTML qui va permettre d'afficher la carte.
# 
# 4. Quelles sont les coordonnées GPS de Lorient ? 
# Créez une carte avec folium centrée sur Lorient (vous pouvez changer le nom de la carte).
# 

# > Lorient (47.75, -3.3667)   Latitude/Longitude
# 
# import folium
# c= folium.Map(location=[47.745, -3.667])
# c.save('maCarte.html')
# 

# In[ ]:


import folium
c= folium.Map(location=[47.7512, -3.3931])
c.save('maCarte.html')


# 5. Exécutez le programme suivant et ouvrez le fichier maCarte.html (ou alors rafraîchissez la page maCarte.hmtl dans votre nagivateur en appuyant sur F5)

# In[ ]:


import folium
c= folium.Map(location=[47.7512, -3.3931],zoom_start=15)
c.save('maCarte.html')


# 6. Où se situe-t-on ? 
# Que permet de faire le paramètre zoom_start ? (pour cela, changez sa valeur et réactualisez votre carte)

# > Lorient, au dessus du Lycée quasiment
# 
# > zoom initial

# ### Amélioration de la carte

# 7. Saisissez et testez le programme ci-dessous 

# In[ ]:


import folium
c= folium.Map(location=[47.7512,-3.3931],zoom_start=20)
folium.Marker([47.751,  -3.3924]).add_to(c)
c.save('maCarte.html')


#  Nous avons uniquement ajouté la ligne "folium.Marker...", il faut juste renseigner les coordonnées souhaitées (ici 47... pour la latitude et -3.3.. pour la longitude)
# 
# Il est possible d'ajouter plusieurs marqueurs sur une même carte, il suffira d'ajouter autant de ligne "folium.Marker([latitude, longitude]).add_to(c)" que de marqueurs désirés.
# 
# Il est possible d'associer une information à un marqueur en ajoutant le paramètre "popup" : 
# 
# 8. Saisissez et testez le programme ci-dessous 

# In[ ]:


import folium
c= folium.Map(location=[47.7512,-3.3931],zoom_start=20)
folium.Marker([47.751,  -3.3924],popup="Vous êtes ici ! ").add_to(c)
c.save('maCarte.html')


# Il suffit de cliquer sur le marqueur pour que l'information définie par le paramètre "popup" apparaisse à l'écran (ici en cliquant sur le marqueur nous verrons donc apparaitre "Vous êtes ici ! "). 

# ## Lecture de fichier de données et affichage sur une carte via folium

# idées : 
# https://pixees.fr/informatiquelycee/n_site/snt_carto.html

# ### Création de votre propre carte ! 
# 
# On va commencer par créer un tableau qui va contenir les informations (longitude, latitude et description du lieu). 
# 
# 1. Regardez l'algorithme suivant, en lisant les commentaires, et rajoutez quelques lieux (maison, piscine, ...)
# 
# On pourra s'aider de sites comme https://www.gps-coordinates.net/ qui proposent une carte qui, en cliquant sur un point de la carte, nous propose les coordonnées GPS précises de ce lieu. 

# In[1]:


import pandas as pd   #Pandas est une librairie qui permet de créer des tableaux de données

# Création d'un tableau vide, ou plutôt une ligne vide, la ligne 0, avec 3 colonnes : 
donnees=pd.DataFrame(index=[0],columns={'Longitude','Latitude','Description'})  

#Dans la première ligne, numéro 0, on va remplir les cases par des données
donnees.at[donnees.index[0],'Latitude']=47.750908
donnees.at[donnees.index[0],'Longitude']=-3.392328
donnees.at[donnees.index[0],'Description']="Vous êtes ici ! " 

#On rajoute une ligne en y accollant (on concatène) une nouvelle ligne
donnees = pd.concat([donnees,pd.DataFrame(index=[1],columns={'Longitude','Latitude','Description'})],ignore_index=True)

#Que l'on remplit par des données
donnees.at[donnees.index[1],'Latitude']=47.750463
donnees.at[donnees.index[1],'Longitude']=-3.392504
donnees.at[donnees.index[1],'Description']="CDI" 

#On peut ainsi créer notre propre tableau avec autant de lignes que l'on souhaite

#On sauvegarde le tableau dans un fichier csv pour pouvoir l'envoyer aux amis par exemple
donnees.to_csv(r'monfichier2.csv',index=True)


# 2. Que signifie csv ? Où est le fichier monfichier2.csv ? 

# > coma separated value : séparé par une virgue

# On va maintenant afficher sur la carte les lieux que vous avez signalés : 

# In[3]:


import folium

#On créé une carte, ici centrée sur le lycée
c= folium.Map(location=[47.7512,-3.3931],zoom_start=20)


for i in range(0,donnees.shape[0]): # à chaque ligne du tableau, on lit la Longitude, Latittude et Description, que l'on place aux bons endroits du marker.
    folium.Marker([donnees.at[donnees.index[i],'Latitude'],donnees.at[donnees.index[i],'Longitude']],popup=donnees.at[donnees.index[i],'Description']).add_to(c)

c.save('maCarte.html')


# In[4]:


del donnees  # si on ne supprime pas le tableau, on occupe inutilement un tableau dans la RAM de votre 
            #ordinateur, ce qui pourrait le ralentir si le tableau est immense


# 3. Il est possible aussi de rajouter plus facilement des lieux. 
# 
# a) Pour cela, allez dans le répertoire où se situe le fichier monfichier2.csv, par un clic-droit, renommez-le en monfichier3.csv afin de sauvegarder ce que vous avez fait dans la question 1.  (Si vous ré-exécutez l'algo précédent alors que vous avez modifié le fichier monfichier2.csv autre part, alors ce fichier sera écrasé et remplacé par le fichier monfichier2.csv de l'algorithme)
# 
# b) Ouvrez ce fichier monfichier2.csv avec un tableur comme LibreOffice, puis rajoutez des lieux directement dans le tableau. N'oubliez pas de sauvegarder votre fichier en gardant toujours le format csv ! 
# 
# 
# 
# 4. Il faut maintenant que Python lise les détails de ce fichier, on va donc réutiliser la bibliothèque Pandas qui va prendre toutes les données du tableau du csv, et en faire un tableau identique sous Python : 

# In[ ]:


import folium #pas obligé de le remettre si on continue l'algorithme précédent, mais bien si vous recommencez 
                # de zero avec seulement un fichier csv
import pandas as pd  # idem 

data =pd.read_csv(r'monfichier3.csv')

#On créé une carte, ici centrée sur le lycée
c= folium.Map(location=[47.7512,-3.3931],zoom_start=20)


for i in range(0,data.shape[0]): # à chaque ligne du tableau, on lit la Longitude, Latittude et Description, que l'on place aux bons endroits du marker.
    folium.Marker([data.at[data.index[i],'Longitude'],data.at[data.index[i],'Latitude']],popup=data.at[data.index[i],'Description']).add_to(c)

c.save('maCarte.html')


# ### Exercice : positionnement des radars de France 

# Après avoir téléchargé dans le bon dossier le fichier des radars au format csv https://www.data.gouv.fr/fr/datasets/radars-automatiques/ , créez une carte qui recense les radars (en 2018) sur le morbihan seulement ! 
# 
# On pourra ouvrir le fichier cvs dans LibreOffice et trier les départements en s'aidant de https://help.libreoffice.org/Common/Sort_Ascending/fr  

# > L'intérêt n'est pas vraiment dans le programme car il est déjà créé plus haut, mais dans la sélection des données sur LibreOffice, qui peut s'avérer un peu compliqué car il faut trier la colonne des départements, copier les lignes pour les 56, coller dans le même doc ou bien dans fichier différent, ne pas oublier de renommer les colonnes, ... 

# In[ ]:




