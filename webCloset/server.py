#!/usr/bin/python
# -*- coding: utf-8 -*- 
from flask import Flask, url_for, render_template
import json
import time
import shelve
import random

app = Flask(__name__)

def incrementa_usos(combinacion, misprendas): 
    for prenda in misprendas:
        if prenda['tipo'] == 'camisa' and prenda['color'] == combinacion[0]:
            prenda['usos'] = prenda['usos']+1        
        if prenda['tipo'] == 'pantalon' and prenda['color'] == combinacion[1]:
            prenda['usos'] = prenda['usos']+1        
        if prenda['tipo'] == 'zapatos' and prenda['color'] == combinacion[2]:
            prenda['usos'] = prenda['usos']+1            
	

def ordena_ropero(misprendas):
    miscamisas = []
    mispantalones = []
    miszapatos = []
    for prenda in misprendas:
        if prenda['tipo'] == 'camisa' and prenda['usos'] < prenda['limite']:   
            miscamisas.append(prenda['color'])
        if prenda['tipo'] == 'pantalon' and prenda['usos'] < prenda['limite']:   
            mispantalones.append(prenda['color'])
        if prenda['tipo'] == 'zapatos' and prenda['usos'] < prenda['limite']:   
            miszapatos.append(prenda['color'])            
    ropero = []
    ropero.append(miscamisas)
    ropero.append(mispantalones)
    ropero.append(miszapatos)
    print "Ropero disponible:"+str(ropero)
    return ropero

def elige_combinacion(ropero):
    camisas = ropero[0]
    pantalones = ropero[1]
    zapatos = ropero[2]
    combinacion = None
    if camisas and pantalones and zapatos:
        random.shuffle(camisas)
        random.shuffle(pantalones)
        random.shuffle(zapatos)
        combinacion = [camisas[0], pantalones[0], zapatos[0]]
    return combinacion


def verifica_combinacion(combinacion, misreglas):
    respuesta = True
    for regla in misreglas:
        if regla == combinacion:
            respuesta = False
    return respuesta    
   


def selecciona_ropa():
    combina = False
    ropero = ordena_ropero(misprendas)
    while (combina == False):
        combinacion = elige_combinacion(ropero)
        if combinacion:
            print 'Combinacion elegida:  camisa '+combinacion[0]+', pantalon '+combinacion[1]+' y zapatos ', combinacion[2]
            combina = verifica_combinacion(combinacion, misreglas)
            if (combina == False):
                print "No combina, elijo otra"
            else:
                print "Combina bien" 
                incrementa_usos(combinacion, misprendas)
                guarda_datos()
                return combinacion
        else: 
            return None           

def repon_ropa():
    for prenda in misprendas:
        if prenda['usos'] >= prenda['limite']:
            print "Repone en el ropero:" + prenda['tipo'] + " " + prenda['color'] 
            prenda['usos'] = 0


def guarda_datos():
    config = shelve.open('miropero.dat')
    config['misprendas'] = misprendas  
    config.close()
    print 'Guarda datos...'
			   
	  
@app.route('/')
def main(): 
	return render_template('index.html')
		

@app.route('/selecciona')
def selecciona():
	combinacion = selecciona_ropa()
	return render_template('selecciona.html', combinacion = combinacion)
	

@app.route('/lista')
def lista():
	return render_template('lista.html', misprendas = misprendas)
	
@app.route('/repon')
def repon():
	repon_ropa()
	#ropero = ordena_ropero(misprendas)
	guarda_datos()
	mensaje = "Reponiendo ropa"
	return render_template('repon.html', mensaje = mensaje)

if __name__=='__main__':
	# *** PROGRAMA PRINCIPAL ***
	config = shelve.open('miropero.dat')
	misprendas = config['misprendas']
	misreglas = config['misreglas'] 
	config.close()
	ropero = ordena_ropero(misprendas)

	app.debug = True
	app.run(host ='0.0.0.0')
		


		  

