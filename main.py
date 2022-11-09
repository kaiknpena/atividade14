# Importar a classe Flask e o objeto request:
from re import X
from flask import Flask, request
import math

# Criar o objeto Flask app:
app = Flask(__name__)

# http://127.0.0.1:5000/medida/distancia
@app.route('/medida/distancia', methods=['POST'])
def distancia():
    objeto_json = request.get_json()
    # Verificar se o ojeto no formato JSON é NULL.
    if objeto_json is not None:
        if 'codigo' in objeto_json:
            x1 = objeto_json['x1']
        if 'codigo' in objeto_json:
            y1 = objeto_json['y1']
        if 'codigo' in objeto_json:
            x2 = objeto_json['x2']
        if 'codigo' in objeto_json:
            y2 = objeto_json['y2']

    #distancia=math.pow((x2-x1),2)+(math.pow((y2-y1),2))
    distancia=x1+x2
    #distancia=math.sqrt(distancia)

    return '''A distância entre os pontos é {}'''.format(x1)

# http://127.0.0.1:5000/produto/verificar
@app.route('/produto/verificar', methods=['POST'])
def verificar():
    objeto_json = request.get_json()
    # Verificar se o ojeto no formato JSON é NULL.
    if objeto_json is not None:
        if 'codigo' in objeto_json:
            c = objeto_json['codigo']

    if(c==1):
        preco="99,99"
    elif(c==2):
        preco="103,89"
    elif(c==2):
        preco="49,98"
    elif(c==2):
        preco="89,72"
    else:
        preco="97,35"

    return '''O valor do produto é: R${}'''.format(preco)

# http://127.0.0.1:5000/calculos/triangulo
@app.route('/calculos/triangulo', methods=['POST'])
def triangulo():
    objeto_json = request.get_json()
    # Verificar se o ojeto no formato JSON é NULL.
    if objeto_json is not None:
        if 'lado1' in objeto_json:
            x = objeto_json['lado1']

        if 'lado2' in objeto_json:
            y = objeto_json['lado2']

        if 'lado3' in objeto_json:
            z = objeto_json['lado3']

    resultado = ""

    if (x >= (y + z) or y >= (x + z) or z >= (y + x)):
        resultado = "Não é"
    else:
        resultado = "É"

    return '''{} possível formar um triângulo com os valores inseridos.'''.format(resultado)


# http://127.0.0.1:5000/calculo/imc?altura=2&peso=200
@app.route('/calculo/imc')
def imc():
    altura = float(request.args.get('altura'))
    peso = float(request.args.get('peso'))
    imc = peso / (altura*altura)
    ideal = ""
    if (imc < 18.5):
        ideal = "Abaixo do peso"
    elif (imc < 24.9):
        ideal = "Peso ideal"
    elif (imc < 29.9):
        ideal = "Levemente acima do peso"
    elif imc < 34.9:
        ideal = "Obesidade Grau I"
    elif imc < 39.9:
        ideal = "Obesidade Grau II (severa)"
    else:
        ideal = "Obesidade Grau III (mórbida)"
    return '''<h1>Resultado: {}</h1>'''.format(ideal)


if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug=True, port=5000)
