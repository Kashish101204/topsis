from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os, re
from topsis import topsis

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Email config (use app password)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='kgupta6_be23@thapar.edu',
    MAIL_PASSWORD='abcdefghijklmnop'
)


mail = Mail(app)

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        weights = request.form["weights"].split(",")
        impacts = request.form["impacts"].split(",")
        email = request.form["email"]

        if len(weights) != len(impacts):
            return "Weights and impacts count mismatch!"

        if not is_valid_email(email):
            return "Invalid email format!"

        weights = list(map(float, weights))

        for i in impacts:
            if i not in ['+', '-']:
                return "Impacts must be + or - only!"

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(OUTPUT_FOLDER, "result.csv")
        file.save(input_path)

        topsis(input_path, weights, impacts, output_path)

        msg = Message("TOPSIS Result",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[email])
        msg.body = "Please find attached TOPSIS result."
        msg.attach("result.csv", "text/csv", open(output_path, "rb").read())

        mail.send(msg)

        return "Result sent to your email!"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
