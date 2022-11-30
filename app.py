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


# @app.route('/guest/<guest>')
# def hello_guest(guest):
#    return 'Hello %s as Guest' % guest

# @app.route('/user/<name>')
# def hello_user(name):
#    if name =='admin':
#       return redirect(url_for('hello_admin'))
#    else:
#       return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
   app.run(debug = True)
