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
    # if 'user' in request.headers:
    #     if request.headers['user'] == 'testuser':
    #         return "<h2> testuser called. Do things differently.</h2>"
    return "<h2>GET pet method called</h2>"


if __name__ == '__main__':
    app.run()

