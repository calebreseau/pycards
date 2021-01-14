from terrain import Terrain
from jeu import Jeu
from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)
jeu=Jeu() 

@app.route('/pycards/')
def start():
    global jeu
    jeu=Jeu()
    res=''
    return render_template('game.html',defausse=res,compteur=str(len(jeu.terrain.paquet)),def_compteur=str(jeu.terrain.trash),len=len(jeu.terrain.defausse))

        
@app.route('/draw/')
def draw():
    global jeu
    res=jeu.update()
    print(str(len(res)))
    print('response: '+'\r\n'.join(res))
    return ''.join(res)
    return render_template('game.html',defausse=res,compteur=str(len(jeu.terrain.paquet)),def_compteur=str(jeu.terrain.trash),len=len(jeu.terrain.defausse))

@app.route('/vider/')
def vider():
    global jeu
    jeu.terrain.viderDefausse()
    return str(jeu.terrain.trash)
    return render_template('game.html',defausse=res,compteur=str(len(jeu.terrain.paquet)),def_compteur=str(jeu.terrain.trash),len=len(jeu.terrain.defausse))
      

app.run(debug=False)