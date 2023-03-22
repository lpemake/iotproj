import requests    
import json   
import math   
import time                               

sade = 10
alfa = 0
while alfa < 200:
    measurement = { }
    measurement['alfa'] = alfa
    measurement['x'] = sade * math.cos(alfa)
    measurement['y'] = sade * math.sin(alfa)
    measurement['z'] = 0

    # muunna json-muotoon 
    s = json.dumps(measurement)
    # TODO: lähetä data HTTP Postilla serverille
    response = requests.post("http://localhost:5000/uusimittaus", data = s)

    print(s)
    time.sleep(1)

    alfa += 0.1
