from app import app
from flask import render_template, Flask, request, make_response

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/team')
def team():
    return render_template('team.html', title='More')

@app.route('/benefits')
def benefits():
    return render_template('benefits.html', title='MoreMore')

@app.route('/information')
def information():
    return render_template('information.html', title='MoreMoreMore')

@app.route('/models')
def models():
    return render_template('models.html', title='MoreMoreMoreMore')


# ------------------------------------------------------------------------------------------------------------


@app.route('/indexPL')
def indexPL():
    return render_template('PL/indexPL.html', title='Home')

@app.route('/teamPL')
def teamPL():
    return render_template('PL/teamPL.html', title='More')

@app.route('/benefitsPL')
def benefitsPL():
    return render_template('PL/benefitsPL.html', title='MoreMore')

@app.route('/informationPL')
def informationPL():
    return render_template('PL/informationPL.html', title='MoreMoreMore')

@app.route('/modelsPL')
def modelsPL():
    return render_template('PL/modelsPL.html', title='MoreMoreMoreMore')


# ------------------------------------------------------------------------------------------------------------


@app.route('/indexES')
def indexES():
    return render_template('ES/indexES.html', title='Home')

@app.route('/teamES')
def teamES():
    return render_template('ES/teamES.html', title='More')

@app.route('/benefitsES')
def benefitsES():
    return render_template('ES/benefitsES.html', title='MoreMore')

@app.route('/informationES')
def informationES():
    return render_template('ES/informationES.html', title='MoreMoreMore')

@app.route('/modelsES')
def modelsES():
    return render_template('ES/modelsES.html', title='MoreMoreMoreMore')

# ------------------------------------------------------- #

@app.context_processor
def inject_template_scope():
    actions = dict()

    def cookies_check():
        value = request.cookies.get('cookie-consent')
        return value == 'true'
    actions.update(cookies_check=cookies_check)

    def rejection():
        if not cookies_check():
            return "Sorry, cookies are not accepted."
    actions.update(rejection=rejection)

    return actions