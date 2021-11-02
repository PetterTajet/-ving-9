#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 15:54:03 2021

@author: pettertajet
"""

class Question:
    def __init__(self,spørsmål,fasit,forslag):
        self.spørsmål=spørsmål
        self.fasit= fasit
        self.forslag = forslag
        
    def __str__(self):
        
        x=0
        mulighet= ""
        for i in self.forslag:
            mulighet += "\n" + str(x) + ":" + i
            x+=1
        
        return f"{self.spørsmål} {mulighet}"
    
    def sjekk_svar(self,svar):
        #print("hva er svaret ditt?")
        
       
        if svar == self.fasit:
            print("dette er riktig")
            return True
        else: 
            print("dette var feil riktig er {self.forslag[self.fasit]}" )
            return False
            
    
    def korrekt_svar_tekst(self):
        return f"riktig svar er {self.forslag[self.fasit]}"
    
    

    
    

        
liste_spm = list()
txt = open("/Users/pettertajet/Documents/Universitetet stavanger/Dat120/Python/sporsmaalsfil.txt","r",encoding=("UTF8"))
for line in txt:
    line = line.strip()
    line =  line.split(":")
    spørsmål = line[0]
    fasit = int(line[1])
    forslag= line[2]
    forslag= forslag.strip()
    forslag = forslag.strip("[]")
    forslag= forslag.strip()
    forslag = forslag.split(",")
    liste_spm.append(Question(spørsmål, fasit, forslag))
    

if __name__=="__main__":   
    poeng1 = 0
    poeng2 = 0
    for spm in liste_spm:
        print(spm)
        spiller1 = int(input("spiller1 svar: "))
        spiller2 = int(input("spiller2 svar: "))
        if spm.sjekk_svar(spiller1) == True:
            poeng1 += 1
        if spm.sjekk_svar(spiller2) == True:
            poeng2 += 1
            
    print(f"spiller1 {poeng1}")
    print(f"spiller2 {poeng2}")
            
            
            

     
            
        
 

  