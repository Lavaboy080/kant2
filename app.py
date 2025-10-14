from flask import Flask, render_template
import datetime

dager = {'Monday':'Mandag','Tuesday':'Tirsdag','Wednesday':'Ondsdag','Thursday':'Torsdag','Friday':'Fredag','Saturday':'Lørdag','Sunday':'Søndag'}
verdi = {'Pølser':'15kr','Risgrøt':'10kr','Pizza':'35kr','Grønnsaksuppe':'20kr','Salat':'10kr','Skolefri':'ingen mat','Skolefri':'ingen mat'}
beskribelse ={'Pølser':'Pølse i brød','Risgrøt':'Glutenfri Risgrøt','Pizza':'Pizzastykke med peperoni','Grønnsaksuppe':'Suppe med gulrot og potet','Salat':'Salat med tomat og agurk'}
idag = datetime.datetime.now().strftime("%A")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
