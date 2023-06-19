from flask import Flask, request
import requests
from opentelemetry.instrumentation.flask import FlaskInstrumentor
app = Flask(__name__)

FlaskInstrumentor.instrument_app(app)

@app.route('/')
def info():
    html = "<h3>Delivery service</h3>"
    return html

@app.route('/delivery', methods=['DELETE'])
def cancelDelivery():
    return "Delivery cancelled"

@app.route('/petdelivery')
def petDelivery():
    getpet = requests.get("http://petservice:8080/pet")
    return getpet.text + " from Delivery service"

@app.route('/delivery')
def getOrder():

    headers = {}
    trace_headers = [ 'x-request-id',
                     'x-b3-traceid',
                        'x-b3-spanid',
        'x-b3-parentspanid',
        'x-b3-sampled',
        'x-b3-flags']
    for thdr in trace_headers:
        val = request.headers.get(thdr)
        if val is not None:
            headers[thdr] = val
    getorder = requests.get("http://orderservice.orders.svc.cluster.local:8080/order", headers)
    return getorder.text + "  " +"GET delivery method called"


if __name__ == '__main__':
    app.run(host='::', port=8080)

