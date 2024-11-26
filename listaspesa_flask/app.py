from flask import Flask, render_template, request, redirect, url_for
#render_template: collegare file HTML.
#inizializza l'app Flask
app = Flask(__name__)

#rotta principale
@app.route('/')
def home():
    return render_template('index.html', lista=listaspesa)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        listaspesa.append(elemento)
    return redirect(url_for('home'))

@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    if 0 <= indice < len(listaspesa):
        listaspesa.pop(indice)
    return redirect(url_for('home'))

listaspesa = []
#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)

