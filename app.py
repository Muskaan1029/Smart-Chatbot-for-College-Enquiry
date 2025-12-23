from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open("responses.json") as f:
    responses = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_msg = request.form["msg"].lower()

    if "course" in user_msg:
        reply = responses["courses"]
    elif "admission" in user_msg:
        reply = responses["admission"]
    elif "fee" in user_msg:
        reply = responses["fees"]
    elif "hostel" in user_msg:
        reply = responses["hostel"]
    elif "contact" in user_msg:
        reply = responses["contact"]
    else:
        reply = "Sorry, I didn't understand. Please ask about courses, admission, fees, hostel, or contact."

    return jsonify(reply)

if __name__ == "__main__":
    app.run(debug=True)
