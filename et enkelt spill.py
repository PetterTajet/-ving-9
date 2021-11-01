#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 08:51:37 2021

@author: pettertajet
"""


class sporsmol:
    def __init__(self, sporsmolstekst, liste_med_svaralternativ, riktig_alternativ):
        self.sporsmolstekst = sporsmolstekst
        self.liste_med_svaralternativ = liste_med_svaralternativ
        self.riktig_alternativ = riktig_alternativ 
    def __str__(self):
        return(print(f"{self.sporsmolstekst}" +"\n" "velg et alternativ " f"{self.liste_med_svaralternativ}"))
    def sjekk_svar (self):
        svar= int(input("ditt valg: "))
        if svar == self.riktig_alternativ:
            print("Riktig svar")
        else:
            print("Feil svar: ")
            
sporsmol_1 = sporsmol("hvem er styggest? svar med tall. ", ["Erna solberg = 0", "Megan fox = 1", "Margot robbie = 2", "Madison beer = 3"] , 0)
sporsmol_2 = sporsmol("hva er 3+3? svar med tall",["12 = 0","10 = 1","9 = 2","99 = 3"],2)

sporsmol_1.__str__()
sporsmol_1.sjekk_svar()

sporsmol_2.__str__()
sporsmol_2.sjekk_svar()
        
    
    