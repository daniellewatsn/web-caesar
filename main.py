from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype = html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }  
        </style> 
    </head>
    <body>
        <form action="encrypt" method="post">
            <label for="rot">Rotate By
                <input id="rot" type="text" name="rot" placeholder="0" value="0"/>
            </label>
            <textarea name="text">
            </textarea>
            <input type="submit" value="Submit Query"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/encrypt", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']

    return '<h1> New encryption:</h1> <p style="color:grey">' + rotate_string(text, rot) + '</p>'

app.run()