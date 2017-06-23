from flask import Flask, abort
import socket, time, logging, sys

app = Flask(__name__)
Fail = ''
hostname = socket.gethostname()

@app.route("/")
def hello():
    return "Host: {host}".format(host=socket.gethostname())

@app.route("/health")
def health():
    if Fail == 'Delay':
        app.logger.warning("Delaying response to %s", hostname)
        time.sleep(7)
    elif Fail == '404':
        app.logger.warning("Failing %s with 404", hostname)
        abort(404)

    return Fail

@app.route("/delay")
def delay():
    global Fail
    Fail = 'Delay'
    app.logger.warning('Next request to %s will be delayed', hostname)
    return "next request to http://{hostname}/health will be delayed 7 seconds".format(hostname=hostname)

@app.route("/fail")
def fail():
    global Fail
    Fail = '404'
    app.logger.warning('Next request to %s will fail with 404', hostname)
    return "next request to http://{hostname}/health will fail with 404".format(hostname=hostname)

if __name__ == '__main__':
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    try:
        app.run(host='0.0.0.0', port=80)
    except KeyboardInterrupt:
        app.stop()
