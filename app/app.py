from flask import Flask
from time import gmtime, strftime

app = Flask(__name__)

def make_time_now():
    return strftime("%a, %d %b %Y %H:%M", gmtime())

@app.route('/')
def hello():
    time_now = make_time_now()
    html = "<h3>Hello!</h3>" \
           "<b>Time now is:</b> {} <br/>" \

    return html.format(time_now)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
