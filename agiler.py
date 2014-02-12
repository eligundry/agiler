from flask import Flask, Blueprint, render_template
import yaml

app = Flask(__name__)
config = yaml.load(open('config.yml', 'r+'))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
