from flask import Flask, render_template

app = Flask(__name__)

# Creating simple Routes 
@app.route('/test') 
def test():
    return "Home Page"

@app.route('/test/about/')
def about_test():
    return "About Page"

# Routes to Render Something
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")

@app.route('/ing', strict_slashes=False)
def ing():
    return render_template("ing.html")

@app.route('/seguridad', strict_slashes=False)
def seguridad():
    return render_template("seguridad.html")

@app.route('/maquinado', strict_slashes=False)
def maquinado():
    return render_template("maquinado.html")

@app.route('/clientes', strict_slashes=False)
def clientes():
    return render_template("clientes.html")

@app.route('/contacto', strict_slashes=False)
def contacto():
    return render_template("contacto.html")

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)