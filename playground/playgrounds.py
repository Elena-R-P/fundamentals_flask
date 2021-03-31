from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def welcome_page():
    return redirect('/play')

@app.route('/play')
def play():
    return render_template('index.html')

@app.route('/play/<x>')
def play_x(x):
    return render_template('index2.html', times=int(x))

@app.route('/play/<x>/<color>')
def play_x_color(x, color):
    return render_template('index_color.html', times=int(x), color=color)

if __name__=="__main__":
    app.run(debug=True)