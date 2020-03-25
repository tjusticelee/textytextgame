from . import index
app.register_blueprint(index.bp)
app.add_url_rule('/', endpoint='index')


@app.route('/')
def index():
    return render_template('index.html')
