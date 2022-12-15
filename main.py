from flask import Flask
import timeit

app = Flask(__name__)

@app.route("/")
def hello():
    numeros(100001)
    tiempo = timeit.timeit('x = 5', number=100000000)
    return(f"El tiempo de ejecución fue {tiempo} segundos" )


def numeros(fin):
    try:
        f = open('numeros.txt', 'w')
        print('Iniciando creación del archivo')
        for i in range(fin):
            f.write("%s\n" % i)
        f.close()
        print('Se ha terminado la creación del archivo')
    except FileNotFoundError:
        print("Error en la genera")

app.run(host="0.0.0.0", port=8080)