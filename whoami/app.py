from flask import Flask, make_response
import socket, time, logging, sys

app = Flask(__name__)
Fail = False
hostname = socket.gethostname()

@app.route("/")
def hello():
    return "Host: {host}".format(host=socket.gethostname())

@app.route("/health")
def health():
    if Fail:
        app.logger.warning("Delaying response to %s", hostname)
        time.sleep(7)
        
    return ""

@app.route("/delay")
def fail():
    global Fail
    Fail = True
    app.logger.warning('Next request to %s will be delayed', hostname)
    return "next request to http://{hostname}/health will be delayed 7 seconds".format(hostname=hostname)

if __name__ == '__main__':
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    try:
        app.run(host='0.0.0.0', port=80)
    except KeyboardInterrupt:
        app.stop()
