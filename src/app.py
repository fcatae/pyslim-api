from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/<res>', methods=['GET', 'POST'])
def api_hello(res):
   return {'msg': 'Hello World'}

@app.route('/ping')
def ping():
   return {'ping': 'app'}

print('--- APP started ---')

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=5000, debug=True)
