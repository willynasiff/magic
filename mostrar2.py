import sqlite3 
import os.path
from configW import __database


def mostrarCartas(requestW):
  miDB = sqlite3.connect(__database)
  c = miDB.cursor()

  retorno = []
  laLista = []
  agregar2 = []
  agregar = []
  ultima = []


  query = 'select Carta.Nombre, Carta.ID, count(Carta.ID) from Carta, Carta_Mazo where Carta.ID = Carta_Mazo.ID_Carta and Carta_Mazo.ID_Mazo = {} group by Carta.ID order by count(Carta.ID);'.format(requestW)

  for row in c.execute(query):
    laLista.append(row)

  miDB.commit()
  miDB.close()
 
  if len(laLista)%2 == 1:
    final = len(laLista) -1
  else:
    final = len(laLista)

  for row in range(0, final, 2):
    sacar = laLista[row]
    sacar2 = laLista[row+1]   
 
    nombre = sacar[0]
    ID = sacar[1]
    cantidad = sacar[2]

    nombre2 = sacar2[0]
    ID2 = sacar2[1]
    cantidad2 = sacar2[2]

    agregar = ["/static/fotos/{}.png".format(ID), "/static/fotos/{}.png".format(ID2)]
    agregar2 = ["{1} {0} cantidad: {2}".format(nombre, ID, cantidad), "{1} {0} cantidad: {2}".format(nombre2, ID2, cantidad2)]

    retorno.append(agregar)
    retorno.append(agregar2)
    
 
  if len(laLista)%2 == 1:
    imparSacar = laLista[row+2]

    nombreImpar = imparSacar[0]
    IDimpar = imparSacar[1]
    cantidadImpar = imparSacar[2]

    agregar = ["/static/fotos/{}.png".format(IDimpar), "/static/fotos/0.png"]
    agregar2 = ["{1} {0} cantidad: {2}".format(nombreImpar, IDimpar, cantidadImpar), ""] 

    retorno.append(agregar)
    retorno.append(agregar2)

      
  ultima = [retorno, requestW]
  return ultima
  
