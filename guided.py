from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)
app.secret_key = 'kadibgandligjad'

@app.route('/')
def home():
    return 'Hello World'

@app.route('/form')
def index():
    return render_template('index.html')

@app.route('/handle_form', methods=['POST'])
def handle_form():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    return redirect('/')

@app.route('/new_route')
def new_route():
    return render_template('info.html', first_name = session['first_name'], last_name = session['last_name'])

if __name__ == '__main__':
    app.run(debug=True)