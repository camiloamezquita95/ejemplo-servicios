from flask import Flask, g
import json
import commands
app = Flask(__name__)

@app.route("/api/v1.0/usermgt/users",methods=['GET'])

def hello():
    r = commands.getoutput('ls /home |sort')
    t = r.split("\n")
    users_dict = {}
    users_dict["users"] = t
    return json.dumps(users_dict)



if __name__ == "__main__":
    g.users = hello()
    app.run('0.0.0.0',debug=True)
