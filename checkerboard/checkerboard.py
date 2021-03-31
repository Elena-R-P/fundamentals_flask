from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboarde():
    return render_template('index_checkerboard.html', x = 8, y = 8, color0 = 'black', color1 = 'red')

@app.route('/<x>')
def play_x(x):
    return render_template('index_checkerboard.html', x = int(x), y = 8, color0 = 'black', color1 = 'red')

@app.route('/<x>/<y>')
def play_x_y(x, y):
    return render_template('index_checkerboard.html', x = int(x), y = int(y), color0 = 'black', color1 = 'red')

@app.route('/<x>/<y>/<color0>')
def play_x_y_color(x, y, color0):
    return render_template('index_checkerboard.html', x = int(x), y = int(y), color0 = color0, color1 = 'red')

@app.route('/<x>/<y>/<color0>/<color1>')
def play_x_y_colors(x, y, color0, color1):
    return render_template('index_checkerboard.html', x = int(x), y = int(y), color0 = color0, color1 = color1)

if __name__=="__main__":
    app.run(debug=True)