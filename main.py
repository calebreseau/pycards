from terrain import Terrain
from jeu import Jeu
import importlib
from flask import Flask, render_template, Response, request, redirect, url_for
import sys
app = Flask(__name__)
#jeu=Jeu() 

def load_jeu(name):
    name='jeu'+name
    importlib.import_module(name)
    mod=sys.modules[name]
    _class=getattr(mod,name)
    inst=_class()
    return inst

@app.route('/pycards/')
def start():
    global jeu
    if request.args.get("game")!=None:
        jeu=load_jeu(request.args.get('game'))
    else:
        jeu=Jeu()
    res=''
    return render_template('game.html',controls=jeu.controls,len=len(jeu.controls))

        
@app.route('/draw')
def draw():
    global jeu
    res=jeu.update(request.args.get('move').split(','))
    print(str(len(res)))
    #print('response: '+'\r\n'.join(res))
    return res[0]+','+''.join(res[1])

@app.route('/vider/')
def vider():
    global jeu
    jeu.terrain.viderDefausse()
    return str(jeu.terrain.trash)
      

app.run(debug=True)