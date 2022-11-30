from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/authenticate')
def api_auth():
   return {'msg': 'test: auth'}

@app.route('/LogOut')
def api_logout():
   return {'msg': 'test: logout'}

@app.route('/register/user')
def api_register_user():
   return {'msg': 'test: register uses'}

if __name__ == '__main__':
   app.run(debug = True)
