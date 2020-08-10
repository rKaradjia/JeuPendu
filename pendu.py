#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

from fonctions import getliste
from donnees import *



continuer=""

while continuer != "q":
	print("START")

#getListe via donnees et fonctions
	get=getliste()
	print("La liste" , get)
	print(" lg ", len(get))
#print("hello")
#Saisir le nom d'un fichier
#fichierexiste()


#Saisir le nom d'un joueur
	saisir = input ("Nom du joueur ")
	print(" Nom du joueur ",saisir)
#Recuperer le dictionnaire A VOIRu
	dicoinit={}
	dico=createdico(dicoinit)
	print(dico)
	var=dico['joueur 2']
	print(var)

#Chercher nom --> fonction

	existe=joueurexiste(saisir,dico)
#creer le joueur dans le fichier

	if existe==False:
		dico[saisir]=0
	print("Verification ",dico["rehane"])

#Recherche d'un mot au hasard dans un fichier
	mot=getmot()
	motcache=getmotcache(mot)
	print("Le mot retourné " , mot)
	print("Le mot caché" , motcache)

	#Le joueur doit chercher le mot
	res=findmot(mot,motcache)
	print("Points ",res)
	print(dico)
	dico[saisir]=str(res)
	enregistrerdico(dico)
	continuer=input("Continuez? q pour quitter")
	


#Le tout tq nb chances
#boucle for sur la liste de ***
	#boucle sur le mot 
		#si lettre correcte
				#boucle tant que
		
#resultat




