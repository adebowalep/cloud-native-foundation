from flask import Flask, json
import logging


app = Flask(__name__)


@app.route("/")
def hello():
    app.logger.info('Main request successful')
    return "Hello World!"


@app.route("/status")
def healthcheck():
    response = app.response_class(
             response=json.dumps({"result":"OK - healthy"}),
	     status = 200,
	     mimetype='application/json'
    
    )
    app.logger.info('Status request successful')
    return response


@app.route("/metrics")
def metrics():
    response = app.response_class(
       response=json.dumps(
	{"status":"success","code":0,"data":{"UserCount":140,"UserActive":23}}),
	status=200,
	mimetype='application/json'
    )
    app.logger.info('Metrics request succesfull')
    return response

if __name__ == "__main__":
    ## Stream logs to a file 
    logging.basicConfig(filename='app.log',level=logging.DEBUG,
               format='%(asctime)s,%(message)s',datefmt='%Y-%m-%d %H:%M:%S')
    app.run(host='0.0.0.0')
