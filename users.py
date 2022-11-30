from flask import Flask, request, redirect
app = Flask(__name__)

@app.route('/authenticate')
def api_auth():
    content = request.get_json()
    username = content['username']
    password = content['password']

    return {
            'ID': 1,
            'Authenticated': True,
            'UserId': 123,
            'Token': 'abcde',
            'SessionToken': 'abcdefgh',
            'AccountId': '321',
            'OMSId': '1'
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
    email = content['contactInfo']['email']

    return { 'msg': f'User registered: {username} ({email})' }

if __name__ == '__main__':
   app.run(debug = True)
