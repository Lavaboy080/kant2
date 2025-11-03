from flask import Flask, render_template
import datetime

app = Flask(__name__)

#lister med retter, dager, priser og bilder 
matretter = ['Pølser','Risgrøt','Pizza','Grønnsaksuppe','Salat']
beskribelse =['Pølse med tilbehør','Risgrøt med tilbehør','Pizzastykke med peperoni','Grønnsaksuppe','Salat med tomat og agurk']
igredienser = ['Melk','Grøtris','Sukker','Purre','Gulrot','Brekkbønner','Tomat','Agurk','Isbergsalat','Pølse','Pølsebrød','Ketchup','Mel','Gjær','Vann','Olje','Sennep','Smør','Kanel','Pepperoni','Brød','Ost','Reker','Mr le kopp','Skinke']
pris = ['15kr','10kr','35kr','20kr','10kr']
fastvarer = ['Vann','Melk','Rekesmørbrød','Nudler','Toast']
fastpris = ['Gratis','5kr','15kr','10kr','15kr']
ukedager = ['Mandag','Tirsdag','Onsdag','Torsdag','Fredag']
bilder4 = ['../static/bilder/Vann.png','../static/bilder/Melk.png','../static/bilder/Rekesmørbrød.png','../static/bilder/Nudler.png','../static/bilder/Toast.png']
bilder3 = ['../static/bilder/Melk.png','../static/bilder/Grøtris.png','../static/bilder/Sukker.png','../static/bilder/Purre.png','../static/bilder/Gulrot.png','../static/bilder/Brekkbønner.png','../static/bilder/Tomat.png','../static/bilder/Agurk.png','../static/bilder/Isbergsalat.png','../static/bilder/Pølsepakker.png','../static/bilder/Pølsebrød.png','../static/bilder/Ketchup.png','../static/bilder/Mel.png','../static/bilder/Gjær.png','../static/bilder/Vann.png','../static/bilder/Olje.png','../static/bilder/Sennep.png','../static/bilder/Smør.png','../static/bilder/Kanel.png','../static/bilder/Pepperoni.png','../static/bilder/Brød.png','../static/bilder/Ost.png','../static/bilder/Reker.png','../static/bilder/Nudler.png','../static/bilder/skinke.png']
bilder2 = ['../static/bilder/Pølse.png','../static/bilder/Risgrøt.png','../static/bilder/Pizza.png','../static/bilder/Grønnsaksuppe.png','../static/bilder/Salat.png']
bilder = {'Monday':'../static/bilder/Pølse.png','Tuesday':'../static/bilder/Risgrøt.png','Wednesday':'../static/bilder/Pizza.png','Thursday':'../static/bilder/Grønnsaksuppe.png','Friday':'../static/bilder/Salat.png'}
dager = {'Monday':'Mandag','Tuesday':'Tirsdag','Wednesday':'Onsdag','Thursday':'Torsdag','Friday':'Fredag'}
verdi = {'Pølser':'15kr','Risgrøt':'10kr','Pizza':'35kr','Grønnsaksuppe':'20kr','Salat':'10kr'}
dag = datetime.datetime.now().strftime("%A")


#kjører det dokumentet som er inni rendertemplate og routen er liksom lenken
#dette er hjemsiden som kjører index.html
@app.route('/')
def index():
    return render_template("index.html")

#kjører det dokumentet som er inni rendertemplate og routen er liksom lenken
#dette er hjemsiden som kjører meny.html
#alle listene blir lagt til her
@app.route('/meny')
def meny():
    return render_template("meny.html",dager=dager,verdi=verdi,beskribelse=beskribelse,dag=dag,ukedager=ukedager,matretter=matretter,pris=pris,bilder=bilder,bilder2=bilder2,igredienser=igredienser,bilder3=bilder3,bilder4 =bilder4,fastpris=fastpris,fastvarer=fastvarer)

#kjører det dokumentet som er inni rendertemplate og routen er liksom lenken
#dette er hjemsiden som kjører varer.html
#alle listene blir lagt til her
@app.route('/varer')
def varer():
    return render_template("varer.html",dager=dager,verdi=verdi,beskribelse=beskribelse,dag=dag,ukedager=ukedager,matretter=matretter,pris=pris,bilder=bilder,bilder2=bilder2,igredienser=igredienser,bilder3=bilder3,bilder4 =bilder4,fastpris=fastpris,fastvarer=fastvarer)

#kjører det dokumentet som er inni rendertemplate og routen er liksom lenken
#dette er hjemsiden som kjører ingredienser.html
#alle listene blir lagt til her
@app.route('/ingredienser')
def ingridienser():
    return render_template("ingredienser.html",dager=dager,verdi=verdi,beskribelse=beskribelse,dag=dag,ukedager=ukedager,matretter=matretter,pris=pris,bilder=bilder,bilder2=bilder2,igredienser=igredienser,bilder3=bilder3,bilder4 =bilder4,fastpris=fastpris,fastvarer=fastvarer)

#kjører det dokumentet som er inni rendertemplate og routen er liksom lenken
#dette er hjemsiden som kjører kontakt.html
@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html")



if __name__ == "__main__":
    app.run()
