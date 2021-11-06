from flask import Flask, render_template, request
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
    return "upload portal here"
  else:
    return "access denied"

app.run(host='0.0.0.0', port=8080)
