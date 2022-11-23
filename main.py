from flask import Flask, request

client = Flask(__name__)

@client.route('/post', methods = ['POST'])
def post():
    req = request.json
    return req

@client.route('/get', methods = ['GET'])
def get():
    req = request.json
    return req

if __name__ == '__main__':
    client.run(host='127.0.0.1', port=3700)
