from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def GET():
    name = request.args.get('name')
    message = request.args.get('message')
    if name is None and message is None:
        return render_template('start.html')
    elif message is None:
        return render_template('index.html', name=name)
    elif name is not None and message is not None:
        return render_template('index.html', name=name, message=message)


