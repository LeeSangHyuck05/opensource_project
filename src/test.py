from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    #return 수정
    return "FLASK TEST"

if __name__ == '__main__':
    app.run(debug=True)
