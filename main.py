from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype = html>
<html>
    <head>
    <link href="https://fonts.googleapis.com/css?family=Raleway:400,500,600" rel="stylesheet">
        <style>
            section{{
                margin: 100px auto;
                width: 540px;
                position: inherit;
            }}
            .header-box {{
                background-color: #898279;
                border-radius: 7px 7px 0 0;
                width: 600px;
                height: 50px;
            }}
            h1 {{
                color: #f4f4f4;
                padding: 11px 0 0 0;
                font: 24px Raleway, sans-serif;
                font-weight: 600;
                letter-spacing: 3px;
                text-transform: uppercase;
                text-align: center;
            }}
            form {{
                background-color: #dfc12a;
                padding: 30px;
                width: 540px;
                font: 16px Raleway, sans-serif;
                letter-spacing: 1px;
                font-weight: 500;
                color: white;
                border-radius: 0 0 7px 7px;
                # box-shadow: 3px 3px 25px -5px rgba(173,173,173,1);
            }}
            textarea {{
                margin: 20px 0;
                width: 540px;
                height: 120px;
                background-color: #f4f4f4;
                border: none;
                padding: 10px;
                font: 14px Raleway, sans-serif;
                color: #898279;
                border-radius: 3px;
            }}  
            label input {{
                background-color: #f4f4f4;
                color: #898279; 

            }}
            input {{
                border: none;
                background-color: #898279;
                padding: 8px;
                font: 12px Raleway, sans-serif;
                letter-spacing: 1px;
                font-weight: 500;
                color: #f4f4f4; 
                cursor: pointer;
                border-radius: 3px;
            }}
            .submit {{
                margin: 10px 0 0 210px;
                padding: 8px 12px;
            }}
        </style> 
    </head>
    <body>
        <section>
            <div class="header-box">
                <h1>Web Caesar</h1>
            </div>
            <form action="/" method="post">
                <label for="rot">Rotate By:
                    <input id="rot" type="text" name="rot" placeholder="0" value="0"/>
                </label>
                <textarea name="text">{0}
                </textarea>
                <input class="submit" type="submit" value="Submit Query"/>
            </form>
        <section>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    encrypted_str = rotate_string(text, rot)

    return form.format(encrypted_str)

app.run()