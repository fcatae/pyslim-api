from flask import Flask, request, redirect
from userdb import UserDb
from sessiondb import SessionDb

app = Flask(__name__)
userdb = UserDb()
sessiondb = SessionDb()

userdb.add('test', { 'password': 'test1', 'email': 'test@email.com' })

@app.route('/authenticate')
def api_auth():
    content = request.get_json()
    username = content['username']
    password = content['password']

    details = userdb.get(username)
    isValid = (details is not None) and details['password'] == password

    if( isValid ):                 
        session = sessiondb.login()

        return {
            'ID': details['ID'],
            'Authenticated': True,
            'UserId': details['UserId'],
            'Token': details['Token'],
            'SessionToken': session,
            'AccountId': details['AccountId'],
            'OMSId': details['OMSId']
        }
    
    return {
        'Authenticated': False,
        'Username': username
    }

@app.route('/Validar', methods=['POST'])
def api_validate():
    content = request.get_json()
    session = content['SessionToken']

    result = sessiondb.isLogged(session)

    return {
            'result': result
        }

@app.route('/LogOut')
def api_logout():
    content = request.get_json()
    session = content['SessionToken']
    sessiondb.logout(session)
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
   app.run(host='0.0.0.0',port=5000, debug=True)
