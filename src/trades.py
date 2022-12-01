from flask import Flask, redirect, url_for
app = Flask(__name__)
properties = { 'transaction_id': 1000}

@app.route('/exchange/trades/<oms_id>/account/<account_id>/order', methods=['GET', 'POST'])
def api_trades_account_order(oms_id, account_id):
   properties['transaction_id'] += 1
   return {
         'msg': 'success',
         'id': properties['transaction_id'] ,
         'oms': oms_id,
         'acc': account_id
      }

@app.route('/ping')
def ping():
   return {'ping': 'trades'}

print('--- TRADES started ---')

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=5000, debug=True)
