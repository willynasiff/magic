from flask import Flask, render_template, request, redirect
from mostrar2 import mostrarCartas

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def a():
  if request.method == 'POST':
     if request.form['opcion'] == "   1    ":
       return redirect('/cadaCarta/1')
     elif request.form['opcion'] == "   2    ":
       return redirect('/cadaCarta/2')
     elif request.form['opcion'] == "   3    ":
       return redirect('/cadaCarta/3')

  elif request.method == 'GET':
    return render_template('cada.html')

@app.route("/cadaCarta/<number>")
def b(number):
  return render_template("cada2.html", returning = mostrarCartas(number))





if __name__=='__main__':
  app.run(host='0.0.0.0')

