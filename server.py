import os
from flask import (
    Flask,
    render_template,
)

# from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = os.environ.get("APP_KEY")

app.config.update(
    MAIL_SERVER="mail.privateemail.com",
    MAIL_USERNAME="info@novacards.ai",
    MAIL_PASSWORD=os.environ.get("EMAILPWD"),
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USE_TSL=False,
)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

