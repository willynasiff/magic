from flask import Flask, render_template, request, redirect
from mostrar2 import mostrarCartas
from mana2 import creador
from sueltas import cartasSueltas

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def a():
  if request.method == 'POST':
     if request.form['opcion'] == "1":
       return redirect('/cadaCarta/1')
     elif request.form['opcion'] == "2":
       return redirect('/cadaCarta/2')
     elif request.form['opcion'] == "3":
       return redirect('/cadaCarta/3')
     elif request.form['opcion'] == "Calcular Mana":
       return redirect('/calcularMana')
     elif request.form['opcion'] == 'Cartas sueltas':
       return redirect('/cartasSueltas')

  elif request.method == 'GET':
    return render_template('inicio.html')

@app.route("/cadaCarta/<number>", methods=['GET','POST'])
def b(number):
  if request.method == 'POST':
    if request.form['pVolver'] == "Volver":
      return redirect('/')
  elif request.method == 'GET':
    return render_template("cada.html", returning = mostrarCartas(number))


@app.route("/calcularMana", methods=['GET','POST'])
def c():
  if request.method == 'POST':
    if request.form['pVolver'] == "Volver":
      return redirect('/')
  elif request.method == 'GET':
    return render_template("mana.html", returning = creador())

@app.route("/cartasSueltas", methods=['GET','POST'])
def d():
  if request.method == 'POST':
    if request.form['pVolver'] == "Volver":
      return redirect('/')
  elif request.method == 'GET':
    return render_template("sueltas.html", returning = cartasSueltas())




if __name__=='__main__':
  app.run(host='0.0.0.0')

