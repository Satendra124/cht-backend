url = "http://127.0.0.1:8000/activity/"
import requests
import random,datetime
def gen(lim,x=1632808540):
    req = requests.post(url,{
        "latitude": 25.25 + random.randint(0,9)/1000,
        "longitude": 82.98 + random.randint(0,9)/1000,
        "amplitude": random.randint(500,2000),
        "useruid": "tT7LbyAWwJQ53cCAS5wJIPllHo73",
        "steps": random.randint(0,5000),
        "time_start": datetime.datetime.fromtimestamp(x),
        "time_end": datetime.datetime.fromtimestamp(x + 5*60)
    })
    print(req.json())
    if(lim>1):
        gen(lim-1,x+5*60)

gen(100)