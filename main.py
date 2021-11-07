from flask import Flask, render_template, request
from twilio.rest import Client
import os

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

def twilioSend(mes, number):
  message = client.messages \
                  .create(
                      body=mes,
                      from_='+12815476047',
                      to=number
                  )
  print(message.sid)

app = Flask('app', template_folder='templates', static_folder='static')

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/', methods = ['POST'])
def hello_world_post():
  btc = request.form['btc']
  doge = request.form['doge']
  if str(btc) == "1337" and str(doge) == "69420":
    # return redirect(url_for('upload'))
    twilioSend('lmao noob', '+917976066450')
    return "upload portal here"
  else:
    return "access denied"

app.run(host='0.0.0.0', port=8080)
