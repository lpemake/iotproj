import json
from flask import Flask, render_template, request, Response
app = Flask(__name__)

# TODO: tee lista mittauksia varten
measurements = []

@app.route('/line')
def get_line():
    return render_template('linechart.html', result = measurements)

# TODO: avaa sivun result.html ja näyttää mittaukset siinä
@app.route('/mittaukset')
def get_all_measurements_page():
    return render_template('result.html', result = measurements)

# TODO: ota vastaan HTTP POSTilla lähetty mittaus ja laita se taulukkoon
@app.route('/uusimittaus', methods=['POST'])
def uusi():
    m = request.get_json(force=True)
    measurements.insert(0, m)
    return json.dumps(m, indent=True)

if __name__ == '__main__':
   app.run(debug = True)
   