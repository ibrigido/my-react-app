from flask import Flask 

app = Flask(__name__)

#create route API for memebers 
@app.route("/members")
def members():
    return {"members" :["Member1", "Member2", "Member3"]}

@app.route('/')
def home():
    return {"message": "Welcome to the flask server- Ivanna"}

if __name__ == "__main__":
    app.run(debug=True)

