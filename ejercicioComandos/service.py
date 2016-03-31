from flask import Flask
import json
import commands
app = Flask(__name__)

@app.route("/")
def hello():
    r = commands.getoutput('ls /home |sort')
    t = r.split("\n")
    users_dict = {}
    users_dict["users"] = t
    return json.dumps(users_dict)


if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)
