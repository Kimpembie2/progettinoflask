from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#configurazione db
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///lista_spesa.db&';
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#inizializza SQLAlchemy
db.init_app(app)
#crea il database se non esiste
with app.app_context():
    db.create_all()

#___________________________________________________________________
#creazione tabelle
db = SQLAlchemy() #inizialliziamo sqlAlchemy
class ListaSpesa(db.Model): #tabella
    id = db.Column(db.Integer, primary_key=True) #id elemento, unico  
    elemento = db.Column(db.String(100), nullable=False) #elemento, non nullo