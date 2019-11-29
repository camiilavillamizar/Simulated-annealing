import string, math
import random
from decimal import *
import os
import copy
import numpy

####### DATOS ########
nombres = []
nombres = ['Deprisa Crespo',
           'Edificio Eliana (Crespo) 1',
           'Joyeria Caribe (Centro) 2',
           'Edificio Tramontana (Crespo) 3',
           'Casa Del Marques De Valdehoyos (Centro) 4',
           'Edificio Taurus (Manga 5)',
           'Terrazas De San Sebastian (Marbella) 6',
           'Edificio Bambu (Manga) 7',
           'Hotel Atuchi (Crespo) 8',
           'Torre Caribe 1 (Bocagrande) 9',
           'Edificio Las Tres Calaberas (Bocagrande) 10',
           'La Casa Del Marquez (Manga) 11',
           'Edificio Platino (Bocagrande) 12',
           'Poseidon Del Caribe (Bocagrande) 13',
            'Edificio El Faraon (Manga) 14',
           'Balcones De Crespo (Crespo) 15',
           'Los Cedros De Manga (Manga) 16',
           'Libreria Nacional (Centro) 17',
            'Edificio Antonela (Manga) 18',
           'Edificio Marina Mar (Manga) 19',
           'Edificio Valenty (Manga) 20']
datos = []
    #Distancias en metros
datos = [
        #Deprisa crespo
[0, 750, 6400, 1200, 6300, 7500, 3800, 7600, 1100, 8200, 9100, 7300, 9100, 10200, 7300, 1400, 7600, 5500, 7800, 6800, 7100],
        #Edificio Eliana
[750, 0, 6200, 450, 6100, 6800, 3100, 6900, 800, 7500, 8400, 6600, 8400, 9500, 6600, 1000, 6900, 4800, 7100, 6100, 6400],
        #Joyeria Caribe
[6400, 6200, 0, 5000, 450, 4900, 3400, 5100, 5400, 2900, 3700, 4700, 3800, 4800, 5800, 5400, 5100, 750, 5200, 4200, 4600],
        #Edificio tramontana
[1200,450, 5000, 0, 5700, 5600, 2700, 6500, 1000, 7100, 8000, 6200, 8000, 9100, 6200, 1000, 5800, 4400, 6600, 5700, 6000],
        #Casa Del Marques De Valdehoyos
[6300,6100, 450, 5700, 0, 5200, 3700, 5300, 5700, 3200, 4100, 5000, 4200, 5200, 5000, 5700, 5300, 1100, 5400, 4500, 4800],
        #Edificio Taurus
[7500, 6800, 4900, 5600, 5200, 0, 4400, 500, 6400, 4800, 5700, 1000, 5800, 6800, 600, 6400, 180, 3100, 1000, 1500, 1600],
        #Terrazas De San Sebastian
[3800, 3100, 3400, 2700, 3700, 4400, 0, 5800, 2000, 8200, 9100, 5700, 9100, 10200, 5900, 2000, 5500, 4500, 5600, 5400, 5700 ],
        #Edificio Bambu
[7600, 6900, 5100, 6500, 5300, 500, 5800, 0, 6300, 4800, 5700, 500, 5700, 6800, 100, 6300, 300, 3100, 550, 1100, 1100],
        #hotel Atuchi
[1100, 800, 5400, 1000, 5700, 6400, 2000, 6300, 0, 7500, 8500, 6600, 8500, 9500, 6600, 220, 6200, 4800, 7100, 6100, 6400],
        #Torre caribe 1
[8200, 7500, 2900, 7100, 3200, 4800, 8200, 4800, 7500, 0, 950, 3300, 1000, 2000, 4700, 7700, 5300, 3600, 5200, 4200, 4500],
        #Edificio las tres calaberas
[9100, 8400, 3700, 8000, 4100, 5700, 9100, 5700, 8500, 950, 0, 7000, 2500, 1000, 7000, 9900, 7600, 5800, 7400, 6500, 6800],
        #La casa del marquez
[7300, 6600, 4700, 6200, 5000, 1000, 5700, 500, 6600, 3300, 7000, 0, 5500, 6500, 500, 6400, 700, 3100, 600, 1100, 550],
        #Edificio platino
[9100, 8400, 3800, 8000, 4200, 5800, 9100, 5700, 8500, 1000, 2500, 5500, 0, 2200, 5500, 8500, 6100, 4300, 5900, 5000, 5300],
        #Poseidon del caribe
[10200, 9500, 4800, 9100, 5200, 6800, 10200, 6800, 9500, 2000, 1000, 6500, 2200, 0, 6000, 8900, 6500, 5100, 6400, 5400, 5700],
        #Edificio el faraon 
[7300, 6600, 5800, 6200, 5000, 600, 5900, 100, 6600, 4700, 7000, 500, 5500, 6000, 0, 7100, 550, 3500, 450, 1500, 1000],
        #Balcones de crespo
[1400, 1000, 5400, 1000, 5700, 6400, 2000, 6300, 220, 7700, 9900, 6400, 8500, 8900, 7100, 0, 7200, 5400, 7300, 6300, 6700],
        #Los cedros de manga
[7600, 6900, 5100, 5800, 5300, 180, 5500, 300, 6200, 5300, 7600, 700, 6100, 6500, 550, 7200, 0, 3000, 850, 1300, 1400],
        #libreria nacional
[5500, 4800, 750, 4400, 1100, 3100, 4500, 3100, 4800, 3600, 5800, 3100, 4300, 5100, 3500, 5400, 3000, 0, 3600, 2600, 3000],
        #edificio antonela
[7800, 7100, 5200, 6600, 5400, 1000, 5600, 550, 7100, 5200, 7400, 600, 5900, 6400, 450, 7300, 850, 3600, 0, 1400, 900],
        #Edificio marina mar
[6800, 6100, 4200, 5700, 4500, 1500, 5400, 1100, 6100, 4200, 6500, 1100, 5000, 5400, 1500, 6300, 1300, 2600, 1400, 0, 550],
        #Edificio Valenty
[7100, 6400, 4600, 6000, 4800, 1600, 5700, 1100, 6400, 4500, 6800, 550, 5300, 5700, 1000, 6700, 1400, 3000, 900, 550, 0],]

###### DATOS ######

def iniciar(arr,x):
    var = 0.0
    p =[]
    p.extend(x)
    p.append(0)
    c = 0
    xe = len(x)
    var = arr[0][x[0]]
    for i in range(xe):
        c = i+1
        var = var + arr[p[i]][p[c]]
        
    return var

def impresion(T,Times,Current,x,nombres):
    ordenado = []
    ordenado.append(nombres[0])
    for i in x:
        ordenado.append(nombres[i])
    os.system('clear')
    print('Temperature: ', T)
    print('Iterations: ', Times)
    print('Current best solution: ', Current)
    print('Route order: ',ordenado )
    print(x)

arr = datos
n = len(arr)-1    
T = 1000 #Temperature
af = 0.99 #Alpha value
times = 0  #Iterations
x = []
x = [i for i in range(len(arr))] #Order in which we're visiting the cities
x.pop(0)
random.shuffle(x) #shuffles the order of the cities
ran =0.0 #For the random worst solution choice-.
xp = copy.copy(x)
ini = iniciar(arr,x) #basic solution

while T >0.1:
    times = times + 1
    q=0
    w=0
    xp=copy.copy(x)
    while (q == w):
        q = random.randint(0,n-1)
        w = random.randint(0,n-1)
    aux1=x[q]
    aux2=x[w]
    xp[q]=aux2
    xp[w]=aux1
    fin = (iniciar(arr,xp)) #tampered solution
    getcontext().prec=5 #This sets a maximum of 5 decimal points for the chance variable, if we don't use this it explodes :V
    chance = Decimal(-(fin-ini)/T).exp()
    if ini < fin: #If the initial solution's better, we set a random probability for it to change to the tampered solution
        ran = Decimal(random.uniform(0,1))
        if ran < chance:
            x = copy.copy(xp)
            T = T * af  #getting cold
    else: #If the tampered solution's better, set the initial equal to it
        ini = fin
        x = copy.copy(xp)
        T = T * af #getting cold
    if times % 100 == 0:
        impresion(T,times,ini,x,nombres)
            