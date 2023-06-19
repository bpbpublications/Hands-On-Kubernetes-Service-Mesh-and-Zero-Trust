from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def info():
    html = "<h3>Pets service</h3>"
    return html

@app.route('/pet', methods=['DELETE'])
def deletePet():
    return "DELETE pet method called"

@app.route('/pet',methods=['PUT'])
def updatePet():
    return "PUT pet method called"


@app.route('/pet', methods=['POST'])
def createPet():
    return "POST pet method called"


@app.route('/pet')
def getPet():
    return "<h2>V2 of pet service. Do things differently</h2>"


if __name__ == '__main__':
    app.run()

