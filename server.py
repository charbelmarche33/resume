# External imports
import os
import json
from flask import Flask, render_template, request, redirect, jsonify
from flask_mail import Mail

# Internal imports
from modules import helpers as hlp
from lib.consts import SENDING_EMAIL

app = Flask(__name__)
app.secret_key = os.environ.get("APP_KEY")

app.config.update(
    MAIL_SERVER="smtp.gmail.com",
    MAIL_USERNAME=SENDING_EMAIL,
    MAIL_PASSWORD=os.environ.get("EMAIL_PWD"),
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USE_TSL=False,
)

mail = Mail(app)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/send-message", methods=["POST"])
def sendMsg():
    if request.method == "POST":
        try:
            data = json.loads(request.data)
            subject = data["subject"]
            name = data["name"]
            email = data["email"]
            message = data["message"]
            hlp.send_message(mail, subject, name, email, message)
            return jsonify({"status": "success"})
        except Exception as e:
            print(e)
            return jsonify({"status": "error"})


@app.errorhandler(404)
def page_not_found(e):
    return redirect("/", code=303)


# Run the app
if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000, debug=False)
    app.run(host="0.0.0.0", port=8080, debug=True)
