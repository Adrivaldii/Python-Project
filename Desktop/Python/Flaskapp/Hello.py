from flask import Flask
app = Flask (__Name__)
@app.route('/')
def hello_guys():
    return 'hello guys!'
