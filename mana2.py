from __future__ import division
import sqlite3
from configW import __database
miDB = sqlite3.connect(__database)


def bNonLands(mazo):
 
  
  c = miDB.cursor()
 
  # esto devuelve cantidad de nonlands del mazo
  statement = ' select count(Carta.ID) from Carta, Carta_Mazo'
  statement += ' where Carta_Mazo.ID_Mazo = {} and Carta_Mazo.ID_Carta'.format(mazo)
  statement += ' = Carta.ID and Carta.ID_Tipo is not 5;'
 
  for row in c.execute(statement):
    tupla = row[0]

  miDB.commit()

  noLand = tupla
  return noLand


def bCuantoMana(mazo):

  c = miDB.cursor()

  statement = 'select Carta_Color.ID_Color, count(Carta_Color.ID)'
  statement += ' from Carta_Color, Carta_Mazo, Carta where Carta_Color.ID_Carta = Carta.ID'
  statement += ' and Carta.ID = Carta_Mazo.ID_Carta and Carta_Color.ID_Color is not 1'
  statement += ' and Carta_Mazo.ID_Mazo = {} group by Carta_Color.ID_Color;'.format(mazo)
  
 
  aLista = []
  bLista = []
  maLista = []

  for row in c.execute(statement):
    tupla = row[0]
    tupla2 = row[1]
 
    aLista.append(tupla)
    bLista.append(tupla2)
   
  miDB.commit()
 
  maLista.append('Mazo {}'.format(mazo))
  derListe = [maLista, aLista, bLista]

  return derListe


def dMana(nonLands, cMana):

  dic2 = {1 : 'colorless', 2 : 'white', 3 : 'blue', 4 : 'black', 5 : 'red', 6 : 'green'}

  nonLand = nonLands 
  nMazo = cMana[0][0]
  colorM = cMana[1]
  cantM = cMana[2]

  sumaM = sum(cantM)
  lands = 60 - nonLand 
  porcentaje = []
  porcentaje2 = []
  
  mandar = [] 
  
  

  
  for number in cantM:
    porcentaje.append(number * ( 100/sumaM))
   
  
  
  for number in range(len(porcentaje)):
    porcentaje2.append(porcentaje[number] * (lands/100))
    if number == 0:
      mandar.append(nMazo)
      mandar.append('{0} {1:.2f}'.format(dic2[colorM[number]], porcentaje2[number])) 
    else:
      mandar.append('{0} {1:.2f}'.format(dic2[colorM[number]], porcentaje2[number])) 
  return mandar
 


def creador():
  enviar = []
  for mazo in range(1, 4):
     enviar.append(dMana(bNonLands(mazo), bCuantoMana(mazo)))
  return enviar




if __name__=='__main__':
   creador()
 

