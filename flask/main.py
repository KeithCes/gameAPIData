from flask import Flask, render_template, request,redirect
import sys
import osrs
import league

app = Flask(__name__)


@app.route("/")
def hello(name=None):
    return render_template("index.html", name=name)
        
        
@app.route('/osrs', methods = ['POST'])
def osrsButton(name=None):
    username = request.form["osrsUsername"]
    print(osrs.main(username), file=sys.stderr)
    return redirect('/')
    
    
@app.route('/league', methods = ['POST'])
def lolButton(name=None):
    username = request.form["lolUsername"]
    print(league.main(username), file=sys.stderr)
    return redirect('/')

if __name__ == "__main__":
    app.run()
    
    