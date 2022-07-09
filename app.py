from flask import Flask,render_template
import pandas as pd
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Line,Bar,Page,Map

app= Flask(__name__)

@app.route('/')
def helle_world():
    return render_template(
        'home.html')

@app.route('/a')
def a():

    with open("a.html", encoding="utf8", mode="r") as f:
        plot_a = "".join(f.readlines())
    return render_template(
        'index.html',rl=plot_a)


@app.route('/b')
def b():

    with open("b.html", encoding="utf8", mode="r") as f:
        plot_a = "".join(f.readlines())
    return render_template(
        'index.html', rl=plot_a)

@app.route('/c')
def c():
    with open("c.html", encoding="utf8", mode="r") as f:
        plot_a = "".join(f.readlines())
    return render_template(
        'index.html', rl=plot_a)

@app.route('/d')
def d():

    with open("d.html", encoding="utf8", mode="r") as f:
        plot_a = "".join(f.readlines())
    return render_template(
        'index.html', rl=plot_a)

@app.route('/e')
def e():

    with open("e.html", encoding="utf8", mode="r") as f:
        plot_a = "".join(f.readlines())
    return render_template(
        'index.html', rl=plot_a)

    
if __name__ == '__main__':
    app.run(debug=True)