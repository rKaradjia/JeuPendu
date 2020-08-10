#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

import pickle
import operator
import os
import random
from donnees import *

def getmot():
	dico={}
	print("Chargement du dictionnaire en cours...")
	i=0
	with open("dico.txt","r") as f:
		for line in f.readlines():
			dico[i]=(line.split("\n")[0])
			print(dico[i])
			i+=1
	print("Le dico" ,dico)	
	print("Un mot au hasard")	
	ran=random.randint(1,323577)		
	mot=dico[ran]
	return mot
			

	

def getliste():
	get=open("dico.txt","r")
	#Utilisation des séquences
	data=[line.split() for line in get]	
	#print(data)
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
				element = line.split(":")
				cletemp = element[0].split("\t")
				print("CLE",cletemp)
				if len(cletemp)>1:
					#Cela veut dire que la premiere 
					#ligne est ignore
					#verif=("".join(cle)).replace(" ","")
					cle=cletemp[1].replace("\"","")
					print("VERIF",cletemp[1])
				else:
					trait="".join(cletemp).split(" ")
					#On ignore les premiers espaces
					cle=(trait[4]+" "+trait[5]).replace("\"","")
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



def findmot(mot,motcache):
	i=0
	while i<donnees.nbchance:
		lettre=input("saisir lettre")
		if len(lettre)>1:
			print("Une lettre à la fois")		
		else:
			trouver = lambda mot, lettre: [i for i, car in enumerate(mot) if car==lettre]
			if len(trouver)>1:
				for pos in trouve:
					print("Remplace")
					motcache[pos]=lettre
			i+=1
			if motcache==mot:
				break;	










