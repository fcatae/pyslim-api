from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/<res>')
def api_hello(res):
   return {'msg': 'Hello World'}

if __name__ == '__main__':
   app.run(debug = True)
