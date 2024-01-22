from flask import Flask, render_template, request
from model import clasificar_imagen

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clasificar', methods=['POST'])
def clasificar():
    imagen = request.files['imagen']
    resultado_clase = clasificar_imagen(imagen)
    return render_template('resultado.html', resultado=resultado_clase)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
