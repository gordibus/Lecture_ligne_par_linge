#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 18:31:52 2022

@author: gordibus
"""

import glob 
for path in glob.glob("../DATA/*"):
    print (path)
mode_path = "../DATA/def_dictature.txt"
file = open ("../DATA/def_dictature.txt", "r")
line = file.readline()
while line:
    print(line)
    line = file.readline()
file.close()
while True:
    reponse = input("Voulez vous lire le texte ligne par ligne ?(O/N): ")
    if reponse == "N":
        break
    else:
        with open (mode_path) as file:
            for line in file:
                print (line)
                for word in line.split():
                    # Afficher chaque mot           
                    print(word)
                  
file.close()
                            
