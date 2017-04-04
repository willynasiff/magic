import sqlite3 
import os.path
from configW import __database


def mostrarCartas(requestW):
  miDB = sqlite3.connect(__database)
  c = miDB.cursor()

  retorno = []
  mapa = []
  

  query = 'select Carta.Nombre, Carta.ID, count(Carta.ID) from Carta, Carta_Mazo where Carta.ID = Carta_Mazo.ID_Carta and Carta_Mazo.ID_Mazo = {} group by Carta.ID order by count(Carta.ID);'.format(requestW)

  for row in c.execute(query):
    nombre = row[0]
    ID = row[1]
    cantidad = row[2]

    agregar2 = "/static/fotos/{}.png".format(ID)

    agregar = "{1} {0} cantidad: {2}".format(nombre, ID, cantidad)
    retorno.append(agregar)
    retorno.append(agregar2)
  
 

  miDB.commit()
  miDB.close()

    



  return retorno
  
