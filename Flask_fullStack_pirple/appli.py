from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('structure.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(port=7000, debug=True)