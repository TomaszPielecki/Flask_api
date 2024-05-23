from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/O_Nas.html')
def O_Nas():
    return render_template('O_Nas.html')


@app.route('/Sklep.html')
def Sklep():
    return render_template('Sklep.html', Sklep='Witaj na stronie sklepu')


@app.route('/Kierowcy.html')
def Kierowcy():
    return render_template('Kierowcy.html')


@app.route('/Kontakt.html')
def Kontakt():
    return render_template('Kontakt.html')


if __name__ == '__main__':
    import os

    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '3001'))
    except ValueError:
        PORT = 3001
    app.run(HOST, PORT, debug=True)
