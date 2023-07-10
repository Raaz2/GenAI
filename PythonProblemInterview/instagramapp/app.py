from flask import Flask,jsonify,request

app = Flask(__name__)


data = {
    "1" : {
        "username" : "rajeev",
        "caption" : "Hello world rajeev"
    },
    "2" : {
        "username" : "shashi",
        "caption" : "Hello world shashi"
    }
}

@app.route("/")
def hello_world():
    return "Hello Instagram"

@app.route("/all")
def viewAllPosts():
    return jsonify(data)

@app.route("/all/<id>")
def viewPostsById(id):
    return jsonify(data.get(id))

@app.route("/add", method = 'POST')
def addPosts():
    data["3"] = {
        "username" : "aman",
        "caption":"hello aman"
    }
    return "post added successfully"


if __name__ == "__main__":
    app.run(debug=True)



