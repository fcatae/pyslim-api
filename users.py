from flask import Flask, request, redirect
from userdb import UserDb

app = Flask(__name__)
userdb = UserDb()
userdb.add('test', { 'password': 'test1', 'email': 'test@email.com' })

@app.route('/authenticate')
def api_auth():
    content = request.get_json()
    username = content['username']
    password = content['password']

    details = userdb.get(username)
    isValid = (details is not None) and details['password'] == password

    if( isValid ):
        return {
            'ID': details['ID'],
            'Authenticated': True,
            'UserId': details['UserId'],
            'Token': details['Token'],
            'SessionToken': 'abcdefgh',
            'AccountId': details['AccountId'],
            'OMSId': details['OMSId']
        }
    
    return {
        'Authenticated': False,
        'Username': username
    }

@app.route('/Validar')
def api_validate():
    return {
            'result': True
        }

@app.route('/LogOut')
def api_logout():
    session = ''
    return { 
            'result': True,
            'errormsg': 'null',
            'errorcode': 0,
            'detail': 'null'
        }

@app.route('/register/user', methods = ['POST'])
def api_register_user():
    content = request.get_json()
    username = content['customerCredential']['username']
    password = content['customerCredential']['password']
    email = content['contactInfo']['email']

    userdb.add(username, { 'password': password, 'email': email })

    return { 'msg': f'User registered: {username} ({email})' }

@app.route('/users')
def api_user_list():
    return userdb.list()

@app.route('/users/<username>')
def api_user_detail(username):
    return userdb.get(username)

if __name__ == '__main__':
   app.run(debug = True)
