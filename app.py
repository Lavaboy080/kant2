from flask import Flask, render_template
import datetime

app = Flask(__name__)

matretter = ['Pølser','Risgrøt','Pizza','Grønnsaksuppe','Salat']
pris = ['15kr','10kr','35kr','20kr','10kr']
ukedager = ['Mandag','Tirsdag','Ondsdag','Torsdag','Fredag']
dager = {'Monday':'Mandag','Tuesday':'Tirsdag','Wednesday':'Ondsdag','Thursday':'Torsdag','Friday':'Fredag'}
verdi = {'Pølser':'15kr','Risgrøt':'10kr','Pizza':'35kr','Grønnsaksuppe':'20kr','Salat':'10kr'}
beskribelse ={'Pølser':'Pølse i brød','Risgrøt':'Glutenfri Risgrøt','Pizza':'Pizzastykke med peperoni','Grønnsaksuppe':'Suppe med gulrot og potet','Salat':'Salat med tomat og agurk'}
dag = datetime.datetime.now().strftime("%A")



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/meny')
def meny():
    return render_template("meny.html",dager=dager,verdi=verdi,beskribelse=beskribelse,dag=dag,ukedager=ukedager,matretter=matretter,pris=pris)

@app.route('/varer')
def varer():
    return render_template("varer.html")

@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html")



if __name__ == "__main__":
    app.run()
