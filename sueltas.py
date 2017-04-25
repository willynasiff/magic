import sqlite3 
import os.path
from configW import __database


def cartasSueltas():
  miDB = sqlite3.connect(__database)
  c = miDB.cursor()

  laLista = []
  listaNueva = []
  mandar = []

  query ='select Carta.ID, Carta.Nombre, count(Carta.ID) from Carta, Carta_Mazo'  
  query += ' where Carta.ID = Carta_Mazo.ID_Carta and Carta_Mazo.ID_Mazo is 0 group by Carta.ID;' 


  for row in c.execute(query):
 
    laLista.append(row[0])
    laLista.append(row[1])
    laLista.append(row[2])

  miDB.commit()
  miDB.close()
  
  for each in range(0, len(laLista), 3):
     
    mandar.append('{0}'.format(laLista[each], laLista[each+1], laLista[each+2]))
    mandar.append('{1}'.format(laLista[each], laLista[each+1], laLista[each+2]))    
    mandar.append('cantidad: {0}'.format(laLista[each+2]))

    listaNueva.append(mandar) 
    mandar = [] 

  return listaNueva


