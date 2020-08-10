#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

import pickle
import operator
import os
import random
import json
#from donnees import nbchance

def getmot():
	dico={}
	print("Chargement du dictionnaire en cours...")
	i=0
	with open("dico.txt","r") as f:
		for line in f.readlines():
			if len(line)<=8:
				dico[i]=(line.split("\n")[0])
				print(dico[i])
				i+=1
	print("Le dico" ,len(dico))	
	print("Un mot au hasard")	
	ran=random.randint(1,47637)		
	mot=dico[ran]
	return mot
			

	

def getliste():
	get=open("dico.txt","r")
	#Utilisation des séquences
	data=[line.split() for line in get if len(line)<=8]	
	return data


def fichierexiste():
	val=os.path.isfile("scores") # retourne vrai si le fichier ou le dossier existe
	if val == False:
		print("Creation du fichier ")
		open("scores","a")
         

def createdico(dicoinit):
	print("Creation du dictionnaire")
	with open("scores","r") as f:
		for line in f.readlines():
			if line.find(":")>=0:
				print("Ligne en cours " ,line)
				element = line.split(":")
				print(element)
				cletemp = element[0].split("\t")
				print("CLE",cletemp)
				cle=""
				if len(cletemp)>1:
					#Cela veut dire que la premiere 
					#ligne est ignore
					#verif=("".join(cle)).replace(" ","")
					cle=cletemp[1].replace("\"","")
					print("VERIF",cletemp[1])
				else:
					#print("cletemp2",cletemp)
					trait="".join(cletemp).split(" ")
					print(trait)
					i=4
					if i==len(trait):
						cle=trait[i]
					else:
						while i<len(trait):
							if i==len(trait)-1:
								cle+=trait[i]
							else:	
								cle+=trait[i]+" " 	
							i+=1
					#On ignore les premiers espaces
					#cle=(trait[4]+" "+trait[5]).replace("\"","")
					print("cle" , cle)
				#if cle[0]=="\t":
				#	temp=cle.split("\t")
				#	cle=temp[1]
				dataX = element[1].split(",\n")
				data1 = dataX[0].replace(" ","")
				data = data1
				print(cle ," ",data)
				dicoinit[cle]=data
	print(dicoinit)			
	return dicoinit			
				

def joueurexiste(joueur,dico):
	for cle in dico.keys():
		if cle==joueur:
			return True
		else:
			return False
	 			
#Genere le mot ********
def getmotcache(mot):
	#mottemp=mot.split("")
	#print(mottemp)
	liste=[]
	i=0
	while i < len(mot):
		print(mot[i])
		lettre=mot[i]
		liste.append("*")
		i+=1
	print(mot)
	motcache="".join(liste)
	print(motcache)		
	return motcache


#Fonction ou le joueur va chercher le mot
def findmot(mot,motcache):
	i=0
	motcacheliste=list(motcache)
	while i<=8:
		lettre=input("saisir lettre")
		if len(lettre)>1:
			print("Une lettre à la fois")		
		else:
			trouver = [pos for pos, char in enumerate(mot) if char == lettre]
			print("Liste " , trouver)
			if len(trouver)>=1:
				#motcacheliste=list(motcache)
				print("mot cache liste " ,motcacheliste)
				for pos in trouver:
					print("Remplace")
					motcacheliste[pos]=lettre
					print(motcacheliste)
			motcache="".join(motcacheliste)	
			print("A ce stade " ,motcache)
			i+=1
			if motcache==mot:
				#Calcul des points	
				print("Calculer les points")
				points=8-i
				return points
	#calcul de points
	print("Calculer les points")
	points=8-i
	return points


def enregistrerdico(dico):
	newfile=open("scores","w")
	dicoString=json.dumps(dico)
	print("Dictionnaire string ",dicoString)
	newfile.write("score = {\n")
	for cle, valeur in dico.items(): #Methode similaire celle des tuples
		type(cle)
		type(valeur)
		newfile.write("    "+cle+":    "+valeur+",\n")
		#print("La cle {} contient la valeur {}.".format(cle,valeur))
	newfile.write("}")
	



