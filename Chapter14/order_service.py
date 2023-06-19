from flask import Flask, request
import requests
from opentelemetry.instrumentation.flask import FlaskInstrumentor

app = Flask(__name__)
FlaskInstrumentor.instrument_app(app)


@app.route('/')
def info():
    html = "<h3>Orders service</h3>"
    return html


@app.route('/order', methods=['DELETE'])
def deleteOrder():
    return "DELETE order method called"


@app.route('/order',methods=['PUT'])
def updateOrder():
    return "PUT order method called"


@app.route('/order', methods=['POST'])
def createOrder():
    return "POST order method called"


@app.route('/order')
def getOrder():
    headers = {}
    trace_headers = ['x-request-id',
                     'x-b3-traceid',
                     'x-b3-spanid',
                     'x-b3-parentspanid',
                     'x-b3-sampled',
                     'x-b3-flags']
    for thdr in trace_headers:
        val = request.headers.get(thdr)
        if val is not None:
            headers[thdr] = val
    getpet = requests.get("http://petservice.default.svc.cluster.local:8080/", headers=headers)
    return getpet.text + " -- " + "GET order method called"


if __name__ == '__main__':
    app.run(host='::', port=8080)

