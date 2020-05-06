from aplicacao import app

@app.route('/')
def index ():
    return 'Olá'
app.run(debug= True)    