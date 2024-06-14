from flask import Flask, render_template
from BD import tables, anim, STOLBY


app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/list")
def list():
    print(tables)
    return render_template('list.html', tables=tables, anim=anim, stolby=STOLBY)


if __name__ == '__main__':
    app.run(debug=True)
