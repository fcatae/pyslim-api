from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/exchange/trades/<oms_id>/account/<account_id>/order')
def api_trades_account_order(oms_id, account_id):
   return {
         'msg': 'test: trades',
         'oms': oms_id,
         'acc': account_id
      }

if __name__ == '__main__':
   app.run(debug = True)
