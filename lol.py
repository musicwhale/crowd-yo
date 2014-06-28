from flask import Flask
from flask import request
import requests
app = Flask(__name__)

#counter = 0

@app.route("/hi")
def hello():
    global counter, sent
    #counter = 0
    x = request.args.get('username')
    if x != None:
        counter += 1
    print x
    print str(counter)
    if counter >= 5 and sent == 0:
        #sent = 1
        requests.post("http://api.justyo.co/yoall/", data={'api_token': '2f9286ca-25cd-5342-e48c-8442aabbb2bb'})
        counter = 0

    #return "lol"
    return str(counter)

if __name__ == "__main__":
    #app.run()
    global counter, sent
    counter = 0
    sent = 0
    app.run(host='0.0.0.0')
