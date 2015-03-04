# -*- coding: utf-8 -*- 
import shelve

misprendas = [
    {'tipo':'camisa','color':'roja', 'usos':0, 'limite':1}, 
    {'tipo':'camisa','color':'azul', 'usos':0, 'limite':1},
    {'tipo':'camisa','color':'verde', 'usos':0, 'limite':1},
    {'tipo':'camisa','color':'negra', 'usos':0, 'limite':1},
    {'tipo':'camisa','color':'blanca', 'usos':0, 'limite':1},  
    {'tipo':'pantalon','color':'rojo', 'usos':0, 'limite':3}, 
    {'tipo':'pantalon','color':'azul', 'usos':0, 'limite':3}, 
    {'tipo':'pantalon','color':'negro', 'usos':0, 'limite':3},
    {'tipo':'pantalon','color':'verde', 'usos':0, 'limite':3}, 
    {'tipo':'pantalon','color':'blanco', 'usos':0, 'limite':3}, 
    {'tipo':'zapatos','color':'azules', 'usos':0, 'limite':5}, 
    {'tipo':'zapatos','color':'negros', 'usos':0, 'limite':5}, 
    {'tipo':'zapatos','color':'marrones', 'usos':0, 'limite':5}]
    
misreglas = (
    ['roja', 'rojo', 'marrones'],
    ['roja', 'rojo', 'negros'],
    ['roja', 'rojo', 'azules'], 
    ['azul', 'verde', 'marrones'],
    ['azul', 'verde', 'negros'],
    ['azul', 'verde', 'azules'], 
    ['azul', 'azul', 'marrones'],
    ['azul', 'azul', 'negros'],
    ['azul', 'azul', 'azules'],
    ['verde', 'verde', 'marrones'],
    ['verde', 'verde', 'negros'],
    ['verde', 'verde', 'azules']
    )


config = shelve.open('miropero.dat')
config['misprendas'] = misprendas
config['misreglas'] = misreglas
config.close()


        

