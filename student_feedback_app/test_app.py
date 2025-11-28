from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name', '').strip()
    feedback = request.form.get('feedback', '').strip()

    if not name or not feedback:
        return render_template('thankyou.html', error="Name and feedback cannot be empty!")

    return render_template('thankyou.html', name=name, feedback=feedback)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
