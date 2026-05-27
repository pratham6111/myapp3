from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>My Project</title>
    <style>
        body {
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
            text-align: center;
            padding-top: 100px;
        }

        .container {
            background: white;
            width: 50%;
            margin: auto;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px gray;
        }

        h1 {
            color: #2c3e50;
        }

        p {
            color: #555;
            font-size: 18px;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Welcome to My Project</h1>
        <p>This application is deployed using Flask, Docker, Jenkins, and openshift.</p>
    </div>

</body>
</html>
"""

@app.route('/')
def hello():
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
